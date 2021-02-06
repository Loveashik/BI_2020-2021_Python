import numpy as np
import matplotlib.pyplot as plt

#задаем начальные точки для вершин и середин сторон квадрата
vertices = np.array([[0, 0],
                     [0, 1],
                     [1, 1],
                     [1, 0]])
mid_vertices = np.array([[0, 0.5],
                         [0.5, 1],
                         [1, 0.5],
                         [0.5, 0]])
#Задаем стартовую точку, от которой будем двигаться
start_point = np.array([0, 0])

N_POINTS = 50000
points = np.zeros((N_POINTS, 2))
points[0] = start_point
for i in range(1, N_POINTS):
    if np.random.rand() > 0.5:	#с вероятностью 1/2 выбираем либо вершину, либо середину ребра
        # Выбираем случайную вершину и проходим к ней на треть пути
        random_point = vertices[np.random.randint(4)]
        points[i] = (points[i - 1] + random_point) / 3
    else:
        # Выбираем центр случайной стороны и проходим к ней на треть пути
        random_point = mid_vertices[np.random.randint(4)]
        points[i] = (points[i - 1] + random_point) / 3
    

plt.figure(figsize=(12,9))   
plt.style.use('seaborn-whitegrid')
plt.xlabel("x", fontsize=16)
plt.ylabel("y", fontsize=16)    
plt.scatter(points[:, 0], points[:, 1], s=5, alpha=0.5, color='purple')
plt.show()

