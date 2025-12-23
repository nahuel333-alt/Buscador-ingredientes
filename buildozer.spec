[app]
title = Buscador de Ingredientes
package.name = buscadoringredientes
package.domain = org.nahuel

source.dir = .
source.include_exts = py,xlsx

version = 1.0

requirements = python3,kivy,pandas,openpyxl

orientation = portrait
fullscreen = 1

android.api = 33
android.minapi = 21
android.build_tools = 33.0.2
android.sdk = 33

[buildozer]
log_level = 2
warn_on_root = 1
