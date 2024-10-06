###########################################################################################
#
# ĦTest
#
# Copyright (c) 2024 Hydraledger / hydraledger.tech / GPLv3 License
#
###########################################################################################


[app]
title = ĦTest
package.name = htest
package.domain = tech.hydraledger

source.dir = .
source.include_exts = 0,1,2,3,atlas,css,epub,frag,gz,html,ico,jpg,js,jpeg,kv,mo,mp3,pdf,png,py,pyi,so,ttf,typed,webp,whl,woff2,zip
source.include_patterns = assets/*
source.exclude_patterns = app_storage/*,patches/*,venv/*,Makefile,./Makefil*,requirements,precompiled/*,parked/*,./setup.py,Makef*,./Makefile,Makefile

version = 0.1
android.numeric_version = 20240907

requirements = kivy==2.3.0,kivymd==1.2.0,pillow,requests,mnemonic,pycryptodome
p4a.local_recipes = ../recipes/
p4a.branch = develop

icon.filename = %(source.dir)s/assets/icons/icon.png
presplash.filename = %(source.dir)s/assets/icons/presplash_small.png
android.presplash_color = #00000000

orientation = portrait,landscape,portrait-reverse,landscape-reverse
fullscreen = 0

android.permissions = INTERNET

android.api = 33
android.minapi = 24
android.ndk = 25b
android.skip_update = False
android.accept_sdk_license = True
android.release_artifact = apk
android.archs = arm64-v8a,armeabi-v7a
#android.logcat_filters = *:S python:D

android.whitelist = lib-dynload/termios.so
android.add_gradle_repositories = flatDir { dirs("libs") }

[buildozer]
log_level = 2
warn_on_root = 0
build_dir = ./.buildozer
bin_dir = ./bin
