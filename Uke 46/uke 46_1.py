(n, i, l) = (int(input("Skriv inn et heltall: ")), 2, [])
while n > 1:
    while n % i == 0:
        (n, _) = (n // i, l.append(i)) # _ brukes ofte for forkaste et resultat
    i += 1
print(f"Primtallsfaktorisering: {", ".join([str(x) for x in l])}")