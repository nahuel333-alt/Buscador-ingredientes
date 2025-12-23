[app]
# Nombre de la app
title = Buscador Ingredientes
package.name = buscadoringredientes
package.domain = org.nahuel
source.dir = .
version = 1.0.0
requirements = python3,kivy==2.2.1,numpy,pandas,openpyxl
orientation = portrait
fullscreen = 1

# Para aceptar licencias automáticamente
android.accept_sdk_license = True

# Bootstrap
p4a.bootstrap = sdl2

# Configuración de la API
android.api = 33
android.minapi = 24
android.ndk = 25b
android.ndk_api = 24

# Copiar librerías
android.copy_libs = 1

# Configuración de permisos más comunes
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

# Configuración de log
log_level = 2
android.logcat_filters = *:S python:D

# Evitar que Buildozer actualice automáticamente NDK/SDK
android.skip_update = True

# Mejor compatibilidad con pantallas
android.screen_orientation = portrait
android.fullscreen = True

# Incluir librerías extras si fueran necesarias
#android.add_libs_armeabi_v7a = path/to/libs/*.so
#android.add_libs_arm64_v8a = path/to/libs/*.so
