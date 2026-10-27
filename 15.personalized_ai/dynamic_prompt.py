"""Personalise the system prompt on every call, from the stored profile."""

from dataclasses import dataclass
from profile import UserProfile, get_profile, store, update_profile

from langchain.agents import create_agent
from langchain.agents.middleware import ModelRequest, dynamic_prompt
from langgraph.checkpoint.memory import InMemorySaver
from model import model

BASE = "You are a helpful assistant for the Parottasalna community."


def build_system_prompt(p: UserProfile) -> str:
    lines = [BASE]
    if p.name:
        lines.append(
            f"The user's name is {p.name}. Use it sometimes, not in every reply."
        )
    if p.language != "english":
        lines.append(f"Reply in {p.language}.")
    lines.append(
        {
            "beginner": "Explain simply, with everyday examples and no jargon.",
            "intermediate": "Assume basic knowledge; keep explanations short.",
            "expert": "Be concise and technical; skip the basics.",
        }[p.expertise]
    )
    lines.append("Tone: formal." if p.tone == "formal" else "Tone: warm and friendly.")
    if p.allergies:
        lines.append(
            "SAFETY: the user is allergic to "
            + ", ".join(p.allergies)
            + ". Never suggest these."
        )
    if p.interests:
        lines.append(
            "Examples may draw on their interests: " + ", ".join(p.interests) + "."
        )
    return "\n".join(lines)


@dataclass
class Context:
    user_id: str


@dynamic_prompt  # runs before every model call
def personalised(request: ModelRequest) -> str:
    return build_system_prompt(get_profile(request.runtime.context.name))


def make_agent(llm):
    return create_agent(
        model=llm,
        tools=[],
        middleware=[personalised],
        context_schema=Context,
        store=store,
        checkpointer=InMemorySaver(),
    )


@dataclass
class Context:
    name: str


if __name__ == "__main__":
    update_profile(
        "jafer",
        name="Jafer",
        language="tanglish",
        interests=["chess"],
        allergies=["peanuts"],
    )
    update_profile("priya", name="Priya", expertise="expert", tone="formal")
    for uid in ("jafer", "priya", "new-user"):
        print(f"===== {uid}")
        print(build_system_prompt(get_profile(uid)))
    agent = make_agent(model)
    config = {"configurable": {"thread_id": "1", "name": "Jafer"}}
    response = agent.invoke(
        {
            "messages": [
                {
                    "role": "user",
                    "content": "greet me and suggest me how to do peanut chutney",
                }
            ]
        },
        config=config,
        context=Context(name="priya"),
    )
    print(response)
