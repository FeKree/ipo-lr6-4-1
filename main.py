gstr = 0 #Переменная для подсчета строк содержащих букву г
str = ['почему', 'светофор', 'бегут', 'светит', 'огней', 'погоди'] #Строки в которых есть или нет буква г
for i in str: #Используем цикл для подсчета 
    if 'г' in i: #Ветвление в котором мы определяем есть ли в строке буква г
        gstr += 1 #Если в 4 строке условие истинно то к переменной для подсчета кол-ва строк добавляем 1 
print(f"Буква г присутствовала в {gstr} строках") #Выводим в скольких строках есть буква г