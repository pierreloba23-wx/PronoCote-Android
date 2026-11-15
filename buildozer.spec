[app]
title = PronoCote
package.name = pronocote
package.domain = com.pronocote
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,txt
icon.filename = %(source.dir)s/icon.png
version = 1.1.0
requirements = python3,kivy,requests,plyer
orientation = portrait
fullscreen = 0
presplash.filename = %(source.dir)s/icon.png
android.permissions = INTERNET,VIBRATE,POST_NOTIFICATIONS
android.api = 35
android.minapi = 23
android.archs = arm64-v8a, armeabi-v7a
android.accept_sdk_license = True
p4a.bootstrap = sdl2

[buildozer]
log_level = 2
warn_on_root = 1
