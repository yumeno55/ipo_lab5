import json

import requests


def get_response():
    num = int(input())
    global response
    url = "http://localhost:8080"
    match num:
        case 1:
            text = input("Введите текст заметки: ")
            token = input("Введите токен: ")
            response = requests.post(url + "/create_note", params={"text": text, "token": token})
        case 2:
            id = int(input("Введите id заметки: "))
            token = input("Введите токен: ")
            response = requests.get(url + "/read_note", params={"id": id, "token": token})
        case 3:
            id = int(input("Введите id заметки: "))
            token = input("Введите токен: ")
            response = requests.get(url + "/get_time_info", params={"id": id, "token": token})
        case 4:
            id = int(input("Введите id заметки: "))
            text = input("Введите текст заметки: ")
            token = input("Введите токен: ")
            response = requests.put(url + "/update_note", params={"id": id, "text": text, "token": token})
        case 5:
            id = int(input("Введите id заметки: "))
            token = input("Введите токен: ")
            response = requests.delete(url + "/delete_note", params={"id": id, "token": token})
        case 6:
            token = input("Введите токен: ")
            response = requests.get(url + "/id_list", params={"token": token})

    print(f"Status code: {response.status_code}")
    print(f"Response body: {response.text}")


if __name__ == '__main__':
    get_response()
