#!/usr/bin/python3
# -*- coding: utf-8 -*-

print("Content-Type: application/json;charset=utf-8")
print("Access-Control-Allow-Origin: https://schulsportwelten.de\n\n")

import cgi
import cgitb
cgitb.enable()

basepath = '' # ENTER ABSOLUTE BASE BATH OF THIS SCRIPT HERE (no closing /)
filepath = '' # ENTER MP3 FILE PATH HERE

import site
site.addsitedir(basepath + '/site-packages')

import librosa
import numpy
import json

y, sr = librosa.load(filepath, sr=None, mono=False)
mono = librosa.to_mono(y)

width = 800

duration = round(librosa.get_duration(y=y, sr=sr))

data = numpy.zeros(shape=(width*2))
steps = len(mono)/width

for i in range(1,width):
    min = round(numpy.min(mono[round((i-1)*steps):round(i*steps)])*100)/100
    max = round(numpy.max(mono[round((i-1)*steps):round(i*steps)])*100)/100
    data[(2*i)-2] = min
    data[(2*i)-1] = max

datalist = data.tolist()

print("{")
print('"version":2,')
print('"channels":1,')
print('"sample_rate":' + str(sr) + ',')
print('"sample_per_pixel":' + str(round((duration * sr) / width)) + ',')
print('"bits":8,')
print('"length":' + str(width) + ',')

print('"data":' + json.dumps(datalist) + '}')
