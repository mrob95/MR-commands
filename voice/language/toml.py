from voice.imports import *

BINDINGS = utilities.load_toml_relative("config/toml.toml")

Breathe.add_commands(
    AppContext(title=".toml"),
    {
        "<command>":
            Alternating("command"),

        "command that":
            Key("end, s-home") + Key("c-c") + Key("quote, right:2, space, equal, space, quote") + Key("c-v"),

    },
    [
        Choice("command", BINDINGS["commands"]),
    ]
)
