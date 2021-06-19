# Task 1

arr = [
    ["разработка", "\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430"],
    ["сокет", "\u0441\u043e\u043a\u0435\u0442"],
    ["декоратор", "\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440"]
]
for i in range(len(arr)):
    print(arr[i][0], type(arr[i][0]), arr[i][1], type(arr[i][1]), arr[i][0] == arr[i][1], sep='\t')
