import os
import psutil
import sys
import shutil

def duplicate_file(filename):
    if os.path.isfile(filename):
        newfile = filename + '.dupl'
        shutil.copy(filename, newfile)
        if os.path.exists(newfile):
            print("Файл", newfile, "был успешно создан")
            return True
        else:
            print("ERROR")
            return False
def del_dublicats(dirname):
        file_list = os.listdir(dirname)
        doble_count = 0

        for f in file_list:
            fullname = os.path.join(dirname, f)
            if fullname.endswith('.dupl'):
                 os.remove(fullname)
                 if not os.path.exists(fullname):
                      doble_count += 1
                      print("файл", fullname, "был успешно удален")
        return doble_count

def sys_info():
    print("Количество процессоров: ", psutil.cpu_count())
    print("Платформа:", sys.platform)
    print("Кодировка файловой системы: ", sys.getdefaultencoding())
    print("Текущая директория: ", os.getcwd())
    print("Текущий пользователь: ", os.getlogin())
    print("Свободное место на диске: ", psutil.disk_usage('/'))
    print("Пользователи в системе:", psutil.users())
    return 0


input("username:")
input("root@192.168.3.52's password:")

print("Connection established. To escape to local shej ll, press 'Ctrl+Alt+]'")
answer = ''
while answer != 'no':
    answer = input("Are you sure you want to continue connecting (yes/no)?")
    if answer == 'yes':
        print("Welcom to Ubuntu 16.04.5 LTS")
        print("Bitrix virtual appliance version 7.3.3")
        print("Pool Configuration manager on this host")
        print("1.  Списек файлов вывести")
        print("2.  Вывести информацию о системе")
        print("3.  Вывести списек процессов")
        print("4.  Дублирование файлов в текущей директори: ")
        print("5.  Дублирование указанный файлов")
        print("6.  Удалить дублекаты ")
        do = int(input("Plesse number:"))
        if do == 1:
            print(os.listdir())
        elif do == 2:
            sys_info()

        elif do == 3:
            print(psutil.pids())
        elif do == 4:
            print("Дублирование файлов в текушей директории")
            file_list = os.listdir()
            i = 0
            while i < len(file_list):
                duplicate_file(file_list[i])
                i += 1
        elif do == 5:
            print("Дублирование файлов в текушей директории")
            filename = input("Укажите имя файла:")
            duplicate_file(filename)
        elif do == 6:
            print("Удаление дубликатов файлов в текушей директории")
            dirname = input("Укажите имя файла:")
            count = del_dublicats(dirname)
            print("-- Удалено файлов: ", count)

        else:
            pass

    elif answer == 'no':
        print("Close sesion")
    else:
        print("Authentication failed.")

    input("Конец программы")
