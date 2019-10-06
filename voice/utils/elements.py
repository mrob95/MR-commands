from dragonfly import Choice as ChoiceBase
from dragonfly import Dictation as DictationBase
from dragonfly import Compound as CompoundBase

def Boolean(name, spec=None):
    if not spec: spec = name
    return CompoundBase(spec=spec, name=name, value=True, default=False)

def Choice(name, choices, default=None, extras=None):
    if isinstance(choices, str):
        choices = {name: choices}
    return ChoiceBase(name, choices, extras, default)

def Dictation(name=None, default=None):
    return DictationBase(name=name, default=default)