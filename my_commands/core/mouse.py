from my_commands.imports import *

Breathe.add_commands(
    None,
    {
        "squat": Mouse("left:down"),
        "bench": ContextAction(
            Mouse("left:up"),
            [
                (
                    AppContext("ShellExperienceHost.exe"),
                    Mouse("left:up/100") + Function(utilities.save_clipboard_image),
                )
            ],
        ),
        "(shift click | shifty)": Key("shift:down") + Mouse("left") + Key("shift:up"),
        "kick": Mouse("left"),
        "kick double": Mouse("left")*Repeat(2),
        "shift right click": Key("shift:down") + Mouse("right") + Key("shift:up"),
        "colic": Key("control:down") + Mouse("left") + Key("control:up"),
        "millick": Mouse("middle"),
    }
)
