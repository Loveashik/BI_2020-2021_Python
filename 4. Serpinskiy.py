import numpy as np
import matplotlib.pyplot as plt

#Задаем первые три точки по углам треугольника
triangle = np.array([[-1, 0],
                     [1, 0],
                     [0, np.sqrt(3) / 2]])

#Задаем стартовую точку от которой будем шагать
start_point = np.array([0, 0])

N_POINTS = 10000
points = np.zeros((N_POINTS, 2))
points[0] = start_point

#Ставим каждую следующую точку точку на полпути к одной из случайных начальных точек от предыдущей точки
for i in range(1, N_POINTS):
    random_point = triangle[np.random.randint(3)]
    points[i] = (points[i - 1] + random_point) / 2

plt.figure(figsize=(12,9))   
plt.style.use('seaborn-whitegrid')
plt.xlabel("x", fontsize=16)
plt.ylabel("y", fontsize=16)    
plt.scatter(triangle[:, 0], triangle[:, 1], s=100, color='darkorange')
plt.scatter(points[:, 0], points[:, 1], s=10, alpha=0.5, color='purple')
plt.show()

