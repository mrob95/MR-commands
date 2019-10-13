from voice.imports import *

CORE = utilities.load_toml_relative("config/core.toml")
PERSONAL = utilities.load_toml_relative("config/personal.toml")

Breathe.add_commands(
    None,
    {
        # "<search> search that": lambda search: utilities.browser_search(url=search),
        "<search> search that": Read("web") + Function(lambda web, search: utilities.browser_search(text=web, url=search)),
        "<search> search <text>": lambda search, text: utilities.browser_search(
            text, url=search
        ),
        "tiny URL that": utilities.tinyurl,
        "open diary": utilities.diary,
        "close all notepads": utilities.kill_notepad,
        "open terminal": lambda: Popen("wt.exe"),
        "open bash": lambda: utilities.terminal("C:/Users/Mike/Documents"),
        # -----------------------------------------------
        # Clipboard
        "paste as text": lambda: Text(Clipboard.get_system_text()).execute(),
        "take screenshot": Key("ws-s"),
        "save clipboard image": Function(utilities.save_clipboard_image),
        "fix clipboard path": lambda: Clipboard.set_system_text(
            Clipboard.get_system_text().replace("\\", "/")
        ),
    },
    [Choice("search", CORE["search"])],
    ccr=False,
)

Breathe.add_commands(
    None, {"<personal>": Text("%(personal)s")}, [Choice("personal", PERSONAL)]
)

if get_engine()._name == "natlink":
    Breathe.add_commands(None, {"reboot dragon": Function(utilities.reboot)}, ccr=False)
