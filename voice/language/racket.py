from voice.imports import *

BINDINGS = utilities.load_toml_relative("config/racket.toml")

Breathe.add_commands(
    AppContext(title=BINDINGS["title_contexts"]),
    {
        "<command>": Alternating("command"),
        BINDINGS["function_prefix"] + " <fun>":
            Text("(%(fun)s )") + Key("left"),
    },
    [
        Choice("command", BINDINGS["commands"]),
        Choice("fun", BINDINGS["functions"]),
    ],
)