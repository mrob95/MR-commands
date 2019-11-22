from my_commands.imports import *

CORE = utilities.load_toml_relative("config/core.toml")

Breathe.add_commands(
    None,
    {
        "[<long>] <punctuation>": lambda long, punctuation: Key(
            "space, %s, space" % punctuation if long else punctuation
        ).execute(),
        "[<long>] <punctuation2> [<equal>]": lambda long, punctuation2, equal: Key(
            ("space, " if long else "")
            + punctuation2
            + (", =, " if equal else "")
            + (", space" if long else "")
        ).execute(),
    },
    [
        Boolean("long"),
        Boolean("equal"),
        Choice("punctuation", CORE["punctuation"]),
        Choice("punctuation2", CORE["punctuation2"]),
    ],
)
