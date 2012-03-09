#!/usr/bin/env python
# -*- coding: utf-8 -*-

import settings
from lib.directory import PhotoDirectory

directory = PhotoDirectory(settings.SOURCE_ROOT)
directory.process()
