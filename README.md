Minipie
=======

Minify Javascript and CSS with Sublimetext 2.

What's this?
============

Basically, a thin wrapper around two existing Python libraries. I made it because other plugins required the Java runtime or a connection to Google Apps, and all I wanted was something fast and simple that used only Python. So, that's what Minipie is.

How does it work?
=================

Simply select the Minipie command from the Command Palette, for files having the `.js` or `.css` extension. Minipie writes a file with a `.min.js` or `.min.css` extension to the file's directory.

Who made this?
==============

Minipie borrows heavily from Bistory's [Minifier plugin](https://github.com/bistory/Sublime-Minifier).

Minipie comes with two libraries:

[CSSMin](https://github.com/zacharyvoase/cssmin)
[RJSMin](http://opensource.perlig.de/rjsmin/)

They, in turn, are based on the YUI Compressor and Douglas Crockfords jsmin.c

Should you backup your files before minifying?
==============================================

Probably, yes.

