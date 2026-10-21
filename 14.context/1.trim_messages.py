"""trim_messages: three ways to cut a history down to a budget."""

from langchain_core.messages import AIMessage, HumanMessage, SystemMessage
from langchain_core.messages.utils import count_tokens_approximately, trim_messages

history = [
    SystemMessage("You are a helpful assistant."),
    HumanMessage("My name is Jafer and I live in Coimbatore."),
    AIMessage("Nice to meet you, Jafer!"),
    HumanMessage("I teach backend and AI engineering."),
    AIMessage("That sounds like a great job."),
    HumanMessage("Suggest a weekend plan."),
    AIMessage("How about a short trek near Valparai?"),
    HumanMessage("What is my name?"),
]


def show(title, msgs):
    print(
        f"--- {title} ({len(msgs)} messages, {count_tokens_approximately(msgs)} tokens)"
    )
    for m in msgs:
        print(f"  {m.type:<6} {m.content}")


common = dict(token_counter=count_tokens_approximately, max_tokens=70)

print(common)
# 1. keep the NEWEST messages that fit (the usual choice)
# show(
#     "last, keep system",
#     trim_messages(
#         history, strategy="last", include_system=True, start_on="human", **common
#     ),
# )

# # 2. keep the OLDEST messages that fit (rare: keep the beginning of a document)
# show("first", trim_messages(history, strategy="first", **common))

# # 3. allow a message to be cut in the middle (words, not whole messages)
show(
    "last, partial",
    trim_messages(
        history,
        strategy="last",
        allow_partial=True,
        text_splitter=lambda t: t.split(" "),
        **common,
    ),
)
