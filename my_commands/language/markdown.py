from my_commands.imports import *

BINDINGS = utilities.load_toml_relative("config/markdown.toml")

Breathe.add_commands(
    AppContext(title=BINDINGS["title_contexts"]),
    {
        "heading [<num>] [<capitalised_text>]": Text("#") * Repeat("num")
        + Text(" %(capitalised_text)s"),
        "subheading [<capitalised_text>]": Text("## %(capitalised_text)s"),
        BINDINGS["insert_prefix"] + " <element>": Key("%(element)s"),
        BINDINGS["insert_prefix"] + " <command>": Alternating("command"),
        BINDINGS["output_prefix"] + " <output>": Text("%(output)s"),
        BINDINGS["option_prefix"] + " <option>": Text("%(option)s"),
        "remark <remarks>": Alternating("remarks"),
        "table row <n>": Function(lambda n: Text("|" * (n - 1)).execute())
        + Key("home"),
        "table (break | split) <n>": Function(
            lambda n: Text("---|" * (n - 1) + "---").execute()
        )
        + Key("enter"),
        "insert link": Function(execution.markdown_link),
        "insert [<language>] code block": Text("```%(language)s```")
        + Key("left:3, enter:2, up"),
    },
    [
        Modifier(Dictation("capitalised_text", ""), lambda s: s.capitalize()),
        IntegerRef("num", 1, 7, 1),
        Choice("element", BINDINGS["elements"]),
        Choice("output", BINDINGS["outputs"]),
        Choice("option", BINDINGS["options"]),
        Choice("remarks", BINDINGS["remarks"]),
        Choice("language", BINDINGS["languages"], ""),
        Choice("command", BINDINGS["alternating"]),
    ],
)
