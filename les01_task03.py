# Task 3
try:
    var1 = b"attribute"
    var2 = b"type"
except SyntaxError:
    print("bytes can only contain ASCII literal characters.")
print(var1, var2)

# В байтовом типе в Python могут быть представлены только сивмолы, представленные в ASCII.
# Попытка реализовать код, демонстрирующий невозможность преобразования кириллицы не удалась:
# Все три представленные ниже варианта приводили к стандартной
# ошибке SyntaxError: bytes can only contain ASCII literal characters.

# -------- Exmpl 1 ------------
# if (b'класс'):
#     # print(var1, type(var1))
# else:
#     print("Error. Not ASCI symbol.")

# -------- Exmpl 2 ------------
# try:
#     b'класс'
# except SyntaxError:
#     print("Ups..")

# -------- Exmpl 2 ------------
# try:
#     b'класс'
# except UnicodeDecodeError:
#     print("Ups..")
