# Task 5
# Вариант с кодировкой cp866, тестировался под Win10 RUS

import subprocess


def sub_proc_ping(url):
    args = ['ping', url]
    subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)
    for line in subproc_ping.stdout:
        line = line.decode('cp866').encode('utf-8')
        print(line.decode('utf-8'))


sub_proc_ping('yandex.ru')
sub_proc_ping('youtube.com')
