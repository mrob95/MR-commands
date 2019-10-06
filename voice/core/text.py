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

