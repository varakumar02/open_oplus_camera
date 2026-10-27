#!/usr/bin/env python3
#
# SPDX-FileCopyrightText: varakumar02
# SPDX-License-Identifier: Apache-2.0
#
"""Rebuild the patched odm camera configs of one device for open_oplus_camera_blobs.

Usage: odm_patch.py <device> <stock root> [<blobs repo>]

<stock root> is a directory holding the device's stock odm/ files: a firmware dump, or
vendor/oneplus/<device>/proprietary in the source tree. Each patches-odm/<device>/*.patch
is a git diff (binary for the protobuf and the tuning file) against the stock file it
names. The stock files are copied to <blobs repo>/devices/<device>/, the patches are
applied there in file-name order, and devices/<device>.mk installs the result.
<blobs repo> defaults to vendor/oplus/camera-blobs next to this repo.
"""
import os
import re
import shutil
import subprocess
import sys

HERE = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))


def main(device, stock, blobs=None):
    blobs = blobs or os.path.join(os.path.dirname(HERE), 'camera-blobs')
    pdir = os.path.join(HERE, 'patches-odm', device)
    patches = sorted(os.path.join(pdir, p) for p in os.listdir(pdir) if p.endswith('.patch'))
    out = os.path.join(blobs, 'devices', device)
    shutil.rmtree(out, ignore_errors=True)
    for p in patches:
        with open(p, 'rb') as f:
            for path in re.findall(rb'^diff --git a/(\S+) b/', f.read(), re.M):
                path = path.decode()
                os.makedirs(os.path.dirname(os.path.join(out, path)), exist_ok=True)
                shutil.copyfile(os.path.join(stock, path), os.path.join(out, path))
    # From the blobs root with --directory: run inside a subdirectory of a work tree,
    # git apply skips every path without a word.
    subprocess.run(['git', 'apply', '--whitespace=nowarn', f'--directory=devices/{device}', *patches],
                   cwd=blobs, check=True)
    print(f'{len(patches)} patches applied in {out}')


if __name__ == '__main__':
    if len(sys.argv) not in (3, 4):
        sys.exit(__doc__)
    main(*sys.argv[1:])
