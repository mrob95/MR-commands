from voice.imports import *

BINDINGS = utilities.load_toml_relative("config/C.toml")

Breathe.add_commands(
    AppContext(title=BINDINGS["title_contexts"]),
    {
        "<command>": Alternating("command"),
        BINDINGS["function_prefix"] + " <fun>": Text("%(fun)s()") + Key("left"),
        "valley <types>": Text("%(types)s ;") + Key("left"),
        "type <types>": Text("%(types)s"),
        "function <types>": Text("%(types)s  () {}")
        + Key("left, enter, up, end, left:3"),
    },
    extras=[
        Choice("command", BINDINGS["commands"]),
        Choice("fun", BINDINGS["functions"]),
        Choice("types", BINDINGS["types"]),
    ],
)

