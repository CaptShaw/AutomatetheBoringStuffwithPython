#! python3
# -*- coding: utf-8 -*-

__author__ = 'CaptShaw'

"""
   chapter 9
"""

import shutil, os, re, zipfile


def renameDates():
    datePatten = re.compile(r'''^(.*?)
    ((0|1)?\d)-
    (([0-3]?)\d)-
    ((19|20)\d\d)
    (.*?)$
    ''', re.VERBOSE)

    for amerFilename in os.listdir('.'):
        mo = datePatten.search(amerFilename)
        if mo == None:
            continue
        beforePart = mo.group(1)
        monthPart = mo.group(2)
        dayPart = mo.group(4)
        yearPart = mo.group(6)
        afterPart = mo.group(8)

    euroFilename = beforePart + dayPart + '-' + monthPart + '-' + yearPart + afterPart
    absWorkingDir = os.path.abspath('.')
    amerFilename = os.path.join(absWorkingDir, amerFilename)
    euroFilename = os.path.join(absWorkingDir, euroFilename)
    print('Renaming "%s" to "%s"...') % (amerFilename, euroFilename)
    shutil.move(amerFilename, euroFilename)


def backupToZip(folder):
    folder = os.path.abspath(folder)
    number = 1
    while True:
        zipFilename = os.path.basename(folder) + '_' + str(number) + '.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1

    print("Creating %s..." % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    for foldername, subfolders, filenames in os.walk(folder):
        print('Adding files in %s...' % (foldername))
        backupZip.write(foldername)
        for filename in filenames:
            newBase = os.path.basename(foldername) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Done')


backupToZip(os.path.join('C:', 'folder'))
