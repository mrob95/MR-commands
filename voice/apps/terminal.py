from voice.imports import *

BINDINGS = utilities.load_toml_relative("config/terminal.toml")
CORE = utilities.load_toml_relative("config/core.toml")


def clip_repo():
    clip = Clipboard.get_system_text()
    if clip.startswith("https://github.com"):
        if clip.endswith("/"):
            clip = clip[:-1]
        Text(clip).execute()
        if not clip.endswith(".git"):
            Text(".git").execute()


Breathe.add_commands(
    AppContext(executable=BINDINGS["executable_contexts"]),
    {
        "option <alph>": Text(" -%(alph)s "),
        "<command>": Alternating("command"),
        #------------------------------------------------
        "git <git_command>": Text("git ") + Alternating("git_command"),
        "git <dictcommand> <snake_text>": Text("git %(dictcommand)s %(snake_text)s"),
        "git clone": Text("git clone ") + Function(clip_repo) + Text(" "),
        "git remote add": Text("git remote add  ")
        + Function(clip_repo)
        + Key("home, right:15"),
        #------------------------------------------------
        "run T mux": Text("tmux "),
        "[T] mux <tmux_command>": Key("c-b, %(tmux_command)s"),
        "ops <ops_command>": Text("%(ops_command)s"),
        #------------------------------------------------
        "open link": Key("c-insert")
        + Function(lambda: utilities.browser_open(Clipboard.get_system_text())),
    },
    [
        Dictation("snake_text").replace(" ", "_"),
        Choice("dictcommand", {"check out": "checkout", "new branch": "checkout -b"}),
        Modifier(
            Repetition(Choice("", CORE["letters_alt"]), 1, 4, "alph"),
            lambda r: "".join(r),
        ),
        Choice("command", BINDINGS["commands"]),
        Choice("git_command", BINDINGS["git_commands"]),
        Choice("tmux_command", BINDINGS["tmux_commands"]),
        Choice("ops_command", BINDINGS["ops_class"]),
    ],
)

