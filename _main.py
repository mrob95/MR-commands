import time
start = time.time()
import logging
import importlib

logging.basicConfig()
import sys, os

# BASE_PATH = os.path.realpath(__file__).split("\\_main.py")[0].replace("\\", "/")
# sys.path.append(BASE_PATH)

from voice.imports import *

# from voice.core import globals
# from voice.core import alphanumeric, keys, misc, mouse, punctuation, text, windows
# from voice.apps import chrome, vscode, explorer, terminal, kindle
# from voice.language import python, standardml, markdown, toml, C

if get_engine()._name == "natlink":
    from voice.utils import modes

extras_module = {
    "voice": {
        "core": "globals",
    }
}
modules = {
    "voice": {
        "core": ["alphanumeric", "keys", "misc", "mouse", "punctuation", "text", "windows"],
        "apps": ["chrome", "vscode", "explorer", "terminal", "kindle"],
        "language": ["python", "standardml", "markdown", "toml", "C"],
    }
}

Breathe.load_modules(extras_module)
Breathe.load_modules(modules)


elapsed = time.time()-start
print("%s elapsed" % elapsed)

