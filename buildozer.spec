[app]
# (str) Title of your application
title = Buscador Ingredientes

# (str) Package name
package.name = buscadoringredientes

# (str) Package domain (reverse domain style)
package.domain = org.nahuel

# (str) Source code where your main.py is located
source.dir = .

# (str) Main application entry point
source.main = main.py

# (list) List of inclusions using pattern matching
source.include_exts = py,png,jpg,kv,txt,xlsx

# (str) Application versioning
version = 1.0

# (list) Application requirements
requirements = python3,kivy,numpy,pandas,openpyxl

# (str) Presplash / Icon
icon.filename = %(source.dir)s/icon.png

# (list) Permissions
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (str) Target Android API
android.api = 33
android.minapi = 24
android.sdk = 33
android.ndk = 25b
android.ndk_api = 24
android.arch = arm64-v8a,armeabi-v7a

# (str) Bootstrap (deprecated, kept for backward compatibility)
p4a.bootstrap = sdl2

# (bool) Copy libraries to APK
android.copy_libs = 1

# (str) Orientation
orientation = portrait

# (bool) Fullscreen
fullscreen = 0

[buildozer]
log_level = 2
warn_on_root = 1
