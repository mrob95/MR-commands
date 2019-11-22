from my_commands.imports import *

Breathe.add_global_extras(
    ShortIntegerRef("n", 1, 20, 1),
    Dictation("text", ""),
    Choice(
        "direction",
        {"lease": "left", "ross": "right", "sauce": "up", "dunce": "down"},
        "left",
    ),
)
