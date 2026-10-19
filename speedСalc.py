print('Выберете кол-во в МБ или в ГБ:', '1 - МБ', '2 - ГБ', sep='\n')
res = int(input())


while res not in (1, 2):
    print('1 или 2, #####')
    res = int(input())


if res == 1:
    mb = int(input('Сколько МБ надо конвертировать: '))
    kb = mb * 1024
    
    full_minutes = kb / 100 / 60

    if full_minutes >= 60:
        hours = int(full_minutes // 60)
        minutes = int(full_minutes % 60)
        print(f'{mb} МБ будет скачивать от {hours} часов и {minutes} минут')
    else:
        print(f'{mb} МБ будет скачивать от {full_minutes:.1f} минут')


elif res == 2:
    gb = int(input('Сколько ГБ надо конвертировать: '))
    kb = gb * 1024 * 1024

    full_minutes = kb / 100 / 60

    hours = int(full_minutes // 60)
    minutes = int(full_minutes % 60)

    print(f'{gb} ГБ будет скачивать от {hours} часов и {minutes} минут')