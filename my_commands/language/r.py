from my_commands.imports import *

BINDINGS = utilities.load_toml_relative("config/r.toml")
rcontext = AppContext(title=BINDINGS["title_contexts"]) & ~AppContext(title=".rkt")

def rfunc(rf, selection):
    if isinstance(rf, string_types):
        action = Text("%s(%s)" % (rf, selection)) + Key("" if selection else "left")
    else:
        action = (
            Text("%s(%s)" % (rf[0], selection))
            + Key("left")
            + Key("comma, space" if selection else "")
            + Text(rf[1])
            + Key("left:%s" % rf[2])
        )
    action.execute()


Breathe.add_commands(
    rcontext,
    {
        "cheat sheet <module>": Function(
            lambda module: Popen(
                ["SumatraPDF", "C:/Users/Mike/Documents/cheatsheets/R/%s.pdf" % module]
            )
        )
    },
    [Choice("module", BINDINGS["cheatsheets"])],
    ccr=False,
)

Breathe.add_commands(
    rcontext,
    {
        "<command>": Alternating("command"),
        "fun <function>": Read("selection")
        + Function(lambda function, selection: rfunc(function, selection)),
        "plot <ggfun>": Read("selection")
        + Function(lambda ggfun, selection: rfunc(ggfun, selection)),
        "model <modelargs>": Text("%(modelargs)s"),
        "library <library>": Text("library(%(library)s)") + Key("end"),
    },
    [
        Choice("command", BINDINGS["commands"]),
        Choice("function", BINDINGS["r_functions"]),
        Choice("ggfun", BINDINGS["r_graph"]),
        Choice("modelargs", BINDINGS["r_model"]),
        Choice("library", BINDINGS["libraries"]),
    ],
)
