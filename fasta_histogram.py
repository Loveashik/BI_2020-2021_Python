import matplotlib.pyplot as plt
import numpy as np

def plot_hist(path):
    list_of_lengths = []
    count = 0
    with open(path, 'r') as in_file:
        for line in in_file:
            if line.startswith(">"):
                list_of_lengths.append(count)
                count = 0
            else:
                count += (len(line)) - 1
        list_of_lengths.append(count)
        list_of_lengths = list_of_lengths[1:]
        list_of_lengths = np.array(list_of_lengths)

        plt.style.use('seaborn-whitegrid')
        plt.title("Распределение длин последовательностей")
        plt.xlabel("длина последовательности, нуклеотиды")
        plt.ylabel("количество последовательностей")
        plt.hist(list_of_lengths, color='darkorange', rwidth=0.8, bins=15)
        plt.show()

if __name__ == '__main__':
    plot_hist('/home/asha/ZIN/islands_ruf/ALIGNMENT/data/31tissue.fas')
