import os

os.system('')


def memo(func):
    def cache_wrapper(self, *args, **kwargs):
        key = args[0]
        self.cache[key] = self[key]
        r = func(self, *args, **kwargs)
        if (key, self[key]) in self.cache.items():
            self.cache.pop(key)
        return r

    return cache_wrapper


class cachelist(list):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cache = {}

    @memo
    def __setitem__(self, key, value):
        return super().__setitem__(key, value)

    def copy(self):
        return cachelist(super().copy())

    def __str__(self):
        tmp = []
        for index, value in enumerate(self):
            if index not in self.cache.keys():
                tmp.append(str(value))
            else:
                tmp.append(f'\033[1;31m{value}\033[0m')
        s = '[' +  ', '.join(tmp) + ']'
        self.cache = {}
        return s
