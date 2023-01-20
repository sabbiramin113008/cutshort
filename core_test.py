# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 14 Jan 2023
email: sabbir.amin@goava.com, sabbiramin.cse11ruet@gmail.com

"""
from core import API
from werkzeug.serving import run_simple

app = API()


def summation(a: int, b: int):
    return a + b


app.add_func(path='/', handler_func=summation, http_method='COSY')

if __name__ == '__main__':
    run_simple(
        hostname='localhost',
        port=8456,
        application=app
    )
