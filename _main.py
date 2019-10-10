import logging

logging.basicConfig()
import sys, os

BASE_PATH = os.path.realpath(__file__).split("\\_main.py")[0].replace("\\", "/")
sys.path.append(BASE_PATH)

from voice.imports import *


from voice.core import globals
from voice.core import alphanumeric, keys, misc, mouse, punctuation, text, windows
from voice.apps import chrome, vscode, explorer, terminal, kindle
from voice.language import python, standardml, markdown, toml, C

if get_engine()._name == "natlink":
    from voice.utils import modes

    Breathe.add_commands(None, {"reboot dragon": Function(utilities.reboot)}, ccr=False)

