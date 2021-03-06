from my_commands.imports import *

CORE = utilities.load_toml_relative("config/core.toml")

Breathe.add_commands(
    None,
    {
        "say <text> [brunt]": Function(
            textformat.master_format_text, capitalisation=0, spacing=0
        ),
        "(<capitalisation> <spacing> | <capitalisation> | <spacing>) (bow|bowel) <text>":
            Function(textformat.master_format_text),

        "word <word>": Text("%(word)s"),
    },
    [
        Choice("capitalisation", CORE["capitalisation"], 0),
        Choice("spacing", CORE["spacing"], 0),
        SingleWord("word"),
    ]
)


# Breathe.add_commands(
#     None,
#     {
#         "<sequence_of_commands>": Exec("sequence_of_commands"),
#         "[<sequence_of_commands>] (<capitalisation> <spacing> | <capitalisation> | <spacing>) (bow|bowel) <text>": Exec(
#             "sequence_of_commands"
#         )
#         + Function(textformat.master_format_text),
#         # "<sequence_of_commands> [and repeat that <n> times]": Exec("sequence_of_commands")
#         # * Repeat("n"),
#     },
#     [
#         CommandsRef("sequence_of_commands", 16),
#         Choice("capitalisation", CORE["capitalisation"], 0),
#         Choice("spacing", CORE["spacing"], 0),
#     ],
#     top_level=True,
# )
