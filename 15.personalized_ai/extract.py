"""Learn the profile from conversation: an LLM reads a message and returns only what is NEW."""

from profile import get_profile, update_profile
from typing import Literal

from model import llm
from pydantic import BaseModel, Field


class ProfileUpdate(BaseModel):
    """Facts the user stated about themselves in THIS message. Leave a field empty if not stated."""

    name: str | None = None
    city: str | None = None
    language: Literal["english", "tamil", "tanglish"] | None = None
    expertise: Literal["beginner", "intermediate", "expert"] | None = None
    interests: list[str] = Field(default_factory=list)
    allergies: list[str] = Field(default_factory=list)


extractor = llm.with_structured_output(ProfileUpdate)


def learn_from(user_id: str, message: str):
    update = extractor.invoke(
        "Extract only facts the user explicitly states about themselves. Do not guess.\n"
        f"Message: {message}"
    )
    changes = {k: v for k, v in update.model_dump().items() if v}  # drop empty fields
    if changes:
        update_profile(user_id, **changes)
    return changes


if __name__ == "__main__":
    for text in [
        "Hi, I'm Arun from Madurai. Please talk to me in Tanglish.",
        "I'm allergic to peanuts and I love trekking.",
        "What's the weather like today?",
    ]:
        print(repr(text), "->", learn_from("arun", text))
    print(get_profile("arun").model_dump(exclude={"updated_at"}))
