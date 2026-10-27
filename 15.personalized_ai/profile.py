"""A user profile: structured facts, one folder per user, safe to update."""

from datetime import datetime, timezone
from typing import Literal

from langgraph.store.memory import InMemoryStore
from pydantic import BaseModel, Field


class UserProfile(BaseModel):
    name: str | None = None
    city: str | None = None
    language: Literal["english", "tamil", "tanglish"] = "english"
    expertise: Literal["beginner", "intermediate", "expert"] = "beginner"
    tone: Literal["formal", "friendly"] = "friendly"
    interests: list[str] = Field(default_factory=list)
    allergies: list[str] = Field(default_factory=list)
    updated_at: str = ""


store = InMemoryStore()


def get_profile(user_id: str) -> UserProfile:
    item = store.get(("profiles", user_id), "main")  # (folder, file name)
    return UserProfile(**item.value) if item else UserProfile()


def update_profile(user_id: str, **changes) -> UserProfile: # UPSERT -> Update + Insert
    """Merge changes into the profile. Lists are added to, not replaced."""
    profile = get_profile(user_id)
    for key, value in changes.items():
        current = getattr(profile, key)
        if isinstance(current, list):
            setattr(profile, key, sorted(set(current) | set(value)))
        else:
            setattr(profile, key, value)
    profile.updated_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    store.put(("profiles", user_id), "main", profile.model_dump())
    return profile


if __name__ == "__main__":
    update_profile(
        "jafer",
        name="Jafer",
        city="Coimbatore",
        language="tanglish",
        interests=["chess"],
    )
    update_profile("jafer", interests=["cricket", "chess"], allergies=["peanuts"])
    update_profile("priya", name="Priya", expertise="expert", tone="formal")

    for uid in ("jafer", "priya", "stranger"):
        p = get_profile(uid).model_dump(exclude={"updated_at"})
        print(uid, "->", p)
