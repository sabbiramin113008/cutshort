# -*- coding: utf-8 -*-

"""
author: S.M. Sabbir Amin
date: 14 Jan 2023
email: sabbir.amin@goava.com, sabbiramin.cse11ruet@gmail.com

"""
from cutshort import API, simple_server

api = API()

user_db = [
    {'ID': 1, 'name': 'John Doe', 'age': 21},
    {'ID': 2, 'name': 'Jane Doe', 'age': 23}]


def get_summation(a: int, b: int):
    return a + b


def get_users():
    resp = {
        'users': user_db
    }
    return resp


def get_user_by_id(user_id: int):
    for user in user_db:
        if user.get('ID') == user_id:
            resp = {
                'user': user
            }
            return resp
    return None


def send_message(message: str):
    return 'Your Message is + {}'.format(message)


api.add_func(get_summation, path='/')
api.add_func(send_message)
api.add_func(get_users)
api.add_func(get_user_by_id)

if __name__ == '__main__':
    simple_server(host='localhost', port=8456, application=api)
