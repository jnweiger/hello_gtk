# FROM https://stackoverflow.com/questions/15734703/use-cx-freeze-to-create-an-msi-that-adds-a-shortcut-to-the-desktop
# See also:
# - https://docs.microsoft.com/en-us/windows/win32/msi/property-reference?redirectedfrom=MSDN#System_Folder_Properties
# - https://docs.microsoft.com/en-us/windows/win32/msi/property-reference#system-folder-properties
# - https://stackoverflow.com/questions/25381761/creating-an-installer-for-a-python-gtk3-application#25443285
from cx_Freeze import *

# http://msdn.microsoft.com/en-us/library/windows/desktop/aa371847(v=vs.85).aspx
# FIXME: TARGETDIR probably needs to be replaced with something that actually exists?
shortcut_table = [
    ("DesktopShortcut",        # Shortcut
     "DesktopFolder",          # Directory_     
     "Hello from Qt5",          # Name
     "TARGETDIR",              # Component_
     "[TARGETDIR]helloqt5.exe",# Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     None,                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     'TARGETDIR'               # WkDir
     )
    ]


setup(
    options = {
        "bdist_msi": {"Shortcut": shortcut_table},
    },
    executables = [
        Executable(
            "hello_gtk.py",
            shortcutName="Hello Gtk",
            shortcutDir="DesktopFolder",        # any of the System Folder Properries
            )
        ]
    )

## Use ALLUSERS=1 on the msiexec command line so that an administrator install adds the desktop shortcut to all users.
