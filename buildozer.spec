[app]
title = Buscador Ingredientes
package.name = buscadoringredientes
package.domain = org.nahuel
source.include_exts = py,xlsx
version = 1.0
orientation = portrait
fullscreen = 1

# Kivy / Python
requirements = python3,kivy,numpy,pandas,openpyxl
presplash.filename = presplash.png
icon.filename = icon.png
android.api = 33
android.minapi = 24
android.sdk = 30
android.ndk = 25b
android.build_tools_version = 30.0.3
android.permissions = INTERNET

# P4A / SDL2
p4a.bootstrap = sdl2
p4a.source_dir = ./p4a
p4a.branch = master

# Packaging
android.arch = arm64-v8a,armeabi-v7a
android.copy_libs = 1
