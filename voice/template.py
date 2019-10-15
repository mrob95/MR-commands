from voice.imports import *

BINDINGS = utilities.load_toml_relative("config/.toml")

Breathe.add_commands(
    AppContext(title=BINDINGS["title_contexts"]),
    {

    },
    [

    ],
)
