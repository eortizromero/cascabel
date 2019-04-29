# -*- coding: utf-8 -*-

__all__ = [
    'Meta'
]

INHERITED_ATTRS = ('_returns',)

class Meta(type):
    def __new__(meta, name, bases, attrs):
        parent = type.__new__(meta, name, bases, {})
        for key, value in list(attrs.items()):
            #print("key: %s, value: %s" % (key, callable(value)))
            if not key.startswith('__') and callable(value):
                value = propagate(getattr(parent, key, None), value)
                print(value)
                # TODO: check if funct has attr for api or reestruct funct then set attrs by value
        #print("cls %s, name %s, base %s, attrs %s " % (cls, name, bases, attrs))
        return type.__new__(meta, name, bases, attrs)

def propagate(method1, method2):
    if method1:
        for attr in INHERITED_ATTRS:
            if hasattr(method1, attr) and not hasattr(method2, attr):
                setattr(method2, attr, getattr(method1, attr))
    return method2


def multi(method):
    method._api = 'multi'
    return method
