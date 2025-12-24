[app]
# Nombre de la app
title = Buscador Ingredientes
package.name = buscadoringredientes
package.domain = org.nahuel
source.dir = .
version = 1.0.0
requirements = python3,kivy,numpy,pandas,openpyxl
orientation = portrait
fullscreen = 1
# Para aceptar licencias automáticamente
android.accept_sdk_license = True

# Bootstrap
p4a.bootstrap = sdl2

# Configuración de la API
android.api = 24
android.minapi = 24
android.ndk = 25b
android.ndk_api = 24

# Copiar librerías
android.copy_libs = 1

# Opciones de compilación
log_level = 2
