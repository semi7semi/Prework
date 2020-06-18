print("Witaj! Dzisiaj pobawimy sie ciagiem Fibonacciego")
n = int(input("Podaj liczbe wyrazów ciągu: "))
fibb = [0, 1]


def fibonacci(fib):
    for i in range(n + 1):
        fib.append(fib[i] + fib[i+1])
        print(f"{i} wyraz ciagu Fibonacciego: {fib[i]}")


fibonacci(fibb)

x = len(fibb) - 3

fi_mid = fibb[x // 2] / fibb[(x // 2)-1]
fi_end = fibb[n] / fibb[n-1]

print(f"złota proporcja z srodka fi = {round(fi_mid, 3)}")
print(f"złota proporcja z konca fi = {round(fi_end, 3)}")

# maksymalny wyraz ciagu ktory mozna policzyc to n = 207223, potem brakuje pamieci :D
