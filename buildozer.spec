[app]
title = Buscador Ingredientes
package.name = buscadoringredientes
package.domain = org.nahuel
source.dir = .
source.include_exts = py,kv,xlsx,txt
version = 1.0.0
requirements = python3,kivy,numpy,pandas,openpyxl
orientation = portrait
fullscreen = 1

# Permisos Android
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Bootstrap
p4a.bootstrap = sdl2

# Configuración Android
android.api = 33
android.minapi = 24
android.ndk = 25b
android.ndk_api = 24

# Copiar librerías
android.copy_libs = 1

# Opciones de compilación
log_level = 2
