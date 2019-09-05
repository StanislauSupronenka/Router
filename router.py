#! usr/lib/python3
# coding:utf-8

METHODS = ['PUT', 'GET', 'DELETE', 'POST', 'UPDATE', 'OPTIONS']

class Router:

    def __init__(self):
        self.paths = {}

    def __getattr__(self, attr):
        if attr in METHODS:
            return lambda path: self.request(attr, path)
        raise AttributeError

    def add_path(self, path, method, function):
        if path in self.paths.keys():
            return 'Already exist'
        else:
            self.paths[path] = [method, function]
            return 'Complete'

    def request(self, method, path):
        if path not in self.paths.keys():
            return 404, 'Error 404: Not Found'

        elif method not in self.paths[path]:
            return 405, 'Error 405: Method Not Allowed'
        else:
            func = self.paths[path][1]
            print(self.paths[path][1])
            return func(path, method)


def my_info(path, method):
    return 200, {'me': 'Joanne'}


def update_me(path, method):
    return 200, 'OK'

