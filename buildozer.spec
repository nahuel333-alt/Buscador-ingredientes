[app]
# Nombre de la app
title = Buscador Ingredientes
package.name = buscadoringredientes
package.domain = org.nahuel
source.dir = .
source.include_exts = py,kv,xlsx,txt
version = 1.0.0

# Dependencias
requirements = python3,kivy,numpy,pandas,openpyxl

# Orientación y pantalla
orientation = portrait
fullscreen = 1

# Permisos necesarios para leer/escribir archivos en Android
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Aceptar licencias automáticamente
android.accept_sdk_license = True

# Bootstrap
p4a.bootstrap = sdl2

# Configuración de Android
android.api = 33
android.minapi = 24
android.ndk = 25b
android.ndk_api = 24

# Copiar librerías
android.copy_libs = 1

# Nivel de log para debugging
log_level = 2
