import numpy as np
(Periode,L) = (4, [])
for N in range(4, 2**60, 2):
    P = np.zeros((N,N))
    for i in range(N//2):
        (P[i*2, i], P[i*2 + 1, N//2 + i]) = (1, 1)
    if abs((2*np.pi)/np.angle(sorted((x for x in np.linalg.eigvals(P) if np.angle(x) > 0), key=np.angle)[0]) - Periode) < 1e-5: L.append(N)
print(L)
print(sum(L)) # sum av alle vektorlengder som permuteres tilbake til sin originale form etter 8 riffle shuffles