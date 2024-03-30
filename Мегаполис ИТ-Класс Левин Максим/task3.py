with open("songs.csv", mode='r', encoding="utf-8") as doc:
    songs = doc.read().split('\n')[1:-1:]
for i in range(len(songs)):
    songs[i] = songs[i].split(";")

name = input("Песню какого исполнителя Вы хотите найти?  ")
while name != '0':
    found = False
    for song in songs:
        if song[1] == name:
            found = True
            info = song[2]
            break
    if found:
        print(f"У {name} найдена песня: {info}")
    else:
        print("К сожалению, ничего не удалось найти")
    name = input("Песню какого исполнителя Вы хотите найти?  ")

