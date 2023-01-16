import unittest
import requests


# Task 1
def geo(geo_logs):
    result = []
    for i in geo_logs:
        if list(i.values())[0][1] == 'Россия':
            result.append(i)
    return result


def numbers(ids):
    result = set()
    for i in ids.values():
        result.update(i)
    return result


def search_query(queries):
    words_count = {}
    for i in queries:
        lenght = len(i.split())
        if lenght in words_count.keys():
            words_count[lenght] += 1
        else:
            words_count[lenght] = 1
    for key, value in words_count.items():
        precent = round(value / len(queries) * 100, 2)
        if key == 1:
            yield f'Поисковый запрос содержит: {key} слово, процент: {precent}%'
        elif 2 <= key <= 4:
            yield f'Поисковый запрос содержит: {key} слова, процент: {precent}%'
        else:
            yield f'Поисковый запрос содержит: {key} слов, процент: {precent}%'


# Task 2
def ya_create_folder(token: str, folder: str):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    headers = {'Content-type': 'application/json', 'Accept': 'application/json', 'Authorization': f'OAuth {token}'}
    response = requests.put(f'{url}/?path={folder}', headers=headers)
    # assert response.status_code == 201, response.json()["message"]
    # return f'Папка "{folder}" создана'
    return response


class TestSomething(unittest.TestCase):
    # Task 1
    def test_geo_ru(self):
        self.assertEqual(geo([{'visit1': ['Москва', 'Россия']}]), [{'visit1': ['Москва', 'Россия']}])

    def test_numbers(self):
        test_data = {'user1': [1, 2, 3, 4], 'user2': [1, 5, 3, 6]}
        self.assertEqual(numbers(test_data), {1, 2, 3, 4, 5, 6})

    def test_search_query(self):
        queries = ['dfdf паапап вапвп ыввапв кцку34']
        self.assertEqual(list(search_query(queries)), ['Поисковый запрос содержит: 5 слов, процент: 100.0%'])

    # Task 2
    def test_ya_status(self):
        token = input('Введите Ваш токен: ')
        name_folder = input('Введите имя папки: ')
        create = ya_create_folder(token, name_folder)
        error_code = [400, 401, 403, 404, 406, 409, 413, 423, 429, 503, 507]
        self.assertNotIn(create.status_code, error_code, f'{create.json()}')
        print(f'Ответ сервера {create.status_code}')
        print(f'Папка "{name_folder}" успешно создана')


if __name__ == '__main__':
    # Task 2
    # token = input('Введите Ваш токен: ')
    # name_folder = input('Введите имя папки: ')
    # create = ya_create_folder(token, name_folder)
    # print(create)
    unittest.main()
