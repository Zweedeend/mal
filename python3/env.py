# -*- encoding: utf-8 -*-

class Env:
    def __init__(self, outer=None):
        self.data = {}
        self.outer = outer

    def set(self, key, value):
        """takes a symbol key and a mal value and adds to the data structure"""
        self.data[key] = value

    def find(self, key):
        """takes a symbol key and if the current environment contains that key then return the environment. If no key 
        is found and outer is not nil then call find (recurse) on the outer environment."""
        if key in self.data:
            return self
        if self.outer is not None:
            return self.outer.find(key)

    def get(self, key):
        """takes a symbol key and uses the find method to locate the environment with the key, then returns the
        matching value. If no key is found up the outer chain, then throws/raises a "not found" error."""
        env = self.find(key)
        if env:
            return env.data[key]
        raise KeyError(key)