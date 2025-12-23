[app]
title = Buscador de Ingredientes
package.name = buscadoringredientes
package.domain = org.nahuel

source.dir = .
source.include_exts = py,xlsx

version = 1.0

# Módulos necesarios
requirements = python3,kivy,numpy,pandas,openpyxl

# Bootstrap y API/NDK
p4a.branch = develop
android.api = 33
android.minapi = 24
android.ndk = https://dl.google.com/android/repository/android-ndk-r25b
android.ndk_path = /home/runner/android-sdk/ndk/25.2.9519653
android.sdk_path = /home/runner/android-sdk
android.build_tools = 33.0.2
android.skip_update = True

# Configuraciones generales
orientation = portrait
fullscreen = 1
log_level = 2
