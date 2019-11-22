# from my_commands.imports import *

from dragonfly import *

# from .lib.ccrmerger import CCRMerger
from .utils.elements import Dictation, Choice, Boolean
from .utils import navigation, workspace, utilities
from .utils import textformat, execution
from .utils.actions import Text, Key, SlowKey, SlowText, Read
from .utils.execution import Alternating, SlowAlternating

from subprocess import Popen
from six import string_types

# Breathe = CCRMerger()
from breathe import Breathe, CommandContext, CommandsRef, Exec

# Acts like a list which contains the last 20 commands,
# most recent last
breathe_repetition_history = RecognitionHistory(20)
breathe_repetition_history.register()
