# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 - 2024 ANSYS, Inc. and/or its affiliates.
# SPDX-License-Identifier: MIT
#
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
Launches an interactive shell with an instance of HFSS.

Omitting the .py in the name of this file hides it from the Electronics Desktop Toolkit menu.
It should be hidden from this menu because the scripts in that menu are meant to be executed using IronPython
cpython_console.py should be run instead of this script.

This file can also serve as a template to modify PyAEDT scripts to take advantage of the command line arguments
provided by the launcher
"""

import atexit
import os
import sys

aedt_process_id = int(sys.argv[1])
version = sys.argv[2]
print("Loading the PyAEDT Console.")

try:
    if version <= "2023.1":
        from pyaedt import Desktop
        from pyaedt.generic.general_methods import active_sessions
        from pyaedt.generic.general_methods import is_windows
    else:
        from ansys.aedt.core import Desktop
        from ansys.aedt.core.generic.general_methods import active_sessions
        from ansys.aedt.core.generic.general_methods import is_windows
except ImportError:
    # Debug only purpose. If the tool is added to the ribbon from a GitHub clone, then a link
    # to PyAEDT is created in the personal library.
    console_setup_dir = os.path.dirname(__file__)
    if "PersonalLib" in console_setup_dir:
        sys.path.append(os.path.join(console_setup_dir, "../..", "..", ".."))
    if version <= "2023.1":
        from pyaedt import Desktop
        from pyaedt.generic.general_methods import active_sessions
        from pyaedt.generic.general_methods import is_windows
    else:
        from ansys.aedt.core import Desktop
        from ansys.aedt.core.generic.general_methods import active_sessions
        from ansys.aedt.core.generic.general_methods import is_windows


def release(d):
    d.logger.info("Exiting the PyAEDT Console.")

    d.release_desktop(False, False)


session_found = False
port = 0
student_version = False


sessions = active_sessions(version=version, student_version=False)
if aedt_process_id in sessions:
    session_found = True
    if sessions[aedt_process_id] != -1:
        port = sessions[aedt_process_id]
if not session_found:
    sessions = active_sessions(version=version, student_version=True)
    if aedt_process_id in sessions:
        session_found = True
        student_version = True
        if sessions[aedt_process_id] != -1:
            port = sessions[aedt_process_id]

error = False
if port:
    desktop = Desktop(
        version=version,
        port=port,
        new_desktop=False,
        non_graphical=False,
        close_on_exit=False,
        student_version=student_version,
    )
elif is_windows:
    desktop = Desktop(
        version=version,
        aedt_process_id=aedt_process_id,
        new_desktop=False,
        non_graphical=False,
        close_on_exit=False,
        student_version=student_version,
    )
else:
    print("Error. AEDT should be started in gRPC mode in Linux to connect to PyAEDT")
    print("use ansysedt -grpcsrv portnumber command.")
    error = True
if not error:
    print(" ")

    print("\033[92m****************************************************************")
    print(f"*  ElectronicsDesktop {version} Process ID {aedt_process_id}")
    print(f"*  CPython {sys.version.split(' ')[0]}")
    print("*---------------------------------------------------------------")
    print("*  Example: \033[94m hfss = ansys.aedt.core.Hfss() \033[92m")
    print("*  Example: \033[94m m2d = ansys.aedt.core.Maxwell2d() \033[92m")
    print("*  \033[31mType exit() to close the console and release the desktop.  \033[92m ")
    print("*  desktop object is initialized and available. Example: ")
    print("*  \033[94mdesktop.logger.info('Hello world')\033[92m")
    print("****************************************************************\033[0m")
    print(" ")
    print(" ")
    print(" ")
    atexit.register(release, desktop)
