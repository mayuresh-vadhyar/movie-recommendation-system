import json
import os
from constants import GUI as constants

def loadStrings():
    if not os.path.exists(constants.LANG_FILE):
        raise FileNotFoundError(f"Language file {constants.LANG_FILE} not found.")

    with open(constants.LANG_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

_strings = loadStrings()

def getString(key, default=""):
    return _strings.get(key, default)