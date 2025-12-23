[app]

# (str) Title of your application
title = Buscador de Ingredientes

# (str) Package name
package.name = buscadoringredientes

# (str) Package domain (can be anything)
package.domain = org.nahuel

# (str) Source code where the main.py is located
source.dir = .

# (list) Source files to include (let empty to include all)
source.include_exts = py,png,jpg,kv,xlsx

# (str) Application versioning (method 1)
version = 1.0

# (int) Application versioning (method 2)
# version.code =

# (str) Application versioning (method 3)
# version.regex =

# (list) Application requirements
requirements = python3,kivy,numpy,pandas,openpyxl

# (str) Supported orientation
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (str) Application entry point
# (this is usually main.py)
entrypoint = main.py

# (str) The icon of the app
# icon.filename = %(source.dir)s/icon.png

# (list) Presplash images
# presplash.filename = %(source.dir)s/presplash.png

# (str) Supported Android bootstrap (SDL2 recommended)
p4a.bootstrap = sdl2

# (str) Android SDK version
android.api = 33

# (str) Minimum Android API your app supports
android.minapi = 24

# (str) Android NDK version
android.ndk = 25b

# (str) Build-tools version (evita problema de AIDL)
android.build_tools_version = 33.0.2

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (bool) Android entry point (if using SDL2)
# android.entrypoint = org.kivy.android.PythonActivity

# (str) Supported architecture
android.archs = arm64-v8a, armeabi-v7a

# (bool) Copy libraries to APK
android.copy_libs = 1

# (str) Android logcat filters
# android.logcat_filters = *:S python:D

# (list) Whitelist of whitelisted modules
# android.whitelist = 

# (str) Extra Python-for-Android arguments
# p4a.extra_args = 

# (str) Presplash color (RGB)
# presplash.color = #FFFFFF

# (list) Included assets
# assets.exclude_exts = 

# (bool) Enable fullscreen (for SDL2)
# fullscreen = 1

# (str) Application versioning (optional alternative)
# version.regex = 

# (bool) Copy your Python code to the device instead of compiling
# android.copy_source = 1

# (str) Android keystore (for release)
# android.keystore = %(source.dir)s/mykeystore.keystore
# android.keyalias = mykey
# android.keyalias_passwd = password

# (list) Android manifest additions
# android.manifest_additions =

# (list) Presplash screen
# presplash.filename = %(source.dir)s/presplash.png

# (list) Icon for Android
# icon.filename = %(source.dir)s/icon.png
