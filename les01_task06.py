# Task 6

file = open("enc_test.txt", "w")
file.write("сетевое программирование\nсокет\nдекоратор")
file.close()
print(file)
with open("enc_test.txt", encoding='utf-8') as enc_f:      # Если принудительно указать UTF-8, то
    for el_str in enc_f:                                    # будет ошибка, поскольку в open указана
        print(el_str, end='')                               # несоответствующая файлу кодировка:
                                                            # UnicodeDecodeError (если он был создн в cp1251)
