from my_commands.imports import *

Breathe.add_commands(
    AppContext(title="photoshop"),
    {
        "new (file | pane)": Key("c-n"),
        "open file": Key("c-o"),
        "close file": Key("c-w"),
        "transform": Key("c-t"),
        "deselect": Key("c-d"),
        "new layer": Key("cas-n"),
        "open folder": Key("cs-o"),
        "save as": Key("cs-s"),
        "step backwards [<n>]": Key("ca-z:%(n)s"),
        "step forwards [<n>]": Key("cs-z:%(n)s"),
        "brush size down [<n>]": Key("lbracket:%(n)s"),
        "brush size up [<n>]": Key("rbracket:%(n)s"),
    },
)
