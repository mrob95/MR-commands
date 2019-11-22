from my_commands.imports import *

BINDINGS = utilities.load_toml_relative("config/.toml")

Breathe.add_commands(
    AppContext(title=BINDINGS["title_contexts"]),
    {

    },
    [

    ],
)
