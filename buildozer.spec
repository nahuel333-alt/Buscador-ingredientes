[app]
title = Buscador de Ingredientes
package.name = buscadoringredientes
package.domain = org.nahuel
source.dir = .
source.include_exts = py,xlsx,png,kv

version = 1.0
requirements = python3==3.8,kivy==2.2.1,pandas,openpyxl

orientation = portrait
fullscreen = 1

android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.build_tools_version = 31.0.0
android.accept_sdk_license = true

[buildozer]
log_level = 2
warn_on_root = 1
