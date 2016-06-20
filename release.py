#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
release.py
Retrieve latest compressed wheels from GitHub


Created by Stephan Hügel on 2016-06-19
"""

import cStringIO
import io
import tarfile
import zipfile
import requests
from subprocess import check_output

path = 'dist/'
url = "https://github.com/urschrei/convertbng/releases/download/{tag}/convertbng-{tag}-{target}.{extension}"
# get latest tag
tag = check_output(["git", "describe", "--abbrev=0"]).strip()

dicts = [
{
    'tag': tag,
    'target': 'x86_64-apple-darwin',
    'extension': 'tar.gz'
    },
{
    'tag': tag,
    'target': 'x86_64-unknown-linux-gnu',
    'extension': 'tar.gz'
    },
{
    'tag': tag,
    'target': 'x86_64-pc-windows-msvc',
    'extension': 'zip'
    }
]
for dct in dicts:
    built = url.format(**dct)
    retrieved = requests.get(built, stream=True)
    content = retrieved.content
    if dct.get('extension') == 'zip':
        so = cStringIO.StringIO(content)
        raw_zip = zipfile.ZipFile(so)
        raw_zip.extractall(path)
    else:
        fo = io.BytesIO(content)
        tar = tarfile.open(mode="r:gz", fileobj=fo)
        tar.extractall(path)