from dragonfly import Playback, Clipboard, ActionBase

from .actions import Key, Text, SlowKey, SlowText
from my_commands.utils import utilities
import re
from six import string_types

# Alternate between executing as text and executing as keys
# "<example>": Alternating("example")
class Alternating(ActionBase):
    def __init__(self, command=""):
        ActionBase.__init__(self)
        self.command = command

    def _execute(self, data=None):
        command = data[self.command]
        if isinstance(command, string_types) or isinstance(command, int):
            Text(str(command)).execute()
        elif type(command) in [list, tuple] and len(command) == 1:
            (Text(command[0]) + Key("left")).execute()
        else:
            for i in range(len(command)):
                if i%2==0:
                    Text(command[i]).execute()
                else:
                    Key(command[i]).execute()

class SlowAlternating(ActionBase):
    def __init__(self, command=""):
        ActionBase.__init__(self)
        self.command = command

    def _execute(self, data=None):
        command = data[self.command]
        if isinstance(command, string_types) or isinstance(command, int):
            SlowText(str(command)).execute()
        elif type(command) in [list, tuple]:
            for i in range(len(command)):
                if i%2==0:
                    SlowText(command[i]).execute()
                else:
                    SlowKey(command[i]).execute()

def template(template):
    utilities.paste_string(template)

# def python_setters():
#     Store().execute()
#     text = re.search(r"self,(.*?)\)", Retrieve.text())
#     args = text.group(1).split(",")
#     args2 = [x.split("=")[0].strip() for x in args]
#     Key("end, enter").execute()
#     for arg in args2:
#         Text("self.%s = %s\n" % (arg, arg)).execute()

def markdown_link():
    text = Clipboard.get_system_text()
    print(text)
    if len(text)>4 and text.startswith("http"):
        Text("[]()").execute()
        Key("left, c-v, left:" + str(len(text) + 2)).execute()
    else:
        (Text("[]()") + Key("left")).execute()
