profiling = False
if profiling:
    import cProfile, pstats

    pr = cProfile.Profile()
    pr.enable()

import time

start = time.time()
import logging

logging.basicConfig()

from voice.imports import *

if get_engine()._name == "natlink":
    from voice.utils import modes

extras_module = {"voice": {"core": "globals"}}
modules = {
    "voice": {
        "core": [
            "alphanumeric",
            # "alias",
            "keys",
            "misc",
            "mouse",
            "punctuation",
            "text",
            "windows",
        ],
        "apps": [
            "chrome",
            "vscode",
            "explorer",
            "terminal",
            "kindle",
            "rstudio",
            "spotify",
            "photoshop",
            # "lyx",
            # "ScientificNotebook55",
        ],
        "language": ["python", "standardml", "markdown", "toml", "C", "r"],
    }
}

Breathe.load_modules(extras_module)
Breathe.load_modules(modules)


elapsed = time.time() - start
print("%s elapsed" % elapsed)

if profiling:
    pr.disable()
    out_stream = open("C:/Users/Mike/Documents/GitHub/new_merger2/stats7.log", "w+")
    # sortby = "tottime"
    sortby = 'cumtime'
    ps = (
        pstats.Stats(pr, stream=out_stream)
        .strip_dirs()
        .sort_stats(sortby)
        .print_stats(0.3)
    )
    out_stream.close()
