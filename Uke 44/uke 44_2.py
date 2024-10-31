def Tn(N: int):
    return N * (N + 1) // 2 # heltallsdivisjon for å bevare integer type
if __name__ == '__main__':
    print(f"Sum av alle N fra 1 til 5 er {Tn(5)}.")