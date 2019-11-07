from voice.imports import *

BINDINGS = utilities.load_toml_relative("config/standardml.toml")

def insert_type(smltype, types, islist):
    Text(smltype).execute()
    if types:
        for t in types:
            Text(" * %s" % t).execute()
    if islist:
        Text(" list").execute()

Breathe.add_commands(
    AppContext(title=BINDINGS["title_contexts"]),
    {
        "<command>": Alternating("command"),
        BINDINGS["function_prefix"] + " <monad>": Text("%(monad)s "),
        BINDINGS["function_prefix"] + " <fun>": Text("%(fun)s()") + Key("left"),
        "type <smltype> [star <types>] [<islist>]":
            Function(insert_type),
    },
    [
        Choice("command", BINDINGS["commands"]),
        Choice("fun", BINDINGS["functions"]),
        Choice("monad", BINDINGS["monads"]),
        Choice("smltype",    BINDINGS["types"]),
        Repetition(
            Choice("",BINDINGS["types"]),
            1, 4, name="types", default=""
            ),
        Boolean("islist", "list"),
    ],
)

