[app]
# (str) Title of your application
title = Buscador de Ingredientes

# (str) Package name
package.name = buscadoringredientes

# (str) Package domain (reverse DNS style)
package.domain = org.nahuel

# (str) Source code where the main.py is located
source.dir = .

# (list) Source files to include (let empty to include all)
source.include_exts = py,png,jpg,kv,xlsx

# (str) Application versioning
version = 1.0

# (str) Icon of the app
icon.filename = %(source.dir)s/icon.png

# (str) Supported orientation: portrait, landscape, all
orientation = portrait

# (bool) Fullscreen mode
fullscreen = 1

# (str) Presplash image
presplash.filename = %(source.dir)s/presplash.png

# (str) Supported Android API (target)
android.api = 33

# (str) Minimum Android API your app supports
android.minapi = 24

# (str) Android SDK version (handled by p4a)
#android.sdk = 24

# (str) Android NDK version
android.ndk = 25b

# (str) Android NDK API level
android.ndk_api = 24

# (str) Bootstrap to use (SDL2 recommended)
android.bootstrap = sdl2

# (list) Application requirements
requirements = python3,kivy,numpy,pandas,openpyxl

# (bool) Copy libraries instead of compiling them
android.copy_libs = 1

# (str) Presplash orientation (same as main orientation)
android.presplash_orientation = portrait

# (list) Supported architectures
android.archs = arm64-v8a,armeabi-v7a

# (bool) Enable debug mode
android.debug = 1

# (int) Timeout for build in seconds
android.timeout = 1800

# (str) Folder for Buildozer to store build artifacts
# default is .buildozer in project folder
# build_dir = .buildozer

# (bool) Android entry point (usually main.py)
#android.entrypoint = main.py

# (bool) Android logcat filtering
#android.logcat_filters = *:S python:D

# (bool) Android presplash fade in/out
#android.presplash_fade = true

# (str) Android application theme
#android.theme = '@android:style/Theme.NoTitleBar'

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (bool) Use AndroidX
android.use_androidx = True

# (bool) Show a notification during build
#android.notify = True

# (str) Custom source for python-for-android (optional)
#p4a.source_dir =

# (bool) Ignore setup.py (recommended)
#ignore_setup_py = True
