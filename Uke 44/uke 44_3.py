(x_1, x_2, N) = (int(0), int(1), int(input("N?: "))) # Fib(1) = 0, Fib(2) = 1
for i in range(N):
    (x_1, x_2) = (x_2, x_1 + x_2)
print(f"Fib({N}): {x_1}.")