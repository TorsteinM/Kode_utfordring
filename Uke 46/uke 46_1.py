(n, i, l) = (int(input("Skriv inn et heltall: ")), 2, [])
while n > 1:
    while n % i == 0:
        (n, _) = (n // i, l.append(i))
    i += 1
print(f"Primtallsfaktorisering: {", ".join([str(x) for x in l])}")