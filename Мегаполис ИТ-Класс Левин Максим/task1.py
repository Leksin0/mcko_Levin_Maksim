def delta(date):
    '''
    Описание функции delta.
    Возвращает разницу в днях между 12.05.2023 и датой в аргументе date

    Описание аргументов
    date - тип: строка - дата в формате ДД.ММ.ГГГГ
    '''
    date = date.split('.')
    d = (2023 - int(date[2])) * 365 + (2023 - int(date[2])) % 4
    d += (5 - int(date[1])) * 30
    d += 12 - int(date[0])
    return d

with open("songs.csv", mode='r', encoding="utf-8") as doc:
    songs = doc.read().split('\n')[1:-1:]

with open("songs_new.csv", mode='w', encoding="utf-8") as rep:
    for song in songs:
        info = song.split(';')
        if int(info[3][6::]) < 2002 or info[3] == "01.01.2002":
            if info[0] == 0:
                info[0] = abs(delta(info[3])/(len(info[1])-len(info[2]))) * 10000
            rep.write(f"{info[2]} - {info[1]} - {info[0]}\n")
