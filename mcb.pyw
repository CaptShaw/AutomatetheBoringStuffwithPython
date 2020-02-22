#! python3
# -*- coding: utf-8 -*-

__author__ = 'CaptShaw'

"""
    mcb.pyw - saves and loards pieces of text to the clipboard.
    usage: py.exe mcb.pyw save <keyword> - saves clipboard to keyword
           py.exe mcb.pyw <keyword> - loads keyword to clipboard
           py.exe mcb.pyw list - loads all keywords to clipboard.
"""
import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')
# TODO: save clipboard content
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        # mcbShelf[sys.sys.argv[2]] = ''
        del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # TODO: list keywords and load content
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])
    elif sys.argv[1].lower() == 'delete':
        mcbShelf.clear()
mcbShelf.close()
