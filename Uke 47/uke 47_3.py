def gcd(A: int, B: int) -> int:
    while B:
        A, B = B, A % B
    return A
if __name__ == '__main__':
    assert gcd(23*21, 23) == 23                                 # assert stanser programmet umiddelbart ved feil
    print(f"Test:  gcd(23*21, 23) = { gcd(23*21, 23) } OK")     # Kommer koden hit har testen gått gjennom.