from my_commands.imports import *

BINDINGS = utilities.load_toml_relative("config/r.toml")


def helper(function):
    if type(function) in ["str", "unicode"]:
        Text(function).execute()
        Pause("50").execute()
    else:
        Text(function[0]).execute()
        Pause("50").execute()


Breathe.add_commands(
    AppContext(executable="rstudio"),
    {
        "new (file | tab)": Key("cs-n"),
        "open file": Key("c-o"),
        "go to file": Key("c-dot"),
        "open recent": Mouse("[20, 34], left") + Key("down:5, right"),
        "open project": Mouse("[20, 34], left") + Key("down:6, enter"),
        "open recent project": Mouse("[20, 34], left") + Key("down:8, right"),
        "save all": Key("ac-s"),
        "select all": Key("c-a"),
        "find": Key("c-f"),
        "find that": Key("c-f3"),
        "align that": Key("c-i"),
        "[go to] line <ln1>": Key("as-g/10") + Text("%(ln1)s") + Key("enter"),
        "focus <screen_element>": Key("%(screen_element)s"),
        "next tab": Key("c-f12"),
        "first tab": Key("cs-f11"),
        "previous tab": Key("c-f11"),
        "last tab": Key("cs-f12"),
        "close tab": Key("c-w"),
        "run (line | that)": Key("c-enter"),
        "(run document | build it)": Key("ac-r"),
        "comment (line | selected | block)": Key("cs-c"),
        "knit (document | file)": Key("cs-k"),
        "next plot": Key("ac-f12"),
        "previous plot": Key("ac-f11"),
        "create function": Key("ca-x"),
        "create variable": Key("ca-v"),
        "rename that": Key("cas-m"),
        # ------------------------------------------------
        "help that": Read("selection")
        + Key("c-2, question")
        + Text("%(selection)s")
        + Key("enter/50, c-1"),
        # ------------------------------------------------
        "help <function>": Key("c-2, question")
        + Function(helper)
        + Key("enter/50, c-1"),
        # ------------------------------------------------
        "help graph <graph>": Key("c-2, question")
        + Function(lambda graph: helper(graph))
        + Key("enter/50, c-1"),
        #------------------------------------------------
        "glimpse that": Read("selection")
        + Key("c-2")
        + Text("%(selection)s")
        + Text(" %>%  glimpse()", static=True)
        + Key("enter/50, c-1"),
        #------------------------------------------------
        "head that": Read("selection")
        + Key("c-2")
        + Text("%(selection)s %%>%% head()")
        + Key("enter/50, c-1"),
        #------------------------------------------------
        "vee table that": Read("selection")
        + Key("c-2")
        + Text("library(vtable)")
        + Key("enter/50")
        + Text("%(selection)s %%>%% vtable()")
        + Key("enter/50, c-1"),
        #------------------------------------------------
        "<action> [line] <ln1> [by <ln2>]": Function(
            navigation.action_lines,
            go_to_line="as-g/10",
            select_line_down="s-down",
            wait="/3",
        ),
    },
    [
        ShortIntegerRef("ln1", 1, 1000),
        ShortIntegerRef("ln2", 1, 1000, 0),
        Choice("function", BINDINGS["r_functions"]),
        Choice("graph", BINDINGS["r_graph"]),
        Choice(
            "screen_element",
            {
                "(main | editor)": "c-1",
                "console": "c-2",
                "terminal": "as-t",
                "help": "c-3",
                "history": "c-4",
                "files": "c-5",
                "plots": "c-6",
                "packages": "c-7",
                "environment": "c-8",
                "viewer": "c-9",
                "git": "c-f1",
                "connections": "c-f5",
            },
        ),
        Choice("action", navigation.actions),
    ],
    ccr=False
)
