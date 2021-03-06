#!/usr/bin/env python
#-*- coding: utf-8 -*-

import os
import sys
import shutil

from qtgui.pinguino_api.pinguino_config import PinguinoConfig

os.environ["PINGUINO_HOME"] = os.path.abspath(sys.path[0])

# For PyInstaller compatibility
if os.path.exists(os.path.abspath("pinguino_data")):
    os.environ["PINGUINO_DATA"] = os.path.abspath("pinguino_data")
else:
    os.environ["PINGUINO_DATA"] = os.getenv("PINGUINO_HOME")

PinguinoConfig.set_environ_vars()

#Remove files and directories
if os.path.isdir(os.path.join(os.getenv("PINGUINO_USER_PATH"), "source")):
    shutil.rmtree(os.path.join(os.getenv("PINGUINO_USER_PATH"), "source"))


#Remove old files
#RB20150202 : each file must be checked before being deleted
if os.path.isfile(os.path.join(os.getenv("PINGUINO_USER_PATH"), "reserved.pickle")):
    os.remove(os.path.join(os.getenv("PINGUINO_USER_PATH"), "reserved.pickle"))
#if os.path.isfile(os.path.join(os.getenv("PINGUINO_USER_PATH"), "pinguino.conf")):
    #os.remove(os.path.join(os.getenv("PINGUINO_USER_PATH"), "pinguino.conf"))
if os.path.isfile(os.path.join(os.getenv("PINGUINO_USER_PATH"), "wikidocs.pickle")):
    os.remove(os.path.join(os.getenv("PINGUINO_USER_PATH"), "wikidocs.pickle"))


#Check files and directories
PinguinoConfig.check_user_files()
