from dragonfly import Mouse, Pause, ActionBase, ActionError, Alternative, Compound, RuleWrap
from dragonfly import Text as TextBase, Key as KeyBase, Clipboard

import time

class Text(TextBase):
    _pause_default = 0.002

Key = KeyBase

class SlowText(TextBase):
    _pause_default = 0.01

class SlowKey(KeyBase):
    interval_default = 1.0

class Read(ActionBase):
    def __init__(self, name=None, remove_cr=False, same_is_okay=True):
        ActionBase.__init__(self)
        self.name = name
        self.remove_cr = remove_cr
        self.same_is_okay = same_is_okay

    def read_selected(self, same_is_okay=False, wait=5):
        key_wait = 0.01 * wait
        cb = Clipboard(from_system=True)
        time.sleep(key_wait)
        temporary = None
        # prior_content = None
        try:
            # prior_content = Clipboard.get_system_text()
            Clipboard.set_system_text("")
            Key("c-c").execute()
            time.sleep(key_wait)
            temporary = Clipboard.get_system_text()
            cb.copy_to_system()
        except Exception:
            return ""
        return temporary

    def _execute(self, data=None):
        text = self.read_selected(self.same_is_okay)
        if data:
            data[self.name] = text
        return True