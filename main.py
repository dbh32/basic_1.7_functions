documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def search_name():
    '''Ищет человека по номеру документа'''
    number_input = input('Номер документа: ')
    for doc_search in documents:
        if number_input in doc_search.values():
            print(doc_search['name'])


def show_all_docs():
    '''Выводит перечень всех доментов'''
    for doc_search in documents:
        print('{}: "{}" "{}"'
            .format(
            doc_search['type'],
            doc_search['number'],
            doc_search['name']
        )
        )


def search_shelf():
    '''Ищет полку по номеру документа'''
    number_input = input('Номер документа: ')
    for shelf, doc in directories.items():
        if number_input in doc:
            print(shelf)


def add_doc():
    '''Добавляет новый документа в каталог и на полку'''
    type_input = input('Тип документа: ')
    number_input = input('Номер документа: ')
    name_input = input('Кому принадлежит: ')
    shelf_input = input('Куда кладём: ')

    new_doc = {
        'type': type_input,
        'number': number_input,
        'name': name_input
    }
    documents.append(new_doc)

    for shelf, doc in directories.items():
        if shelf_input in shelf:
            doc.append(number_input)
        else:
            pass


def del_doc():
    '''Удаляет документ по номеру'''
    number_input = input('Номер документа: ')
    for doc_search in documents:
        if number_input in doc_search.values():
            dict.clear(doc_search)
    documents.remove({})


def move_doc():
    '''Перемещает документ на выбранную полку'''
    number_input = input('Номер документа: ')
    shelf_input = input('Куда перекладываем: ')

    for shelf, doc in directories.items():
        if number_input in doc:
            doc.remove(number_input)
        else:
            pass

        if shelf_input in shelf:
            doc.append(number_input)
        else:
            pass


def create_shelf():
    '''Спрашивает номер новой полки и создаёт её в перечне'''
    new_shelf_input = input('Идентификатор новой полки: ')

    dir_it = directories.copy()
    # Будем итерироваться по копии, чтобы поменять тело списка
    for shelf, doc in dir_it.items():
        if new_shelf_input not in shelf:
            directories[new_shelf_input] = []
        else:
            pass


def main():
    print('p - найти человека по номеру документа')
    print('l - вывести список всех документов')
    print('s - показать, где хранится документ')
    print('a - добавить новый документ')
    print('d - удалить документ')
    print('m - переместить документ на другую полку')
    print('as - добавить новую полку в перечень')
    print('q - выход')
    while True:
        print()
        user_input = input('Введите команду: ')
        if user_input == 'p':
            search_name()
        elif user_input == 'l':
            show_all_docs()
        elif user_input == 's':
            search_shelf()
        elif user_input == 'a':
            add_doc()
        elif user_input == 'd':
            del_doc()
        elif user_input == 'm':
            move_doc()
        elif user_input == 'as':
            create_shelf()
        elif user_input == 'q':
            print('До свидания!')
            break


if __name__ == "__main__":
    main()
