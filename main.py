# Бот спрашивает имя собеседника
# Бот говорит о погоде
# Бот задает вопросы
# Бот реагирует на сообщения пользователя
# Бот общается на тематику компьютерных игр

from random import choices
from time import sleep

rand_users = choices(['Андрей Сухов', "Васька Пупкин", 'Михаил Державин'])

print(f'{rand_users[0]}: --> Привет. Давай знакомиться')
sleep(1.5) 
print(f'{rand_users[0]}: --> Меня зовут {rand_users[0]}, я из Таллина мне 17 лет.')
sleep(2)
name = input(f'{rand_users[0]}: --> Как тебя зовут? ')
sleep(2)
city = input(f'{rand_users[0]}: --> Из какого ты города, {name}? ')
sleep(2)
print(f'{rand_users[0]}: --> В городе {city} сегодня хорошая погода? ')
pogoda = input()
if  'солнечно' in pogoda:
  sleep(3)
  print(f'{rand_users[0]}: Обожаю солнце! Я бы пошел купаться, ведь лето же.')
if 'пасмурно' in pogoda:
  sleep(3)
  print(f'{rand_users[0]}: Некоторые любят такую погоду. Тёплый плед и горячий чай...у камина...')
else:
  sleep(2)
  print(f'{rand_users[0]}: Чтож! Одни любят когда солнечно,другие когда пасмурно. Всем не угодишь =))')
sleep(1)
game = input(f'{rand_users[0]}:Слушай, а какая у тебя самая любимая игра на компе?' )
sleep(2)

print(f'{rand_users[0]}: {game} да клевая игрушка, я играл в нее недавно, перепроходил')
sleep(1.5)
print(f'{rand_users[0]}: Мне вообще нравятся подобные жанры')
sleep(1)
print(f'{rand_users[0]}: Я обожаю стратегии, люблю гонки погонять, онлайн mmorpg тоже нравятся, но они занимают много времени, а так жаль....')
sleep(2)
nfs= input(f'{rand_users[0]}: А как тебе последний Need for Speed? ' )
if 'супер' in nfs:
  print(f'{rand_users[0]}: рад что тебе поже нравится эта часть. Графон супер!')
if 'неочень' in nfs:
  print(f'{rand_users[0]}: Жаль что тебе не понравилась =(')
else:
  print(f'{rand_users[0]}: всегда так) кому-то нравится, кому-то нет. Но все равно раньше игры лучше делали!')

sleep(1.4)
print(f'{rand_users[0]}: слушай, мне пора на тренировку, потом спишемся еще =)) ')
sleep(1.5)
print(f'{rand_users[0]}: До встречи {name}, всего тебе доброго =)')
