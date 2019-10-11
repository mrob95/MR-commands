from dragonfly import Mouse, Pause, ActionBase, ActionError, Alternative, Compound, RuleWrap
from dragonfly import Text as TextBase, Key as KeyBase, Clipboard

import time
import re
from six import string_types

class Text(TextBase):
    _pause_default = 0.002

Key = KeyBase

class SlowText(TextBase):
    _pause_default = 0.01

class SlowKey(KeyBase):
    interval_default = 1.0

'''
Stores the currently highlighted text in a temporary variable,
to be Retrieved after some other action. If no text was
highlighted, an empty string will be stored.
Sample usage:
"find that": Store() + Key("c-f") + Retrieve() + Key("enter")

In order to enable use with web URLs, Store() takes a string,
space, which will replace all space characters, and a bool,
remove_cr, which if true will remove any newlines in the
selection, to avoid them triggering the request early.
Sample usage:
"wikipedia that":
    Store(space="+", remove_cr=True) + Key("c-t") +
    Text("https://en.wikipedia.org/w/index.php?search=") +
    Retrieve() + Key("enter")

There are cases where you may want the same function to do
different things depending on whether or not text was highlighted.
The action_if_no_text and action_if_text arguments to Retrieve()
are calls to Key() and allow this.
For example, you may want to finish inside a set of brackets
if no text was highlighted, but outside if there was text.
Sample usage:
"insert bold text":
    Store() + Text("\\textbf{}") + Key("left") +
    Retrieve(action_if_text="right")
'''
# class Store(ActionBase):
#     def __init__(self, space=" ", remove_cr=False, same_is_okay=True):
#         ActionBase.__init__(self)
#         self.space = space
#         self.remove_cr = remove_cr
#         self.same_is_okay = same_is_okay

#     def _execute(self, data=None):
#         orig = utilities.read_selected(self.same_is_okay)
#         text = orig.replace(" ", self.space) if orig else ""
#         control.nexus().temp = text.replace("\n", "") if self.remove_cr else text
#         return True
class Read(ActionBase):
    def __init__(self, name=None, remove_cr=False, same_is_okay=True):
        ActionBase.__init__(self)
        self.name = name
        self.remove_cr = remove_cr
        self.same_is_okay = same_is_okay

    def read_selected(self, same_is_okay=False, wait=5):
        key_wait = 0.01 * wait
        time.sleep(key_wait)
        cb = Clipboard(from_system=True)
        temporary = None
        prior_content = None
        try:
            prior_content = Clipboard.get_system_text()
            Clipboard.set_system_text("")
            Key("c-c").execute()
            time.sleep(key_wait)
            temporary = Clipboard.get_system_text()
            cb.copy_to_system()
        except Exception:
            return None
        return temporary

    def _execute(self, data=None):
        text = self.read_selected(self.same_is_okay)
        if data:
            data[self.name] = text
        return True


# class Retrieve(ActionBase):
#     def __init__(self, action_if_no_text="", action_if_text=""):
#         ActionBase.__init__(self)
#         self.action_if_no_text = action_if_no_text
#         self.action_if_text = action_if_text

#     @classmethod
#     def text(cls):
#         return control.nexus().temp

#     def _execute(self, data=None):
#         output = control.nexus().temp
#         Text(output).execute()
#         if output:
#             Key(self.action_if_text).execute()
#         else:
#             Key(self.action_if_no_text).execute()
#         return True
