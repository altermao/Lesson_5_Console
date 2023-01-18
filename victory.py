# Викторина "Годы рождения знаменитых рок-гитаристов" (данные получены их Википедии)
print ('Внимание ! Проверьте Ваши знания. Укажите правильные годы рождения знаменитых рок-гитаристов')
user_y = 0
user_n = 0
#Год рождения Джимми Хендрикса - 1942
answer1 = int(input(' Год рождения Джимми Хендрикса ? : '))
if answer1 == 1942:
    print ('Верно')
    user_y += 1
else:
    print('Неверно')
    user_n += 1
#Год рождения Карлоса Сантаны - 1947
answer2 = int(input(' Карлос Сантана (Santana) ? : '))
if answer2 == 1947:
    print ('Верно')
    user_y += 1
else:
    print('Неверно')
    user_n += 1
#Год рождения Риччи Блэкмора - 1945
answer3 = int(input(' Риччи Блэкмор (Deep Purple, Rainbow, Blackmore`s Night) ? : '))
if answer3 == 1945:
    print ('Верно')
    user_y += 1
else:
    print('Неверно')
    user_n += 1
#Год рождения Эорика Клэптона - 1945
answer4 = int(input(' Эрик Клэптон ? : '))
if answer4 == 1945:
    print ('Верно')
    user_y += 1
else:
    print('Неверно')
    user_n += 1
#Год рождения Марка Нопфлера - 1949
answer5 = int(input(' Марк Нопфлер (Dire Straits) ? : '))
if answer5 == 1949:
    print ('Верно')
    user_y += 1
else:
    print('Неверно')
    user_n += 1
#Год рождения Рэнди Роадса - 1956
answer6 = int(input(' Рэнди Роадс (Ozzy Ozborn) ? : '))
if answer6 == 1956:
    print ('Верно')
    user_y += 1
else:
    print('Неверно')
    user_n += 1
#Год рождения Брайана Мэя - 1947
answer7 = int(input(' Брайан Мэй (Queen) ? : '))
if answer7 == 1947:
    print ('Верно')
    user_y += 1
else:
    print('Неверно')
    user_n += 1

print('Количество верных ответов: ' + str(user_y))
print('Количество неверных ответов: ' + str(user_n))

print('Процент верных ответов: ' + str(user_y*100/7))
print('Процент неверных ответов: ' + str(user_n*100/7))

print('До новых встреч !')

exit()
