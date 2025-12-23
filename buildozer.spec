[app]
# Nombre y paquete
title = Buscador Ingredientes
package.name = buscadoringredientes
package.domain = org.nahuel

# Directorio de código fuente
source.dir = .
source.include_exts = py,png,jpg,kv,txt

# Versión de la app
version = 1.0

# Orientación y pantalla
orientation = portrait
fullscreen = 1

# Dependencias
requirements = python3,kivy,numpy,pandas,openpyxl

# Android
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.minapi = 24
android.sdk = 33
android.accept_sdk_license = True
p4a.bootstrap = sdl2

# Logging
log_level = 2

# Opciones varias
# Evitar que Buildozer intente actualizar SDK automáticamente (útil en CI)
android.skip_update = True

# Archivos a ignorar
ignore_patterns = *.pyc, *.pyo, *.git, __pycache__

# Otras configuraciones útiles
presplash.filename = %(source.dir)s/data/presplash.png
icon.filename = %(source.dir)s/data/icon.png
