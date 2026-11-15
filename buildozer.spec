[app]
title = PronoCote Pro
package.name = pronocote
package.domain = com.pierreloba
source.dir = .
source.include_exts = py,png,jpg,kv
version = 2.0
requirements = python3,kivy,requests,plyer
orientation = portrait
fullscreen = 0

android.permissions = INTERNET,VIBRATE,POST_NOTIFICATIONS
android.api = 35
android.minapi = 23
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
