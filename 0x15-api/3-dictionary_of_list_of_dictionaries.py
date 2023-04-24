#!/usr/bin/python3
'''A script that, uses a REST API, for a given employee ID,returns
information about his/her TODO list progress.
Usage:
   ./0-gather_data_from_an_API.py <id>
Author:
    Abdulsalam Abdulsomad .A. - April 24th, 2023.
'''
import json
import requests



API = "https://jsonplaceholder.typicode.com"
if __name__ == '__main__':
    users_res = requests.get('{}/users'.format(API)).json()
    todos_res = requests.get('{}/todos'.format(API)).json()
    users_data = {}
    for user in users_res:
        id = user.get('id')
        user_name = user.get('username')
        todos = list(filter(lambda x: x.get('userId') == id, todos_res))
        user_data = list(map(
            lambda x: {
                'username': user_name,
                'task': x.get('title'),
                'completed': x.get('completed')
            },
            todos
        ))
        users_data['{}'.format(id)] = user_data
    with open('todo_all_employees.json', 'w') as file:
        json.dump(users_data, file)
