from my_commands.imports import *

CORE = utilities.load_toml_relative("config/core.toml")

# Don't paste newlines into terminals
def sanitise_clipboard():
    Clipboard.set_system_text(Clipboard.get_system_text().replace("\n", ""))
    Pause("10")

Breathe.add_commands(
    None,
    {
        "(<direction> | <modifier> [<direction>]) [(<n> | <extreme>)]": Function(
            navigation.text_nav
        ),
        "<key> [<n>]": Key("%(key)s") * Repeat("n"),
        "tabby [<tabdir>] [<n>]": Key("%(tabdir)s" + "tab") * Repeat("n"),
        "(splat | spat) [<splatdir>] [(<n> | <extreme>)]": ContextAction(
            Function(navigation.splat),
            [(AppContext("notepad"), Function(navigation.splat, manual=True))],
        ),
        "check [<n>]": ContextAction(
            Key("c-enter:%(n)s"),
            [
                (
                    AppContext(title=["notepad", "scientific notebook", "jupyter"]),
                    Key("end, enter:%(n)s"),
                )
            ],
        ),
        "<misc_core_keys>": Key("%(misc_core_keys)s"),
        # ------------------------------------------------
        "stoosh": ContextAction(
            Key("c-c"),
            [
                (
                    AppContext(
                        executable=[
                            "\\sh.exe",
                            "\\bash.exe",
                            "\\cmd.exe",
                            "\\mintty.exe",
                        ]
                    ),
                    Key("c-insert"),
                ),
                (AppContext(executable="windowsterminal.exe"), Key("cs-c")),
            ],
        ),
        "cutter": Key("c-x"),
        "duple [<n>]": ContextAction(
            Function(navigation.duple),
            [
                (AppContext(title="Sublime Text"), Key("cs-d:%(n)s")),
                (AppContext("code.exe"), Key("sa-down:%(n)s")),
                (AppContext(title="jupyter"), Function(navigation.duple, esc=False)),
                (AppContext(title="pycharm"), Key("c-d:%(n)s")),
                (
                    AppContext(
                        executable=[
                            "\\sh.exe",
                            "\\bash.exe",
                            "\\cmd.exe",
                            "\\mintty.exe",
                            "windowsterminal",
                        ]
                    ),
                    Key(""),
                ),
            ],
        ),
        "(spark | sparky)": ContextAction(
            Key("c-v"),
            [
                (
                    AppContext(
                        executable=[
                            "\\sh.exe",
                            "\\bash.exe",
                            "\\cmd.exe",
                            "\\mintty.exe",
                        ]
                    ),
                    Function(sanitise_clipboard) + Key("s-insert"),
                ),
                (AppContext("windowsterminal.exe"), Key("cs-v")),
            ],
        ),
        "hug <enclosure>": navigation.enclose_selected,
    },
    [
        Boolean("extreme", "wally"),
        Choice("modifier", CORE["modifiers"], ""),
        Choice("splatdir", {"ross": "right"}, "left"),
        Choice("tabdir", {"lease": "s-"}, ""),
        Choice("key", CORE["keys"]),
        Choice("misc_core_keys", CORE["misc_core_keys"]),
        Choice("enclosure", CORE["enclosures"]),
    ],
)

# ------------------------------------------------

Breathe.add_commands(
    None,
    {
        "undo [<n>]": Key("c-z:%(n)s"),
        "redo [<n>]": Key("c-y:%(n)s"),
        "save [file]": Key("c-s"),
        "context menu": Key("s-f10"),
        "volume up [<n>]": Key("volumeup/5:%(n)d"),
        "volume down [<n>]": Key("volumedown/5:%(n)d"),
        "volume (mute|unmute)": Key("volumemute"),
        "music next [<n>]": Key("tracknext/5:%(n)d"),
        "music previous [<n>]": Key("trackprev/5:%(n)d"),
        "music (pause|play)": Key("playpause"),
        "zoom in [<n>]": Key("c-equal:%(n)s"),
        "zoom out [<n>]": Key("c-minus:%(n)s"),
    },
    ccr=False,
)
