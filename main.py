print('Українська CAPTCHA')
print('Щоб пройти далі потрібно відповісти на декілька запитаннь')
flag = True
temp = input('Як українською буде "Каравай": ')
if temp.lower()[:8] == 'паляниця':
    print('Це дійсно "Паляниця"')
else: flag = False
if flag == True:
    temp = input('Як українською буде "Клубника": ')
    if temp.lower()[:8] == 'полуниця':
        print('Звісно це "Полуниця"')
    else: flag = False
if flag == True:
    temp = input('Слава Україні: ')
    if temp.lower()[:12] == 'героям слава':
        print('Видно, що ти - не москаль. Проходь')
    else: flag = False
if flag == False: print('Смерть ворогам!!!')
