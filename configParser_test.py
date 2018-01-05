# -*- coding: utf-8 -*-
import ConfigParser
import string

config = ConfigParser.ConfigParser()
config.read('example.ini')
print config.get("book", "title")
print string.upper(config.get("book", "title")),
print "by", config.get("book", "author"),
print "(" + config.get("book", "email") + ")"
print
print config.get("size", "size")
print
print config.sections()
print config.options('book')

for sections in config.sections():
    for options in config.options(sections):
        print "" + options + "=" + config.get(sections, options)
