[app]
# Nombre de la app
title = Buscador Ingredientes
package.name = buscadoringredientes
package.domain = org.nahuel
source.dir = .
source.include_exts = py,png,jpg,kv,xlsx,csv
version = 1.0.0
orientation = portrait
fullscreen = 0
# Permite aceptar licencias automáticamente
android.accept_sdk_license = True

# Icono y splash (si tenés)
# icon.filename = %(source.dir)s/icon.png
# presplash.filename = %(source.dir)s/presplash.png

# Requerimientos de Python
requirements = python3,kivy,numpy,pandas,openpyxl

# Archivos adicionales a copiar al APK
# include_patterns = assets/*,data/*.txt

# No actualizar el SDK automáticamente
android.skip_update = True

# Versión mínima y target de Android
android.api = 33
android.minapi = 24
android.ndk_api = 24

# Bootstrap recomendado
p4a.bootstrap = sdl2
p4a.source_dir = .buildozer/android/platform/python-for-android
p4a.libraries = sqlite3

# Archivos a copiar en la carpeta de assets dentro del APK
android.add_assets = data/

# Permisos (si necesitás acceso a Internet, almacenamiento, etc.)
# android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE

# Configuración para no cerrar la app en ciertos errores de Cython
log_level = 2

[buildozer]
# Directorio donde se crea todo el build
build_dir = .buildozer
