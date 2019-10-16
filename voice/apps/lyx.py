from voice.imports import *

BINDINGS = utilities.load_toml_relative("config/lyx.toml")
CORE = utilities.load_toml_relative("config/core.toml")


def greek(big, greek_letter):
    if big:
        greek_letter = greek_letter.title()
    Text("\\" + greek_letter + " ").execute()


def matrix(rows, cols):
    Text("\\" + BINDINGS["matrix_style"] + " ").execute()
    Key("a-m, w, i, " * (rows - 1) + "a-m, c, i, " * (cols - 1)).execute()


Breathe.add_commands(
    AppContext(executable="lyx"),
    {
        "<control>": Key("%(control)s"),
        "<control_repeat> [<n>]": Key("%(control_repeat)s") * Repeat("n"),
    },
    [
        Choice("control", BINDINGS["control"]),
        Choice("control_repeat", BINDINGS["control_repeat"]),
    ],
    ccr=False,
)

Breathe.add_commands(
    AppContext(executable="lyx"),
    {
        "<numbers>": Text("%(numbers)s"),
        BINDINGS["symbol1_prefix"] + " <symbol1>": Text("\\%(symbol1)s "),
        BINDINGS["symbol2_prefix"] + " <symbol2>": Text("\\%(symbol2)s "),
        BINDINGS["accent_prefix"] + " <accent>": Key("a-m, %(accent)s"),
        BINDINGS["text_prefix"] + " <text_modes>": Text("\\%(text_modes)s "),
        BINDINGS["greek_prefix"] + " [<big>] <greek_letter>": Function(greek),
        "<misc_lyx_keys>": Key("%(misc_lyx_keys)s"),
        "<command>": Alternating("command"),
        "matrix <rows> by <cols>": Function(matrix),
        "<numbers> <denominator>": Key(
            "a-m, f, %(numbers)s, down, %(denominator)s, right"
        ),
        # "configure "
        # + BINDINGS["pronunciation"]: Function(
        #     utilities.load_config, config_name="lyx.toml"
        # ),
    },
    [
        IntegerRef("rows", 1, BINDINGS["max_matrix_size"]),
        IntegerRef("cols", 1, BINDINGS["max_matrix_size"]),
        IntegerRef("numbers", 0, CORE["numbers_max"]),
        Boolean("big", CORE["capitals_prefix"]),
        Choice("greek_letter", BINDINGS["greek_letters"]),
        Choice("symbol1", BINDINGS["tex_symbols1"]),
        Choice("symbol2", BINDINGS["tex_symbols2"]),
        Choice("accent", BINDINGS["accents"]),
        Choice("text_modes", BINDINGS["text_modes"]),
        Choice("misc_lyx_keys", BINDINGS["misc_lyx_keys"]),
        Choice("command", BINDINGS["misc_lyx_commands"]),
        Choice("denominator", BINDINGS["denominators"]),
    ],
)

Breathe.add_commands(
    AppContext(executable="lyx"),
    {
        "[<before>] integral from <sequence1> to <sequence2>": ExecNested("before")
        + Text("\\int _")
        + ExecNested("sequence1")
        + Key("right, caret")
        + ExecNested("sequence2")
        + Key("right"),
        "[<before>] definite from <sequence1> to <sequence2>": ExecNested("before")
        + Key("a-m, lbracket, right, underscore")
        + ExecNested("sequence1")
        + Key("right, caret")
        + ExecNested("sequence2")
        + Key("right, left:2"),
        "[<before>] differential <sequence1> by <sequence2>": ExecNested("before")
        + Key("a-m, f, d")
        + ExecNested("sequence1")
        + Key("down, d")
        + ExecNested("sequence2")
        + Key("right"),
        "[<before>] sum from <sequence1> to <sequence2>": ExecNested("before")
        + Text("\\stackrelthree ")
        + Key("down")
        + Text("\\sum ")
        + Key("down")
        + ExecNested("sequence1")
        + Key("up:2")
        + ExecNested("sequence2")
        + Key("right"),
        "[<before>] limit from <sequence1> to <sequence2>": ExecNested("before")
        + Text("\\underset \\lim ")
        + Key("down")
        + ExecNested("sequence1")
        + Text("\\rightarrow ")
        + ExecNested("sequence2")
        + Key("right"),
        "[<before>] argument that <minmax> <sequence1>": ExecNested("before")
        + Text("\\underset \\arg \\%(minmax)s ")
        + Key("down")
        + ExecNested("sequence1")
        + Key("right"),
        "[<before>] <minmax> by <sequence1>": ExecNested("before")
        + Text("\\underset \\%(minmax)s ")
        + Key("down")
        + ExecNested("sequence1")
        + Key("right"),
        "[<before>] <script1> <singleton1> [<after>]": ExecNested("before")
        + Key("%(script1)s")
        + ExecNested("singleton1")
        + Key("right")
        + ExecNested("after"),
        "[<before>] <script1> <singleton1> <script2> <singleton2> [<after>]": ExecNested(
            "before"
        )
        + Key("%(script1)s")
        + ExecNested("singleton1")
        + Key("right, %(script2)s")
        + ExecNested("singleton2")
        + Key("right")
        + ExecNested("after"),
    },
    extras=[
        Choice(
            "minmax", {"(minimum | minimises)": "min", "(maximum | maximises)": "max"}
        ),
        Choice("script1", {"sub": "_", "super": "^"}),
        Choice("script2", {"sub": "_", "super": "^"}),
        Nested("before", 8),
        Nested("after", 8),
        Nested("singleton1", 1),
        Nested("singleton2", 1),
        Nested("sequence1", 4),
        Nested("sequence2", 4),
    ],
    nested=True,
)

