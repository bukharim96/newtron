# @todo

- BrowserView, BrowserWindow
    - title
    - url
    - js_api
    - width
    - height
    - resizable
    - fullscreen
    - min_size
    - strings
    - confirm_quit
    - background_color
    - debug
    - text_selection
    - frame: false
    - transparent: true
    - titleBarStyle: 'hidden' (mac)
    - Draggable region
- Accelerator (key codes shortcuts)
- Menu
- Notification
- Tray
- Locales
- Clipboard
- Debugger
- Dialog
    - browserWindow BrowserWindow (optional)
    - options Object
      - title String (optional)
      - defaultPath String (optional)
      - buttonLabel String (optional) - Custom label for the confirmation button, when left empty the default label will be used.
      - filters FileFilter[] (optional)
      - properties String - Contains which features the dialog should use. The following values are supported:
          - openFile - Allow files to be selected.
          - openDirectory - Allow directories to be selected.
          - multiSelections - Allow multiple paths to be selected.
          - showHiddenFiles - Show hidden files in dialog.
          - createDirectory macOS - Allow creating new directories from dialog.
          - promptToCreate Windows - Prompt for creation if the file path entered in the dialog does not exist. This does not actually create the file at the path but allows non-existent paths to be returned that should be created by the application.
          - noResolveAliases macOS - Disable the automatic alias (symlink) path resolution. Selected aliases will now return the alias path instead of their target path.
          - treatPackageAsDirectory macOS - Treat packages, such as .app folders, as a directory instead of a file.
      - message String (optional) macOS - Message to display above input boxes.
      - securityScopedBookmarks Boolean (optional) masOS mas - Create security scoped bookmarks when packaged for the Mac App Store.
    - callback Function (optional)