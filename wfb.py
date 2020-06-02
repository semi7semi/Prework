

off = input("Podaj wartoc Offensive Skill: ")
deff = input("Podaj wartosc Defensive Skill: ")
str = input("Podaj wartosc Strengh: ")
res = input("Podaj wartosc Res: ")
att = input("Podaj wartosc Attack: ")
reflex = input("Podaj wartosc: Jesli masz Reflexy [ 1 ], Jesli przeciwnik ma Distracting [ -1 ], jesli nic [ 0 ] ")

OFF = float(off)
DEF = float(deff)
STR = float(str)
RES = float(res)
ATT = float(att)
REFLEX = int(reflex)

if OFF - DEF > 0:
    test = ATT*(2/3 + (REFLEX*1/6))

else:
    test = ATT * (1 / 2 + (REFLEX * 1 / 6))

print(f"{round(test, 1)} atakow trafilo!")

if STR - RES <= -2:
    test2 = test * 1/6

elif STR - RES > -2 and STR - RES <= -1:
    test2 = test * 1/3

elif STR - RES <= 0 and STR - RES >=0:
    test2 = test * 1/2

elif STR - RES >= 1 and STR - RES < 2:
    test2 = test * 2/3

else:
    test2 = test * 5/6

print(f"{round(test2, 1)} tyle zadales ran")


input('Do you want to quit? Enter')


