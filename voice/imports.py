# from voice.imports import *

from dragonfly import *

# from .lib.ccrmerger import CCRMerger
from .utils.elements import Dictation, Choice, Boolean
from .utils import navigation, workspace, utilities
from .utils import textformat, execution
from .utils.actions import Text, Key, SlowKey, SlowText, Read
from .utils.execution import Alternating, SlowAlternating

from subprocess import Popen

# Breathe = CCRMerger()
from breathe import Breathe, CommandContext