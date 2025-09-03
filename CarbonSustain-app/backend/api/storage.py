import json
import os
from datetime import date

FILE_PATH = "actions.json"

def load_actions():
    if not os.path.exists(FILE_PATH):
        return []
    with open(FILE_PATH, "r") as f:
        return json.load(f)

def serialize_action(action):
    result = action.copy()
    if isinstance(result.get("date"), date):
        result["date"] = result["date"].isoformat()
    return result

def save_actions(actions):
    with open(FILE_PATH, "w") as f:
        json.dump([serialize_action(a) for a in actions], f, indent = 4)

