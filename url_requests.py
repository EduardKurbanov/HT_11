import requests
import random

BASE_URL = "https://jsonplaceholder.typicode.com"


def get_requests_id():
    url = 'https://jsonplaceholder.typicode.com/users'
    rec = requests.get(url)
    rec_data: dict = rec.json()
    return rec_data


def get_requests_user_info_by_id(user_id):
    rec = requests.get(BASE_URL + f"/users?id={user_id}")
    rec_data: dict = rec.json()
    return rec_data


def get_requests_post_by_user_id(user_id):
    rec = requests.get(BASE_URL + f"/posts?userId={user_id}")
    rec_data: dict = rec.json()
    return rec_data


def get_requests_post_by_post_id(post_id):
    rec = requests.get(BASE_URL + f"/posts?id={post_id}")
    rec_data: dict = rec.json()
    return rec_data


def get_requests_post_comments_by_post_id(post_id):
    rec = requests.get(BASE_URL + f"/comments?postId={post_id}")
    rec_data: dict = rec.json()
    return rec_data


def get_requests_random_photo():
    rec = requests.get(BASE_URL + f"/photos")
    rec_data: dict = rec.json()
    random_value = random.randint(0, len(rec_data))
    rec = requests.get(BASE_URL + f"/photos?id={random_value}")
    rec_data: dict = rec.json()
    for i in rec_data:
        print(f'url: {i["url"]}')

def get_requests_todos_by_user_id(user_id,is_arg=True):
    url = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}&completed={str(is_arg).lower()}'
    rec = requests.get(url)
    rec_data: dict = rec.json()
    return rec_data

