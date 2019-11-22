from my_commands.imports import *

CORE = utilities.load_toml_relative("config/core.toml")

def playback_history(n=1):
    print(breathe_repetition_history)
    if len(breathe_repetition_history) <= n:
        raise ActionError("Not enough items in history: have %s, need %s", len(breathe_repetition_history), n)
    Playback([(sequence, 0) for sequence in breathe_repetition_history[-n:]]).execute()

Breathe.add_commands(
    None,
    {
        "say <text> [brunt]": Function(
            textformat.master_format_text, capitalisation=0, spacing=0
        ),
        "(<capitalisation> <spacing> | <capitalisation> | <spacing>) (bow|bowel) <text>":
            Function(textformat.master_format_text),

        "repeat last [<n>]": playback_history,
    },
    [
        Choice("capitalisation", CORE["capitalisation"], 0),
        Choice("spacing", CORE["spacing"], 0),
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
