import random
import numpy as np
import matplotlib.pyplot as plt
import time


def generate_n_random_points_classic(n):
    random_numbers = [random.random() for _ in range(n)]
    return random_numbers

def generate_n_random_points_numpy(n):
    random_numbers = np.random.uniform(0, 1, n)
    return random_numbers

def count_execution_times(n):
    '''функция считает время выполнения забора n случайных чисел
    из равномерного распределения для random и numpy и выводит оба
    '''
    classic_start = time.time()
    generate_n_random_points_classic(n)
    classic_end = time.time()
    classic_execution = classic_end - classic_start
    
    numpy_start = time.time()
    generate_n_random_points_numpy(n)
    numpy_end = time.time()
    numpy_execution = numpy_end - numpy_start
    
    return classic_execution, numpy_execution


counts = [100, 1000, 10000, 100000, 1000000]
classic_time = []
numpy_time = []
for i in counts:
    classic_time.append(count_execution_times(i)[0])
    numpy_time.append(count_execution_times(i)[1])

plt.figure(figsize=(12,9))
plt.style.use('seaborn-whitegrid')
plt.xlabel("count", fontsize=16)
plt.ylabel("time, s", fontsize=16)
line_classic,=plt.plot(counts, classic_time, color="darkorange", linestyle="dotted", 
                      linewidth= 5, dash_capstyle="round", label='Classic')
line_numpy,=plt.plot(counts, numpy_time, color="green", linestyle="dotted",
                    linewidth= 5, dash_capstyle="round", label='Numpy')
plt.legend(handles=[line_classic, line_numpy])
plt.show()


