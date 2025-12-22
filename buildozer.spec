[app]
# Información básica de la app
title = Buscador de Ingredientes
package.name = buscadoringredientes
package.domain = org.nahuel
source.dir = .
source.include_exts = py,xlsx,png,kv

# Versión
version = 1.0

# Librerías requeridas
requirements = python3==3.10,kivy==2.2.1,pandas,openpyxl

# Pantalla
orientation = portrait
fullscreen = 1

# Permisos Android
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.build_tools_version = 31.0.0
android.archs = arm64-v8a
android.accept_sdk_license = true

[buildozer]
# Logs y advertencias
log_level = 2
warn_on_root = 1
