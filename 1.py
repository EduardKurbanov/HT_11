"""
Сайт для виконання завдання: https://jsonplaceholder.typicode.com

Написати програму, яка буде робити наступне:
1. Робить запрос на https://jsonplaceholder.typicode.com/users і вертає коротку інформацію про користувачів (ID, ім'я, нікнейм)
2. Запропонувати обрати користувача (ввести ID)
3. Розробити наступну менюшку (із вкладеними пунктами):
   1. Повна інформація про користувача
   2. Пости:
      - перелік постів користувача (ID та заголовок)
      - інформація про конкретний пост (ID, заголовок, текст, кількість коментарів + перелік їхніх ID)
   3. ТУДУшка:
      - список невиконаних задач
      - список виконаних задач
   4. Вивести URL рандомної картинки
"""

from url_requests import get_requests_id, get_user_info_by_id, get_post_by_post_id, get_post_by_user_id, \
    get_post_comments_by_post_id, get_requests_todos_by_user_id, get_requests_random_photo


def get_users_list():
    print("*" * 30)
    print(f" id   name      nikname")
    print("*" * 30)

    for i in get_requests_id():
        print(f'{i["id"]:3}  {str(i["name"]).split()[0]:10}  {i["username"]}.')
    print("*" * 30)


def get_short_user_info_by_id(user_id):
    for i in get_user_info_by_id(user_id):
        return f'id: {i["id"]},\n' \
               f'name: {i["name"]},\n' \
               f'username: {i["username"]}\n'


def full_inf_user(user_id):
    pars: str = None

    for i in get_user_info_by_id(user_id):
        pars = f'id user: {i["id"]}\n' \
               f'name: {i["name"]}\n' \
               f'nikname: {i["username"]}\n' \
               f'email: {i["email"]}\n' \
               f'<address>\n' \
               f'street: {i["address"]["street"]}\n' \
               f'suite: {i["address"]["suite"]}\n' \
               f'city: {i["address"]["city"]}\n' \
               f'zipcode: {i["address"]["zipcode"]}\n' \
               f'<geolocation>\n' \
               f'latitude: {i["address"]["geo"]["lat"]}\n' \
               f'longitude: {i["address"]["geo"]["lng"]}\n' \
               f'phone: {i["phone"]}\n' \
               f'website: {i["website"]}\n' \
               f'<company>\n' \
               f'name: {i["company"]["name"]}\n' \
               f'catchPhrase: {i["company"]["catchPhrase"]}\n' \
               f'bs: {i["company"]["bs"]}'

    print(pars)


def get_post_user(user_id):
    pars: str = None

    for i in get_post_by_user_id(user_id):
        pars = f'Post ID: {i["id"]}, title: {i["title"]}'
    print(pars)


def get_user_post_id_range(user_id):
    post_id_list: list = []

    for i in get_post_by_user_id(user_id):
        post_id_list.append(i["id"])

    return int(min(post_id_list)), int(max(post_id_list))


def get_post_info_by_post_id(post_id):
    pars: str = None
    comment_id_list: list = []
    comments_list: dict = get_post_comments_by_post_id(post_id)
    comments_num: int = len(comments_list)

    for i in comments_list:
        comment_id_list.append(i["id"])

    for i in get_post_by_post_id(post_id):
        pars = f'Post ID: {i["id"]},\n' \
               f'title: {i["title"]},\n' \
               f'{">" * 30}\n' \
               f'body: {i["body"]},\n' \
               f'{">" * 30}\n' \
               f'comments num: {comments_num},\n' \
               f'comments list: {comment_id_list}'

    print(pars)


def get_todos(user_id, is_arg=True):
    if is_arg == False:
        print("*" * 50)
        print("list of non-specific tasks: ")
        for i in get_requests_todos_by_user_id(user_id, False):
            pars = f'id: {i["id"]}, title: {i["title"]}'
            print(pars)

    elif is_arg == True:
        print("*" * 50)
        print("list of tasks: ")
        for i in get_requests_todos_by_user_id(user_id):
            pars = f'id: {i["id"]}, title: {i["title"]}'
            print(pars)


def consol_menu():
    while True:
        try:
            if input("want to continue y/n: ").lower() == "y":
                get_users_list()

                in_id = input("enter the number id -> ")
                if int(in_id) in range(len(get_requests_id()) + 1):
                    get_short_user_info_by_id(in_id)

                else:
                    print(f"<< incorrect id - > {in_id} >>")
                    continue

            else:
                exit()

            while True:
                print("*" * 50)
                in_namb = input("1. Information about koristuvach\n"
                                "2. Post.\n"
                                "3. Todos\n"
                                "4. Enter URL of a random image\n"
                                "5. Exit.\n"
                                "choose -> ")
                print("*" * 30)
                if int(in_namb) == 1:
                    full_inf_user(in_id)

                elif int(in_namb) == 2:
                    get_post_info_by_post_id(in_id)

                elif int(in_namb) == 3:
                    get_todos(in_id, False)
                    get_todos(in_id)

                elif int(in_namb) == 4:
                    print("random url:")
                    get_requests_random_photo()

                elif int(in_namb) == 5:
                    consol_menu()

        except Exception as err:
            print(f"incorrect input -> {err}")


if __name__ in "__main__":
    consol_menu()
