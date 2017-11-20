#!/usr/bin/python
#vim: set fileencoding:utf-8

def add_end(L=[]):
    L.append('END')
    return L

print add_end([1, 2])
print add_end(["x", 7])
print add_end()
print add_end()