[app]
# Nombre de la aplicación
title = Buscador Ingredientes
package.name = buscadoringredientes
package.domain = org.nahuel
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 1.0.0
requirements = python3,kivy,numpy,pandas,openpyxl
orientation = portrait
fullscreen = 1
android.api = 33
android.minapi = 24
android.arch = armeabi-v7a,arm64-v8a
android.sdk = 33
android.ndk = 25b
android.ndk_api = 24
android.private_storage = True
android.bootstrap = sdl2

# Mantener permisos y configuraciones de Android
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.whitelist = *

[buildozer]
log_level = 2
warn_on_root = 1
