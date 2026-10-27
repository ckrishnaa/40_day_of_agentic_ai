"""Three kinds of personal memory, each stored and recalled differently."""

import uuid

from langgraph.store.memory import InMemoryStore

store = InMemoryStore()
USER = "jafer"

# 1. PROFILE (facts that are true now): one small record, always loaded
store.put(
    ("profile", USER),
    "main",
    {"name": "Jafer", "city": "Coimbatore", "language": "tanglish"},
)

# 2. EPISODES (things that happened): many records, recalled only when relevant
for text in [
    "Asked for a Kerala trip plan in December; budget 40,000 rupees.",
    "Debugged a Django migration error together.",
    "Said the long answers were too wordy.",
]:
    store.put(("episodes", USER), str(uuid.uuid4()), {"text": text})

# 3. PROCEDURES (how to behave with this user): learned from feedback, edited rarely
store.put(
    ("procedures", USER),
    "style",
    {"rule": "Keep answers under 5 lines unless asked for detail."},
)


def assemble(user_id):
    item = store.get(("profile", user_id), "main")
    profile = item.value if item else {}
    episodes = [i.value["text"] for i in store.search(("episodes", user_id))]
    rules = [i.value["rule"] for i in store.search(("procedures", user_id))]
    return profile, episodes, rules


profile, episodes, rules = assemble(USER)
print("PROFILE   :", profile)
print("EPISODES  :", len(episodes), "stored ->", episodes[0])
print("PROCEDURES:", rules)
print(
    "another user:", assemble("priya")[1:]
)  # empty folders: nothing leaks between users
