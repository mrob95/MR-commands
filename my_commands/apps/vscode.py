from my_commands.imports import *


def Wait(n=1):
    return Pause(str(15 * n))


def Pallette(command):
    return Key("cs-p") + Wait() + Text(command) + Key("enter")


Breathe.add_commands(
    AppContext(executable="Code.exe"),
    {
        "comment block": Key("sa-a"),
        "new (file | tab)": Key("c-n"),
        "new window": Key("cs-n"),
        "open file": Key("c-o"),
        "open folder": Key("c-k, c-o"),
        "open recent": Key("c-r"),
        "save as": Key("cs-s"),
        "save all": Key("c-k, s"),
        "revert (file | changes)": Pallette("revert file"),
        "close tab": Key("c-w"),
        "close all tabs": Key("c-k, c-w"),
        "next tab": Key("c-pgdown"),
        "previous tab": Key("c-pgup"),
        "<nth> tab": Key("a-%(nth)s"),
        #
        "terminal here": Key("cs-c"),
        "explorer here": Key("sa-r"),
        #
        "find": Key("c-f"),
        "find <text>": Key("c-f") + Wait() + Text("%(text)s") + Key("escape"),
        "find next [<n>]": Key("f3") * Repeat("n"),
        "find previous [<n>]": Key("s-enter") * Repeat("n"),
        "find all": Key("a-enter"),
        "replace": Key("c-h"),
        "search in directory": Key("cs-f"),
        "search for that": Key("cs-f") + Wait() + Key("enter"),
        #
        "go to <text> [<filetype>]": Key("c-p")
        + Wait()
        + Text("%(text)s" + "%(filetype)s")
        + Wait()
        + Key("enter"),
        "go to word": Key("c-semicolon"),
        "go to symbol": Key("cs-o"),
        "go to [symbol in] project": Key("c-t"),
        "go to that": Key("f12"),
        "peek (definition | that)": Key("a-f12"),
        "command pallette [<text>]": Key("cs-p") + Text("%(text)s"),
        "rename symbol": Key("f2"),
        #
        "edit lines": Key("sa-i"),
        "sort lines": Pallette("sort ascending"),
        "edit next [<n>]": Key("c-d") * Repeat("n"),
        "skip next [<n>]": Key("c-k, c-d") * Repeat("n"),
        "edit all": Key("cs-l"),
        "<action> [line] <ln1> [by <ln2>]": Function(navigation.action_lines),
        "<action> by [line] <ln1>": Key("c-k, c-space, c-g")
        + Function(lambda ln1: Text(str(ln1 + 1)).execute())
        + Key("enter, c-k, c-a, %(action)s, c-k, c-g"),
        #
        "transform upper": Pallette("uppercase"),
        "transform lower": Pallette("lowercase"),
        "transform title": Pallette("titlecase"),
        #
        "fold": Key("cs-lbracket"),
        "unfold": Key("cs-rbracket"),
        "unfold all": Key("c-k, c-j"),
        "fold [level] <n2>": Key("c-k, c-%(n2)s"),
        #
        "full screen": Key("f11"),
        "toggle side bar": Key("c-b"),
        "(toggle | show) problems": Key("cs-m"),
        "flash problems": Key("cs-m") + Pause("50") + Key("cs-m"),
        "show extensions": Key("cs-x"),
        "show explorer": Key("cs-e"),
        "show terminal": Key("c-apostrophe"),
        "new terminal": Key("cs-apostrophe"),
        "show python repel": Key("cs-p") + Wait() + Text("pyrepl\n"),
        "open settings": Key("c-comma"),
        "open keyboard shortcuts": Key("c-k, c-s"),
        #
        "build it": Key("c-b"),
        "build with": Key("cs-b"),
        "format document": Key("as-f"),
        "preview html": Key("cs-v"),
        #
        "column <cols>": Key("as-%(cols)s"),
        "focus <panel>": Key("c-k, c-%(panel)s"),
        "move <panel>": Key("c-k, cs-%(panel)s"),
        # "split right": Key("c-backslash"),
        "split right": Key("as-2, c-k, cs-right"),
        "split definition": Key("c-k, f12"),
    },
    [
        ShortIntegerRef("ln1", 1, 1000),
        ShortIntegerRef("ln2", 1, 1000, 0),
        IntegerRef("n2", 1, 9, 1),
        Choice("action", navigation.actions),
        Choice(
            "nth",
            {
                "first": "1",
                "second": "2",
                "third": "3",
                "fourth": "4",
                "fifth": "5",
                "sixth": "6",
                "seventh": "7",
                "eighth": "8",
                "last": "9",
            },
        ),
        Choice("cols", {"one": "1", "two": "2", "three": "3", "grid": "5"}),
        Choice("panel", {"up": "up", "down": "down", "left": "left", "right": "right"}),
        Choice(
            "filetype",
            {
                "pie | python": "py",
                "mark [down]": "md",
                "tech": "tex",
                "tommel": "toml",
            },
            "",
        ),
    ],
    ccr=False,
)

Breathe.add_commands(
    AppContext(executable="Code.exe"),
    {
        "[<end>] line <ln1>": Key("c-g")
        + Wait()
        + Text("%(ln1)s")
        + Key("enter")
        + Key("%(end)s"),
        "shunt [<n>]": Key("s-down:%(n)s"),
        "(go to | good) file": Key("c-p"),
        "comment line": Key("c-slash"),
        "indent [<n2>]": Key("c-rbracket:%(n2)s"),
        "[auto] complete": Key("c-space"),
        "meta sell": Key("sa-;") + Wait(),
        "meta go": Key("c-;") + Wait(),
    },
    [
        ShortIntegerRef("ln1", 1, 1000),
        IntegerRef("n2", 1, 9, 1),
        Choice("end", "end", ""),
    ],
)

