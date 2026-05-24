[app]
title = ElimuYetuUniverse
package.name = elimuyetuuniverse
package.domain = org.tz.elimuyetu
source.dir =.
source.include_exts = py,png,jpg,kv,atlas
version = 4.0
requirements = python3,kivy==2.3.0,pillow
orientation = portrait
log_level = 2

[buildozer]
android.archs = arm64-v8a
android.api = 31
android.minapi = 24
android.ndk = 25b
android.accept_sdk_license = True
