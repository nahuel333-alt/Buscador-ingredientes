[app]
title = Buscador Ingredientes
package.name = buscadoringredientes
package.domain = org.nahuel
source.dir = .
source.include_exts = py,png,jpg,kv,kvlang
version = 1.0
requirements = python3,kivy,numpy,pandas,openpyxl
orientation = portrait

# --- Android ---
# Paths locales para evitar problemas de licencias
android.sdk_path = .buildozer/android/platform
android.ndk_path = .buildozer/android/platform/ndk
android.ndk_version = 25b
android.api = 33
android.minapi = 24
android.build_tools_version = 33.0.2
android.bootstrap = sdl2

# Evitar que busque en /home/runner/android-sdk
android.sdk = None
