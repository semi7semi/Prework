DEF = int(input("podaj def: "))
REFLEX = int(input("Relfexy: 1, Distracting: -1, Brak: 0 - "))
ATT_WL = int(input("ataki WL: "))
ATT_FW = int(input("ataki FW: "))
ATT_SM = int(input("ataki SM: "))


# OFF, STR, AP
WL = [5, 6, 3]
FW = [5, 4, 1]
SM = [6, 5, 2]


def hit1(off, deff, att):
    if off > deff:
        test1 = att * 2 / 3
    else:
        test1 = att / 2
    return test1


def hit2(off, deff, att, ref):
    if off > deff:
        test1 = att * (2 / 3 + ref / 6)
    else:
        test1 = att * (1 / 2 + ref / 6)
    return test1


HIT = [hit1(WL[0], DEF, ATT_WL), hit2(FW[0], DEF, ATT_FW, REFLEX), hit2(SM[0], DEF, ATT_SM, REFLEX)]

print("----------------WL, FW, SM")
print("----Trafienia:", round(HIT[0], 1), round(HIT[1], 1), round(HIT[2], 1))
print("---------------------------")


def wound(st, res, test11):
        if st - res >= 2:
            test2 = test11 * 5 / 6
        elif 2 > st - res >= 1:
            test2 = test11 * 2 / 3
        elif 1 > st - res >= 0:
            test2 = test11 / 2
        elif 0 > st - res >= -1:
            test2 = test11 / 3
        else:
            test2 = test11 / 6
        return(round(test2, 1))


for RES in range(3, 7):
    WOUND = [wound(WL[1], RES, HIT[0]), wound(FW[1], RES, HIT[1]), wound(SM[1], RES, HIT[2])]
    print(f"Rany vs Res {RES}:", WOUND[0], WOUND[1], WOUND[2])


    def armour(ap, arm, test111):
        if arm - ap <= 0:
            test3 = test111
        elif 0 < arm - ap <= 1:
            test3 = test111 * 5 / 6
        elif 1 < arm - ap <= 2:
            test3 = test111 * 2 / 3
        elif 2 < arm - ap <= 3:
            test3 = test111 / 2
        elif 3 < arm - ap <= 4:
            test3 = test111 / 3
        else:
            test3 = test111 / 6
        return round(test3, 1)


    for ARM in range(6):
        print(f"------Arm {7 - ARM}+ :",
              armour(WL[2], ARM, WOUND[0]), armour(FW[2], ARM, WOUND[1]), armour(SM[2], ARM, WOUND[2]))
    print("--------------------------")
#  input("Nacisnij ENTER aby zakonczyc:")
