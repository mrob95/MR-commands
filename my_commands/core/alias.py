from my_commands.imports import *

# aliases = DictList("aliases", utilities.load_toml_relative("config/aliases.toml"))
aliases = DictList("aliases")


def add_alias(spec):
    text = utilities.read_selected(True)
    if text and spec:
        aliases[str(spec)] = text.replace("\r\n", "\n")
        # utilities.save_toml_relative(dict(aliases), "config/aliases.toml")

def delete_aliases():
    aliases.clear()
    # utilities.save_toml_relative(dict(aliases), "config/aliases.toml")

def delete_alias(del_alias):
    del aliases[del_alias]
    # utilities.save_toml_relative(dict(aliases), "config/aliases.toml")

Breathe.add_commands(
    None,
    {
        "alias <text>": lambda text: add_alias(text),
        "delete all aliases": delete_aliases,
    },
    ccr=False
)

Breathe.add_commands(
    None,
    {
        "delete alias <del_alias>": delete_alias,
        "<alias>": Text("%(alias)s")
    },
    [
        DictListRef("alias", aliases),
        ListRef("del_alias", aliases),
    ]
)
