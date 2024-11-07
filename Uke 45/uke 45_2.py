import functools as ft, operator as op
res = 0
for i in range(10, 100):
    res += ft.reduce(op.mul, [int(x) for x in str(i)]) # Map-Reduce Idiom
print(res)  # Løsning på Abel Del 1 2024, oppgave 18. 