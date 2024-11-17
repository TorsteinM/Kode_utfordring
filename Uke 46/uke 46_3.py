from time import sleep
(i, c) = (0, '▁▂▃▄▅▆▇█▉'*5)
while True:
    print(c[i % len(c):] + c[:i % len(c)], end='\r')
    i += 1
    sleep(0.05)