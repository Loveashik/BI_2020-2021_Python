import numpy as np
import matplotlib.pyplot as plt


WALK_SIZE = 100000
coordinates = np.zeros((WALK_SIZE, 2))

#задаем список возможных движений
movements = np.array([[-1, 0],
                      [1, 0],
                      [0, 1],
                      [0, -1]])


#прибавляем к предыдущей координате случайное движение чтобы получить следующую
for t in range(1, WALK_SIZE):
    coordinates[t] = coordinates[t - 1] + movements[np.random.randint(4)]


plt.figure(figsize=(12,9))
plt.scatter(coordinates[:,0], coordinates[:,1], c=np.arange(WALK_SIZE))
plt.show()

