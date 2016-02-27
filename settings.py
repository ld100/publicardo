#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import os.path
import os
import sys
import yaml

PROJECT_ROOT = os.path.normpath(os.path.dirname(__file__))
CONFIG_ROOT = os.path.join(PROJECT_ROOT, "config")
BIN_ROOT = os.path.join(PROJECT_ROOT, "bin")
RESOURCES_ROOT = os.path.join(PROJECT_ROOT, "resources")
FONTS_ROOT = os.path.join(RESOURCES_ROOT, "fonts")

APP_ENVIRONMENT = os.environ.get("APP_ENVIRONMENT", "development")

config_stream = open(os.path.join(CONFIG_ROOT, "settings.yml"), "r")
CONFIG = yaml.load(config_stream)[APP_ENVIRONMENT]

if "local" == CONFIG["folders"]["layout"]:
    SOURCE_ROOT = os.path.join(
        PROJECT_ROOT,
        CONFIG["folders"]["source_folder"])
    DESTINATION_ROOT = os.path.join(
        PROJECT_ROOT, CONFIG["folders"]["destination_folder"])
else:
    SOURCE_ROOT = CONFIG["folders"]["source_folder"]
    DESTINATION_ROOT = CONFIG["folders"]["destination_folder"]

DEBUG = CONFIG["debug"]

# Defining current platform

if "darwin" == sys.platform:
    PLATFORM = "mac"
    JHEAD_BIN = os.path.join(BIN_ROOT, "jhead")
elif "win32" == sys.platform:
    PLATFORM = "win"
    JHEAD_BIN = os.path.join(BIN_ROOT, "jhead.exe")
elif "cygwin" == sys.platform:
    PLATFORM = "win"
    JHEAD_BIN = os.path.join(BIN_ROOT, "jhead.exe")
else:
    PLATFORM = "undefined"
    JHEAD_BIN = os.path.join(BIN_ROOT, "jhead")
