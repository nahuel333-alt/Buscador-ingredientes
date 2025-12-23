[app]
# Nombre de la aplicación
title = Buscador Ingredientes
# Nombre del paquete (recomendado en minúsculas)
package.name = buscadoringredientes
# Dominio de tu app (no obligatorio, pero se recomienda)
package.domain = org.nahuel
# Carpeta donde está el código fuente
source.dir = .
# Archivo principal de Python
source.main = main.py
# Lista de requisitos de Python
requirements = python3,kivy,numpy,pandas,openpyxl
# Icono de la app (opcional)
# icon.filename = %(source.dir)s/icon.png
# Orientación de la app
orientation = portrait
# Indica si la app se puede instalar en tablet
fullscreen = 1
# Versión de la app
version = 1.0
# SDL2 es el bootstrap recomendado para Android
p4a.bootstrap = sdl2

[buildozer]
# Directorio donde se guardarán los builds
build_dir = .buildozer
# Nivel de log (0=minimal, 2=debug)
log_level = 2
# Directorio donde se almacenan archivos temporales
# bin_dir = bin (por defecto)
# Comando para limpiar después de construir
# clean_build = True

[android]
# Versión mínima de Android
android.minapi = 24
# Versión objetivo de Android
android.api = 33
# Versión del NDK (opcional, Buildozer lo descarga)
# android.ndk = 25b
# SDK Build-tools
android.build_tools_version = 33.0.2
# Activar permisos si es necesario
# android.permissions = INTERNET
# Si se requiere orientación por pantalla
# android.orientation = portrait

# Se pueden agregar más opciones aquí según tu app
