'''
Работа функции занимает до 10 минут! Если нужно быстро проверить,
что все заработало, можно уменьшить MAX_RANGE или N_RUNS
'''
from random import shuffle
import numpy as np
import matplotlib.pyplot as plt
import time

def generate_n_random_list(n):
    random_list = np.random.uniform(0, 100, n)
    return random_list

# Реализация monkey-sort, в начале проверка что список отсортирован
def is_sorted(data) -> bool:
    return all(data[i] <= data[i + 1] for i in range(len(data) - 1))

def bogosort(data) -> list:
# перемешиваем список случайным образом пока он не отсортируется
    while not is_sorted(data):
        shuffle(data)
    return data


MAX_RANGE = 11
N_RUNS = 5
l = []
means = []
stds = []

for k in range(1, MAX_RANGE):
    time_line = np.zeros(N_RUNS)
    for i in range(N_RUNS):
        l = generate_n_random_list(k)
        start = time.time()
        bogosort(l)
        end = time.time()
        execution = end - start
        time_line[i] = execution
    means.append(np.mean(time_line))
    stds.append(np.std(time_line))
print(means)



means = np.asarray(means)
stds = np.asarray(stds)

plt.figure(figsize=(12,9))
plt.style.use('seaborn-whitegrid')
plt.xlabel("count", fontsize=16)
plt.ylabel("mean time, s", fontsize=16)

plt.plot(np.arange(1, MAX_RANGE), means, color='red', linewidth=5, linestyle="dotted", dash_capstyle="round")
plt.fill_between(np.arange(1, MAX_RANGE), means-stds, means+stds, alpha=0.5, color='darkorange')
plt.show()

