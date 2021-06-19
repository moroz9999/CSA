# Task 4
arr2 = ["разработка", "администрирование", "protocol", "standard"]
for i in range(len(arr2)):
    x_enc = arr2[i].encode('utf-8')
    x_dec = x_enc.decode('utf-8')
    print(x_enc, x_dec)
