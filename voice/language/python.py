from voice.imports import *

BINDINGS = utilities.load_toml_relative("config/python.toml")

Breathe.add_commands(
    AppContext(title=BINDINGS["title_contexts"]),
    {
        # "create setters":
        #     Function(execution.python_setters),
        "magic <umeth>": Text("def __%(umeth)s__(self):"),
        "magic [<right>] <bmeth>": Text("def __%(right)s%(bmeth)s__(self, other):"),
        "magic <mmeth>": lambda mmeth: Text(
            "def __%s__(%s):" % (mmeth[0], mmeth[1])
        ).execute(),
        "decorator <decorator>": Text("@") + Alternating("decorator"),
        "try except [<exception>] [error] [<as>]": Text("try: ")
        + Key("enter:2, backspace")
        + Text("except%(exception)s%(as)s:")
        + Key("up"),
        "raise [<exception>] [error]": Text("raise%(exception)s"),
        "error <exception> [error]": Text("%(exception)s"),
        "comment [<text>]": lambda text: Text("# %s" % text.capitalize()).execute(),
        "insert line break": Text("#" + ("-" * 48)),
        "insert to do": Text("# TODO: "),
        # ------------------------------------------------
        "cheat sheet <module>": lambda module: Popen(
            ["SumatraPDF", "C:/Users/Mike/Documents/cheatsheets/python/%s.pdf" % module]
        ),
        "help <docs>": lambda docs: utilities.browser_open(docs),
        "help that": Function(
            utilities.browser_search, url="https://www.google.com/search?q=python+%s"
        ),
    },
    [
        Choice("as", {"as": " as "}, ""),
        Choice("right", {"right": "r", "eye": "i"}, ""),
        Choice("module", BINDINGS["cheatsheets"]),
        Choice("decorator", BINDINGS["decorators"]),
        Choice("template", BINDINGS["templates"]),
        Choice("umeth", BINDINGS["unary_methods"]),
        Choice("bmeth", BINDINGS["binary_methods"]),
        Choice("mmeth", BINDINGS["misc_methods"]),
        Choice("exception", BINDINGS["exceptions"], ""),
        Choice("fun", BINDINGS["functions"]),
        Choice("docs", BINDINGS["docs"]),
    ],
    ccr=False,
)

Breathe.add_commands(
    AppContext(title=BINDINGS["title_contexts"]),
    {
        "<command>": Alternating("command"),
        "fun <fun>": ContextAction(
            Read("previous")
            + Text("%(fun)s(%(previous)s)")
            + Function(lambda previous: Key("left" if not previous else "").execute()),
            [(AppContext(title="jupyter"), Text("%(fun)s()") + Key("left"))],
        ),
        "meth <fun>": Text(".%(fun)s()") + Key("left"),
        "from typing import <types>": Text("from typing import %(types)s"),
        "type <types>": Text("%(types)s"),
        "type is <types>": Text(": %(types)s"),
        "produces [<types>]": Key("end:2, left") + Text(" -> %(types)s"),
        "method": Text("def (self):") + Key("left:7"),
        "list comp": Text("[ for  in i]") + Key("left:11"),
        # ------------------------------------------------
        "method [<under>] <snaketext>": Text("def %(under)s%(snaketext)s(self):")
        + Key("left:2"),
        "function <snaketext>": Text("def %(snaketext)s():") + Key("left:2"),
        "selfie [<under>] [<snaketext>]": Text("self.%(under)s%(snaketext)s"),
        "pointer [<under>] [<snaketext>]": Text(".%(under)s%(snaketext)s"),
        "classy [<classtext>]": Text("class %(classtext)s:") + Key("left"),
        "<formatting> <text>": lambda formatting, text: textformat.master_format_text(
            formatting[0], formatting[1], text
        ),
    },
    [
        Dictation("snaketext", "").lower().replace(" ", "_"),
        Dictation("classtext", "").title().replace(" ", ""),
        Choice("under", "_", ""),
        Choice("formatting", {"(snaky | sneaky)": [5, 3], "(singer | title)": [2, 1]}),
        Choice("fun", BINDINGS["functions"]),
        Choice("command", BINDINGS["commands"]),
        Choice("types", BINDINGS["types"], ""),
    ],
)

# ------------------------------------------------

VOICE_DEV = utilities.load_toml_relative("config/python_caster.toml")

Breathe.add_commands(
    AppContext(title=["caster", "merger"]) & AppContext(title=".py"),
    {
        BINDINGS["function_prefix"] + " <cfun>": Text("%(cfun)s()") + Key("left"),
        "<cmisc>": Alternating("cmisc"),
    },
    [Choice("cfun", VOICE_DEV["functions"]), Choice("cmisc", VOICE_DEV["misc"])],
)

# ------------------------------------------------

Breathe.add_commands(
    AppContext(title="jupyterlab"),
    {
        "next pane [<n>]": Key("cs-rbracket:%(n)s"),
        "previous pane [<n>]": Key("cs-lbracket:%(n)s"),
        "replace": Key("cs-r"),
        "toggle cyber": Key("c-b"),
        "(insert | new) cell": Key("a-enter"),
        "run cell": Key("c-enter"),
        "(next cell | necker) [<n>]": Key("s-enter:%(n)s"),
        "split cell": Key("cs-minus"),
        "[insert] cell above": Key("escape, a"),
        "[insert] cell below": Key("escape, b"),
        "merge below": Key("escape, M"),
        "merge above": Key("escape, s-up, M"),
        "toggle line numbers": Key("escape, L"),
        "delete cell [<n>]": Key("escape, d, d") * Repeat("n"),
        "select all": Key("c-a"),
        "indent [<n>]": Key("c-rbracket:%(n)s"),
        "outdent [<n>]": Key("c-lbracket:%(n)s"),
        "comment line": Key("c-slash"),
        "command pallette": Key("cs-p"),
    },
    ccr=False,
)
