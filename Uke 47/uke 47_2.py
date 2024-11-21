import matplotlib.pyplot as plt, numpy as np
(A, x, p) = (np.array([[np.cos(np.pi/100), -np.sin(np.pi/100)],[np.sin(np.pi/100), np.cos(np.pi/100)]]), np.array([1,0]), [])
for i in range(100):
    x = A @ x
    p.append(x)
points = np.array(p)
(_, _) = (plt.plot(points[:,0], points[:,1]), plt.show())