#!/usr/bin/env python3

import inspect
import os
import sys

# enable usage of the local version of diaspy
cmd_path = os.path.realpath(os.path.abspath(os.path.split(inspect.getfile(inspect.currentframe()))[0]))
diaspy_path = cmd_path + '/diaspy'
if os.path.exists(diaspy_path):
    sys.path.insert(0, diaspy_path)

