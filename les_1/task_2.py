user_time = int(input('Введите время в секундах: '))
if user_time < 60:
    if user_time < 10:
        print(f'00:00:0{user_time}')
    else:
        print(f'00:00:{user_time}')
elif 60 <= user_time < 3600:
    min = user_time // 60
    if min < 10:
        min = str(0) + str(min)
    sec = user_time % 60
    if sec < 10:
        sec = str(0) + str(sec)
    print(f'00:{min}:{sec}')
elif user_time >= 3600:
    hour = user_time // 3600
    if hour < 10:
        hour = str(0) + str(hour)
    min_2 = (user_time % 3600) // 60
    if min_2 < 10:
        min_2 = str(0) + str(min_2)
    sec_2 = (user_time % 3600) % 60
    if sec_2 < 10:
        sec_2 = str(0) + str(sec_2)
    print(f'{hour}:{min_2}:{sec_2}')
