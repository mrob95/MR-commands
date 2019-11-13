from voice.imports import *

Breathe.add_commands(
    None,
    {
        "window <direction> [<direction2>]": Key(
            "win:down, %(direction)s/15, %(direction2)s, win:up"
        ),
        "minimize": lambda: Window.get_foreground().minimize(),
        "maximize": lambda: Window.get_foreground().maximize(),
        "close window": Key("a-f4"),
        "show work [spaces]": Key("w-tab"),
        "(create | new) work [space]": Key("wc-d"),
        "close work space": Key("wc-f4"),
        "next work [space] [<n>]": Key("wc-right") * Repeat("n"),
        "(previous | prior) work [space] [<n>]": Key("wc-left") * Repeat("n"),
        "go work [space] <n>": Function(lambda n: workspace.go_to_n(n)),
        "send work [space] <n>": Function(lambda n: workspace.move_current_to_n(n)),
        "move work [space] <n>": Function(
            lambda n: workspace.move_current_to_n(n, True)
        ),
        "move everything to work [space] <n>": Function(workspace.move_desktop_to),
        "send work [space] new": Function(workspace.move_current_to_new, follow=False),
        "move work [space] new": Function(workspace.move_current_to_new, follow=True),
        "close all work [spaces]": Function(workspace.close_all),
        "show window information": Function(utilities.windowinfo),
    },
    [
        Choice(
            "direction2",
            {"lease": "left", "ross": "right", "sauce": "up", "dunce": "down"},
            "",
        )
    ],
    ccr=False,
)
