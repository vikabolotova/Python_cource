def abbrvt_stroka(stroka):
    abbrvt = []
    if type(stroka) == str:
        stroka_1 = stroka.upper().split()
        print(stroka_1)
        #stroka_1 = stroka.split()
        for i in range(len(stroka_1)):
            abbrvt.append(stroka_1[i][0])
        print(''.join(abbrvt))

    else:
        print("На вход функция должна получать только строковые переменные")


abbrvt_stroka('федеральное государственное автономное образовательное учреждение')