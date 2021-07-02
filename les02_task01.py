import csv
import re


def get_data(file_list):
    os_prod_list, os_name_list, os_code_list, os_type_list = [], [], [], []
    tl = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы']
    main_data_list = [tl]
    for file in file_list:
        summary = {}
        with open(file, encoding="utf-8") as f:
            for row in f:
                if re.findall(f"{tl[0]}:\s+|{tl[1]}:\s+|{tl[2]}:\s+|{tl[3]}:\s+", row):     # Тут колхоз. Но проще
                    row1 = re.findall('([\w\s]+):\s+([\w\s-]+)', row.strip())               # не нашел инструмента
                    summary[row1[0][0]] = row1[0][1]
        # os_prod_list.append(summary[tl[0]])   # Закомментировал. В задании об этом есть, но не используется
        # os_name_list.append(summary[tl[1]])   # далее в коде.
        # os_code_list.append(summary[tl[2]])
        # os_type_list.append(summary[tl[3]])
        main_data_list.append([summary[tl[0]], summary[tl[1]], summary[tl[2]], summary[tl[3]]])
    with open('main_data.csv', 'w', encoding='utf-8', newline='') as f_n:
        f_n_writer = csv.writer(f_n)
        for el in main_data_list:
            f_n_writer.writerow(el)


f_list = ["info_1.txt", "info_2.txt", "info_3.txt"]
get_data(f_list)
