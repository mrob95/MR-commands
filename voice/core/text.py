from voice.imports import *

CORE = utilities.load_toml_relative("config/core.toml")

Breathe.add_commands(
    None,
    {
        "say <text> [brunt]": Function(
            textformat.master_format_text, capitalisation=0, spacing=0
        ),
        "(<capitalisation> <spacing> | <capitalisation> | <spacing>) (bow|bowel) <text> [brunt]": textformat.master_format_text,
    },
    [
        Choice("capitalisation", CORE["capitalisation"], 0),
        Choice("spacing", CORE["spacing"], 0),
    ],
)


Breathe.add_commands(
    None,
    {
        "[<sequence_of_commands>] dictate <text>": Exec("sequence_of_commands")
        + Text("%(text)s"),
        "<sequence_of_commands> [and repeat that <n> times]": Exec("sequence_of_commands")
        * Repeat("n"),
    },
    [CommandsRef("sequence_of_commands", 16)],
    top_level=True,
)
