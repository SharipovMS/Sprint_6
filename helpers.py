import random


def name():
    name_list = ['Иван', 'Алексей', 'Матвей']
    return random.choice(name_list)

def second_name():
    second_name_list = ['Иванов', 'Петров', 'Сидоров']
    return random.choice(second_name_list)

def address():
    address_street = ['улица Красного знамени, 24', 'улица Уставшего студента, 99', 'улица Как же я устал, 1']
    return random.choice(address_street)

def phone_number():
    return random.randint(89000000000, 89999999999)
