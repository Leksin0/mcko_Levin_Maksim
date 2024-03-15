with open('game.txt', encoding='utf-8') as doc:
    '''
    Чтение файла входных данных и создание массива данных
    '''
    errors = doc.read().split('\n')[1::]
    for i in range(len(errors)):
        errors[i] = errors[i].split('$')

fixed = open("game_new.csv", 'w', encoding="utf-8")
report = open("report.txt", 'w', encoding="utf-8")
fixed.write('GameName$characters$nameError$date\n')
'''
Создание файлов выходных данных
'''
for err in errors:
    if '55' in err[2]:
        '''
        Поиск ошибок, удовлетворяющих условию задачи и запись их в файл отчёта
        '''
        report.write(f"У персонажа\t{err[1]}\tв игре\t{err[0]}\t" +
                     f"нашлась ошибка с кодом:\t {err[2]}.\tДата фиксации:\t {err[3]}\n")
        fixed.write(f"{err[0]}${err[1]}$Done$0000-00-00\n")
    else:
        fixed.write(f"{err[0]}${err[1]}${err[2]}${err[3]}\n")
fixed.close()
report.close()
