# Консольный файловый менеджер
import os
import shutil
import sys

while True:
    print('1. создать папку')
    print('2. удалить (файл/папку)')
    print('3. копировать (файл/папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. выход')
    choice = input('Выберите пункт меню')

    if choice=='1':
        answere=input('Введите имя папки')
        for i in range(1):
            if not os.path.exists(f'{answere}'):
                os.mkdir (f'{answere}')
                print('Создана папка', answere)

    elif choice == '2':
        answere1=input('Введите имя папки/файла для удаления')
        for i in range(1):
            if os.path.exists(f'{answere1}'):
                os.rmdir (f'{answere1}')
                print('Удалена папка/файл', answere1)

# Пункт 3 Выдает ошибку: No such file or directory: 'answere2'. Сломал мозг, но задачу не решил.
    elif choice == '3':
        answere2 = input('Введите имя копируемой папки/файла из списка')
        if os.path.exists(f'{answere2}'):
            answere3 = input('Введите имя новой папки/файла')
            shutil.copy ('answere2', 'answere3')
            print('Скопирована папка/файл', answere3)

    elif choice == '4':
        print('Cодержимое рабочей директории:', os.listdir())

    # Пункт 5 выдает ошибку
    elif choice=='5':
        dirs=[d for d in os.listdir() if os.path.lisdir(d)]
        print('Список папок:', dirs ())

    elif choice=='6':
        print('Список файлов:', os.listdir('.idea'),os.listdir('Console_file_manager'),os.listdir('venv'),os.listdir('YES'))

    elif choice == '7':
        print (sys.platform)

    elif choice == '8':
        import creator

    elif choice == '9':
        import victory

    elif choice =='10':
        import Bank_account

    elif choice == '11':
        exit()

    else:
        print('Неверный пункт меню')
        break