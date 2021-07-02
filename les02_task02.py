# Создать функцию write_order_to_json(), в которую передается 5 параметров —
# товар (item), количество (quantity), цена (price), покупатель (buyer), дата (date).
# Функция должна предусматривать запись данных в виде словаря в файл orders.json.
# При записи данных указать величину отступа в 4 пробельных символа;
import json


def get_data_for_json():
    item = input("Товар: ")
    quantity = int(input("Количество: "))
    price = float(input("Цена: "))
    buyer = input("Покупатель: ")
    date = input("Дата: ")
    data_for_json = {
        "item": item,
        "quantity": quantity,
        "price": f"{price:.2f}",
        "buyer": buyer,
        "date": date
    }
    return data_for_json


def append_json(new_json_objects):
    with open('orders.json') as json_file:
        json_objects = json.load(json_file)
    json_objects["orders"].append(new_json_objects)
    with open('orders.json', 'w', encoding='utf-8') as json_file:   # Русский шрифт при тестах кодируется :(
        json.dump(json_objects, json_file, indent=4)


append_json(get_data_for_json())
