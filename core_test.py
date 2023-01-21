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


def create_user(id: int, name: str, age: int):
    user = {
        'ID': id,
        'name': name,
        'age': age
    }
    user_db.append(user)
    return user_db


def delete_user(id: int):
    for index, user in enumerate(user_db):
        if user.get('ID') == id:
            user_db.remove(user)
            return user_db
    return None


def update_user(id: int, name: str):
    for user in user_db:
        if user.get('ID') == id:
            user['name'] = name
            return user
    return None


def send_message(message: str):
    return 'Your Message is + {}'.format(message)


api.add_func(get_summation, path='/', http_method='GET')
api.add_func(send_message,http_method='POST')
api.add_func(get_users)
api.add_func(get_user_by_id)
api.add_func(create_user)
api.add_func(delete_user)
api.add_func(update_user)

if __name__ == '__main__':
    simple_server(host='localhost', port=8456, application=api)

