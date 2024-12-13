(k, results) = (25,[])
for N in range(2, 2**(k-1)):
    if pow(2, k, N - 1) == 1:
        is_minimal = all(pow(2, m, N - 1) != 1 for m in range(1, k))
        if is_minimal:
            results.append(N)
results.append(2**k)
print(f"Lengder N med minste periode k={k}:{results} \nSom summerer til {sum(results)}" )