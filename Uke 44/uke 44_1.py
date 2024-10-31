(a, b) = [int(x) for x in input("Skriv inn en brøk A/B: ").split("/")]
while b > 0:
    (a, b) = (b, a % b)
print(f"Brøken kan forkortes med {a}.") 