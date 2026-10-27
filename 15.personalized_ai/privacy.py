"""Personal memory is personal data: let users see it, export it and delete it."""

import json
import time

from langgraph.store.memory import InMemoryStore

store = InMemoryStore()
FOLDERS = ("profile", "episodes", "procedures")


def remember(user_id, folder, key, value, ttl_days=None):
    if ttl_days:
        value = {**value, "expires_at": time.time() + ttl_days * 86400}
    store.put((folder, user_id), key, value)


def export_all(user_id):
    """'Show me everything you know about me.'"""
    return {
        f: {
            i.key: {
                k: v for k, v in i.value.items() if k != "expires_at"
            }  # hide internal fields
            for i in store.search((f, user_id))
        }
        for f in FOLDERS
    }


def forget_all(user_id):
    """'Delete everything.'"""
    for f in FOLDERS:
        for i in store.search((f, user_id)):
            store.delete((f, user_id), i.key)


def purge_expired(user_id):
    for f in FOLDERS:
        for i in store.search((f, user_id)):
            if i.value.get("expires_at", float("inf")) < time.time():
                store.delete((f, user_id), i.key)


remember("jafer", "profile", "main", {"name": "Jafer", "city": "Coimbatore"})
remember("jafer", "episodes", "e1", {"text": "Asked about Kerala trip"}, ttl_days=30)
remember(
    "jafer", "episodes", "e2", {"text": "Old temporary note"}, ttl_days=-1
)  # already expired

purge_expired("jafer")
print(json.dumps(export_all("jafer"), indent=2))
forget_all("jafer")
print("after forget_all:", export_all("jafer"))
