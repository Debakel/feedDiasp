import os, sys, inspect
# enable usage of the local version of diaspy
cmd_path = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
diaspy_path = cmd_path + '/diaspy'
if os.path.exists(diaspy_path):
    sys.path.insert(0, diaspy_path)

from feedDiasp import RSSParser
from feedDiasp import FBParser
from feedDiasp import FeedDiasp
from feedDiasp import Diasp
