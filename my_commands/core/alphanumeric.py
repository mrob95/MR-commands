from my_commands.imports import *

CORE = utilities.load_toml_relative("config/core.toml")

Breathe.add_commands(
    None,
    {
        "[<big>] <letter>": lambda big, letter: Key(
            letter.upper() if big else letter
        ).execute(),
        "numb <num_seq>": Text("%(num_seq)s"),
    },
    extras=[
        Boolean("big"),
        Choice("letter", CORE["letters_alt"]),
        Modifier(
            Repetition(IntegerRef("", 0, 10), min=1, max=5, name="num_seq"),
            lambda r: "".join(map(str, r)),
        ),
    ],
)
