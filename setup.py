#!/usr/bin/env python
#
# Urwid setup.py exports the useful bits
#    Copyright (C) 2004  Ian Ward
#
#    This library is free software; you can redistribute it and/or
#    modify it under the terms of the GNU Lesser General Public
#    License as published by the Free Software Foundation; either
#    version 2.1 of the License, or (at your option) any later version.
#
#    This library is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
#    Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public
#    License along with this library; if not, write to the Free Software
#    Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA  02111-1307  USA
#
# Urwid web site: http://excess.org/urwid/

from distutils.core import setup

import os

release = "0.8.2" #os.popen("make -s release").read().strip()

setup_d = {
	'name':"urwid",
	'version':release,
	'author':"Ian Ward",
	'author_email':"ian@excess.org",
	'url':"http://excess.org/urwid/",
	'download_url':"http://excess.org/urwid/urwid-%s.tar.gz"%release,
	'license':"LGPL",
	'keywords':"curses ui widget scroll listbox interface text layout",
	'platforms':"unix-like",
	'description':"A curses-based UI/widget library featuring fluid interface resizing, multiple text layout options, simple markup for attributes, powerful scrolling list boxes and flexible edit boxes.",
	'long_description':"""
Urwid is a curses-based UI/widget library.  It includes many features useful
for console application developers, including:

- Fluid interface resizing (xterm window resizing / fbset on Linux console)
- Multiple text alignment and wrapping modes built-in
- Ability to register user-defined text alignment and wrapping modes
- Simple markup for setting text attributes
- Powerful list box that handles scrolling between different widget types
- List box contents may be managed with a user-defined class
- Flexible edit box for editing almost any type of text
- Plain HTML screen shots


Example Programs:

tour.py 
  A list box showing the built-in widget types and modes.
  
fib.py 
  A Fibonacci set viewer that demonstrates a list box with infinite data.

edit.py 
  A text editor that starts-up instantly by lazily reading files.  It is
  suitable for editing text files with lines longer than the terminal width.

browse.py 
  A directory browser that displays directories in a single tree structure.
  It reads directories as required and lets you select multiple files.

calc.py
  A calculator program that shows its work.  It splits sub-expressions
  into separate columns for easy editing.
"""[1:],
	'classifiers':[
		"Development Status :: 4 - Beta",
		"Environment :: Console",
		"Environment :: Console :: Curses",
		"Intended Audience :: Developers",
		"License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)",
		"Operating System :: POSIX",
		"Operating System :: Unix",
		"Operating System :: MacOS :: MacOS X",
		"Topic :: Software Development :: Libraries :: Python Modules",
		"Topic :: Software Development :: Widget Sets",
		],
	'packages':['urwid'],
     }

try:
	True
except:
	# python 2.1's distutils doesn't understand these:
	del setup_d['classifiers']
	del setup_d['download_url']

setup( ** setup_d )

