from my_commands.imports import *

Breathe.add_commands(
    AppContext(title="kindle for PC"),
    {
        "library": Key("ca-l"),
        "(show | hide) notebook": Key("c-b"),
        "(search | find)": Key("c-f"),
        "(synchronise | refresh)": Key("f5"),
    },
)
