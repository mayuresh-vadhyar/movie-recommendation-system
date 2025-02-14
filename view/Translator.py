import json
import os

LANG_FILE = "./view/en_us.json"

def loadStrings():
    if not os.path.exists(LANG_FILE):
        raise FileNotFoundError(f"Language file {LANG_FILE} not found.")

    with open(LANG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

_strings = loadStrings()

def getString(key, default=""):
    return _strings.get(key, default)