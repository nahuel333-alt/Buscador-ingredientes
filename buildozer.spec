[app]

# (str) Title of your application
title = Buscador Ingredientes

# (str) Package name
package.name = buscadoringredientes

# (str) Package domain (reverse DNS notation)
package.domain = org.nahuel

# (str) Source code where the main.py is located
source.dir = .

# (str) Application version
version = 1.0.0

# (list) Requirements separated by commas
requirements = python3,kivy,numpy,pandas,openpyxl

# (str) Entry point of the app
entrypoint = main.py

# (list) Permissions required
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE

# (str) Android SDK version to use (deprecated in favor of p4a)
# android.sdk = 33

# (str) Python-for-Android bootstrap
p4a.bootstrap = sdl2

# (list) Supported architectures
android.archs = arm64-v8a,armeabi-v7a

# (bool) Copy libraries instead of linking
android.copy_libs = 1

# (str) Minimum Android API your app supports
android.minapi = 24

# (str) Target Android API
android.api = 33

# (str) Build-tools version
android.build_tools_version = 33.0.2

# (bool) Enable debug mode
android.debug = 1

# (str) Directory for temporary build files
build_dir = .buildozer

# (str) Android NDK version (optional)
# android.ndk = 25b

# (list) Exclude any modules not needed
# exclude_modules =

[buildozer]

# (str) Path to Buildozer bin (usually default)
build_dir = .buildozer
