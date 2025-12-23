[app]
# Nombre de la app y paquete
title = Buscador de Ingredientes
package.name = buscadoringredientes
package.domain = org.nahuel

# Carpeta de origen y archivos a incluir
source.dir = .
source.include_exts = py,xlsx
source.include_patterns = *.xlsx

# Versión de la app
version = 1.0

# Requerimientos de Python y librerías
requirements = python3,kivy==2.3.2,numpy==1.25.2,pandas==2.2.2,openpyxl
p4a.branch = master

# Android
android.api = 33
android.minapi = 24
android.build_tools = 33.0.2
android.ndk = 25b
android.skip_update = True

# Orientación y pantalla
orientation = portrait
fullscreen = 1

# Paths de SDK/NDK se manejan automáticamente
# android.sdk_path =
# android.ndk_path =

# Opciones de compilación
log_level = 2
warn_on_root = 1
