DEF = int(input("podaj def: "))
ATT_WL = int(input("ataki WL: "))
ATT_FW = int(input("ataki FW: "))
ATT_SM = int(input("ataki SM: "))
REFLEX = int(input("Reflexy >> 1; Distracting >> -1; nic >> 0: "))


# OFF, STR
WL = [5, 6]
FW = [5, 4]
SM = [6, 5]

if WL[0] > DEF:
    test_WL = ATT_WL * 2 / 3
else:
    test_WL = ATT_WL * 1 / 2

if FW[0] > DEF:
    test_FW = ATT_FW * (2 / 3 + (REFLEX*1/6))
else:
    test_FW = ATT_FW * (1 / 2 + (REFLEX*1/6))

if SM[0] > DEF:
    test_SM = ATT_SM * (2 / 3 + (REFLEX*1/6))
else:
    test_SM = ATT_SM * (1 / 2 + (REFLEX*1/6))

TAB = [round(test_WL, 1), round(test_FW, 1), round(test_SM, 1)]
print("---------------------WL,   FW,   SM")
print(f"---------trafienia: {TAB}")

#  test2
for RES in range(3, 7):
    if WL[1] - RES >= 2:
        test2_WL = test_WL * 5 / 6
    elif 2 > WL[1] - RES >= 1:
        test2_WL = test_WL * 2 / 3
    elif 1 > WL[1] - RES >= 0:
        test2_WL = test_WL * 1 / 2
    elif WL[1] - RES < 0 and WL[1] - RES <= -1:
        test2_WL = test_WL * 1 / 3
    else:
        test2_WL = test_WL * 1 / 6

    if FW[1] - RES >= 2:
        test2_FW = test_FW * 5 / 6
    elif 2 > FW[1] - RES >= 1:
        test2_FW = test_FW * 2 / 3
    elif 1 > FW[1] - RES >= 0:
        test2_FW = test_FW * 1 / 2
    elif FW[1] - RES < 0 and FW[1] - RES <= -1:
        test2_FW = test_FW * 1 / 3
    else:
        test2_FW = test_FW * 1 / 6

    if SM[1] - RES >= 2:
        test2_SM = test_SM * 5 / 6
    elif 2 > SM[1] - RES >= 1:
        test2_SM = test_SM * 2 / 3
    elif 1 > SM[1] - RES >= 0:
        test2_SM = test_SM * 1 / 2
    elif SM[1] - RES < 0 and SM[1] - RES <= -1:
        test2_SM = test_SM * 1 / 3
    else:
        test2_SM = test_SM * 1 / 6

    TAB2 = [round(test2_WL, 1), round(test2_FW, 1), round(test2_SM, 1)]
    print(f"zraniena na res {RES} : {TAB2}")
    # TEST3
    for ARM in range(0, 7):
        if ARM - 3 <= 0:
            test3_WL = test2_WL
        elif 0 < ARM - 3 <= 1:
            test3_WL = test2_WL * 5 / 6
        elif 1 < ARM - 3 <= 2:
            test3_WL = test2_WL * 2 / 3
        elif 2 < ARM - 3 <= 3:
            test3_WL = test2_WL * 1 / 2
        elif 3 < ARM - 3 <= 4:
            test3_WL = test2_WL * 1 / 3
        elif 4 < ARM - 3 <= 5:
            test3_WL = test2_WL * 1 / 6

        if ARM - 1 <= 0:
            test3_FW = test2_FW
        elif 0 < ARM - 1 <= 1:
            test3_FW = test2_FW * 5 / 6
        elif 1 < ARM - 1 <= 2:
            test3_FW = test2_FW * 2 / 3
        elif 2 < ARM - 1 <= 3:
            test3_FW = test2_FW * 1 / 2
        elif 3 < ARM - 1 <= 4:
            test3_FW = test2_FW * 1 / 3
        elif 4 < ARM - 1 <= 5:
            test3_FW = test2_FW * 1 / 6

        if ARM - 2 <= 0:
            test3_SM = test2_SM
        elif 0 < ARM - 2 <= 1:
            test3_SM = test2_SM * 5 / 6
        elif 1 < ARM - 2 <= 2:
            test3_SM = test2_SM * 2 / 3
        elif 2 < ARM - 2 <= 3:
            test3_SM = test2_SM * 1 / 2
        elif 3 < ARM - 2 <= 4:
            test3_SM = test2_SM * 1 / 3
        elif 4 < ARM - 2 <= 5:
            test3_SM = test2_SM * 1 / 6

        TAB3 = [round(test3_WL, 1), round(test3_FW, 1), round(test3_SM, 1)]
        print(f"po save'ach AS {7 - ARM}+ : {TAB3}")
    print("------------------")
input("Nacisnij ENTER aby zakonczyc:")
