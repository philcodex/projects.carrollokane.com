import time

def find_inactive_users(users, days=90):
    cutoff = time.time() - (days * 86400)
    return [
        u for u in users
        if not u.get("deleted")
        and u.get("updated", 0) < cutoff
    ]

# Example usage
users = [
    {"id": "U001", "name": "alice", "deleted": False, "updated": 1700000000},
    {"id": "U002", "name": "bob",   "deleted": False, "updated": time.time()},
    {"id": "U003", "name": "carol", "deleted": True,  "updated": 1700000000},
]

print(find_inactive_users(users))

import time
print(time.time()) 