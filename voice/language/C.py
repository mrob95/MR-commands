from voice.imports import *

BINDINGS = utilities.load_toml_relative("config/C.toml")

Breathe.add_commands(
    AppContext(title=BINDINGS["title_contexts"]),
    {
        "<command>": Alternating("command"),
        "fun <fun>": Read("previous")
        + Text("%(fun)s(%(previous)s);")
        + Function(lambda previous: Key("" if previous else "left:2").execute()),
        "valley <types>": Text("%(types)s ;") + Key("left"),
        "type <types>": Text("%(types)s"),
        "function <types>": Text("%(types)s  () {}")
        + Key("left, enter, up, end, left:3"),
        "arrow [<snaketext>]": Text("->%(snaketext)s"),
    },
    extras=[
        Dictation("snaketext", "").lower().replace(" ", "_"),
        Choice("command", BINDINGS["commands"]),
        Choice("fun", BINDINGS["functions"]),
        Choice("types", BINDINGS["types"]),
    ],
)

Breathe.add_commands(
    AppContext(title=BINDINGS["title_contexts"]),
    {"comment [<text>]": lambda text: Text("// %s" % text.capitalize()).execute()},
    ccr=False,
)

