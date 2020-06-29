time = int(input("Podaj ile sekund minelo od błyskawicy: "))


def storm(sec):
    v_sonic = 340
    d = sec * v_sonic
    return f"Burza jest {round(d/1000, 1)}km od ciebie!"


print(storm(time))
print(input("Nacisnij ENTER aby zakonczyc"))
