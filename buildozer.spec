[app]

# (str) Title of your application
title = Buscador Ingredientes

# (str) Package name
package.name = buscadoringredientes

# (str) Package domain (reverse DNS style)
package.domain = org.nahuel

# (str) Source code directory (relative to this spec file)
source.dir = .

# (list) List of inclusions using pattern matching
source.include_exts = py,png,jpg,kv,txt,xlsx

# (str) Application versioning (method 1)
version = 1.0.0

# (list) Application requirements
requirements = python3,kivy,numpy,pandas,openpyxl

# (str) Entry point for your app
entrypoint = main.py

# (str) Icon of the app
icon.filename = %(source.dir)s/icon.png

# (list) Supported orientation: portrait, landscape
orientation = portrait

# (list) Permissions (optional)
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# (int) Minimum API your app will support
android.minapi = 24

# (int) Target API
android.api = 33

# (int) Android SDK Build-Tools version
android.build_tools_version = 33.0.2

# (str) NDK version (let Buildozer manage it)
android.ndk = 25b

# (str) Android bootstrap (use current)
p4a.bootstrap = sdl2

# (str) Presplash image
presplash.filename = %(source.dir)s/presplash.png

# (bool) Include debug symbols
android.debug = 1

# (bool) Include assets in the APK
android.add_assets = %(source.dir)s/assets

# (str) Android archs
android.archs = arm64-v8a, armeabi-v7a

# (list) Additional python-for-android recipes
p4a.extra_packages =

# (str) Android icon, optional
android.icon = %(source.dir)s/icon.png
