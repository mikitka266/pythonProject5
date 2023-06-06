'Напишите функцию, которая принимает на вход строку - абсолютный путь до файла\
Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.'


text = 'myname/writer.doc'

def make_link(text: str):
    first = text
    second = text.split('/')
    third = text.split('.')
    return first, second[1], third[1]


print(make_link(text))



