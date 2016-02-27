#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import inspect

# Import from parent directory
currentdir = os.path.dirname(
    os.path.abspath(
        inspect.getfile(
            inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

import settings
from lib.directory import PhotoDirectory

directory = PhotoDirectory(settings.SOURCE_ROOT)
directory.process()
