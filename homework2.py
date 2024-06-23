task = 'Практическое задание по работе в Pycharm - "Переменные".'
avtor = 'Студент Крылов Эдуард Васильевич'
thanks = 'Благодарю за внимание :-)'
print()
print(task)
print(avtor)
print()
print('Введите название курса:')
kurs_name = str(input())
print('Введите колисество пройденных курсов:')
quanity_dz = int(input())
print('Введите количество портаченных часов:')
quanity_hours = float(input())
quanity_minuten = int(quanity_hours * 60)
print('Кол-во выполненных ДЗ в переменной - quanity_dz =', quanity_dz)
print('Количество затраченных часов в переменной - quanity_hours =', quanity_hours)

print('Название курса в переменной - kurs_name =', kurs_name)
timeOneTask = (((quanity_hours * 60) / quanity_dz) / 60)
print('Потрачено на обучение -', quanity_minuten, 'минут')
print('Расчет среднего времени выполнения - timeOneTask = (((quanity_hours * 60) / quanity_dz) / 60) =',timeOneTask)
if timeOneTask == 1.0:
    h = ' '
else:
    h = 'а'
print()
print('На курс', kurs_name, 'состоящего из', quanity_dz, 'заданий, было потрачено часов -', quanity_hours,', среднее время выполнения -', timeOneTask, 'час' + h +'.')
print()
print(thanks)