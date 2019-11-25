from dragonfly import Choice as ChoiceBase
from dragonfly import Dictation as DictationBase
from dragonfly import Compound as CompoundBase
from dragonfly import RuleRef, Rule

def Boolean(name, spec=None):
    if not spec: spec = name
    return CompoundBase(spec=spec, name=name, value=True, default=False)

def Choice(name, choices, default=None, extras=None):
    if isinstance(choices, str):
        choices = {name: choices}
    return ChoiceBase(name, choices, extras, default)

def Dictation(name=None, default=None):
    return DictationBase(name=name, default=default)

class DgnImported(RuleRef):
    """
        Base class that implements an imported rule and takes care of
        decoding recognitions accordingly.

    """

    def __init__(self, name=None, imported_name=None, default=None):
        if not imported_name:
            imported_name = name
        self.imported_name = imported_name
        self.imported_rule = Rule(self.imported_name, imported=True)
        RuleRef.__init__(self, self.imported_rule, name, default=default)

    def decode(self, state):
        state.decode_attempt(self)

        # Check that at least one word has been dictated, otherwise fail.
        if state.rule() != self.imported_name:
            state.decode_failure(self)
            return

        # Determine how many words have been dictated.
        count = 1
        while state.rule(count) == self.imported_name:
            count += 1

        # Yield possible states where the number of dictated words
        # gobbled is decreased by 1 between yields.
        for i in range(count, 0, -1):
            state.next(i)
            state.decode_success(self)
            yield state
            state.decode_retry(self)
            state.decode_rollback(self)

        # None of the possible states were accepted, failure.
        state.decode_failure(self)
        return

    def value(self, node):
        return node.words()

class SingleWord(DgnImported):
    def __init__(self, name, default=None):
        DgnImported.__init__(self, name, imported_name="dgnwords", default=default)

    def value(self, node):
        return node.words()[0]
