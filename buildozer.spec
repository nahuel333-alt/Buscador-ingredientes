[app]
# Nombre y paquete de tu app
title = Buscador Ingredientes
package.name = buscadoringredientes
package.domain = org.nahuel

# Carpeta con tu código fuente
source.dir = .

# Requerimientos de Python y librerías
requirements = python3,kivy,numpy,pandas,openpyxl,cython==0.29.36

# Permisos de Android (si necesitás alguno, agregalos aquí)
#android.permissions = INTERNET

# Licencias y actualizaciones
android.accept_sdk_license = True
#android.skip_update = True

# Opciones del bootstrap (SDL2 recomendado)
p4a.bootstrap = sdl2

# Arquitecturas soportadas
android.arch = arm64-v8a,armeabi-v7a

# Nivel mínimo de API de Android
android.minapi = 24
android.api = 33
android.ndk = 25b
android.ndk_api = 24
android.sdk = 33

# Copiar librerías al APK
android.copy_libs = 1

# Directorios de logs y compilación
log_level = 2
