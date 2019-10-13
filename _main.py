import time
start = time.time()
import logging
logging.basicConfig()

from voice.imports import *

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

