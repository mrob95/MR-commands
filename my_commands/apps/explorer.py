from my_commands.imports import *

BRING = utilities.load_toml_relative("config/bringme.toml")
CORE = utilities.load_toml_relative("config/core.toml")


def current_directory():
    title = Window.get_foreground().title
    remap = {
        "Downloads": "C:\\Users\\Mike\\Downloads",
        "Documents": "C:\\Users\\Mike\\Documents",
        "Pictures": "C:\\Users\\Mike\\Pictures",
        "Mike": "C:\\Users\\Mike",
    }
    if title in remap.keys():
        title = remap[title]
    return title


Breathe.add_commands(
    AppContext(executable="explorer"),
    {
        "address bar": Key("a-d"),
        "new folder": Key("cs-n"),
        "new file": Key("a-f, w, t"),
        "[(show | file | folder)] properties": Key("a-enter"),
        "go up [<n>]": Key("a-up:%(n)s"),
        "go back [<n>]": Key("a-left:%(n)s"),
        "go forward [<n>]": Key("a-right:%(n)s"),
        "go <folder>": Key("a-d/10") + Text("%(folder)s") + Key("enter"),
        "follow <letter_rep>": Text("%(letter_rep)s") + Key("enter"),
        # "terminal here": lambda: utilities.windows_terminal("{0caa0dad-35be-5f56-a8ff-afceeeaa6101}", current_directory().replace("\\", "/")),
        "terminal here": Function(
            lambda: utilities.terminal(current_directory().replace("\\", "/"))
        ),
        "new window": Function(lambda: Popen(["explorer", current_directory()])),
        "sublime here": Function(
            lambda: Popen(["subl", "-n", current_directory().replace("\\", "/")])
        ),
        "[VS] code here": Function(
            lambda: Popen(["code", current_directory().replace("\\", "/")])
        ),
    },
    [
        Choice("folder", BRING["folder"]),
        Modifier(
            Repetition(Choice("", CORE["letters_alt"]), 1, 5, "letter_rep"),
            lambda r: "".join(r),
        ),
    ],
)

Breathe.add_commands(
    AppContext(title=["save", "open", "select", "choose directory"]),
    {
        "go up [<n>]": Key("a-up:%(n)s"),
        "go back [<n>]": Key("a-left:%(n)s"),
        "go forward [<n>]": Key("a-right:%(n)s"),
        "(files | file list)": Key("a-d, f6:3"),
        "navigation [pane]": Key("a-d, f6:2"),
        "file name [<text>]": Key("a-d, f6:5") + Text("%(text)s"),
        "go <folder>": Key("a-d/10") + Text("%(folder)s") + Key("enter/10, tab:4"),
        "dot <ext>": Text(".%(ext)s"),
        "follow <letter_rep>": Text("%(letter_rep)s") + Key("enter"),
    },
    [
        Choice("folder", BRING["folder"]),
        Modifier(
            Repetition(Choice("", CORE["letters_alt"]), 1, 5, "letter_rep"),
            lambda r: "".join(r),
        ),
        Choice(
            "ext",
            {
                "batch": "bat",
                "(hyper | HTML)": "html",
                "git ignore": "gitignore",
                "mark [down]": "md",
                "PDF": "pdf",
                "(pie | python)": "py",
                "R": "R",
                "R mark [down]": "Rmd",
                "shell": "sh",
                "tech": "tex",
                "text": "txt",
                "tommel": "toml",
                "yammel": "yml",
            },
        ),
    ],
)
