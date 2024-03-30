def days(info):
    '''
    Описание функции days.
    Возвращает условный дату, полность переведённую в дни

    Описание аргументов
    info - тип: строка - дата в формате ДД.ММ.ГГГГ
    '''
    dtm = info[3].split('.')
    return int(dtm[0]) + int(dtm[1]) * 30 + int(dtm[2] * 365) - int(dtm[2] % 4)


with open("songs.csv", mode='r', encoding="utf-8") as doc:
    songs = doc.read().split('\n')[1:-1:]
for i in range(len(songs)):
    songs[i] = songs[i].split(";")

for t in range(len(songs)):
    cur = max(songs[t::], key=timecode)
    curid = songs.index(cur)
    songs = [cur] + songs[0:curid:] + songs[curid+1::]

for i in range(5):
    print(f"{i + 1} {songs[i][2]}, {songs[i][1]}, {songs[i][3]}")
