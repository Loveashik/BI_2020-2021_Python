# Libraries
import matplotlib.pyplot as plt
import pandas as pd
from math import pi

# Set data
df = pd.DataFrame({
    'вид': ['Ягуар', 'Лев', 'Леопард', 'Гепард'],
    'сила укуса': [137, 112, 112, 119],
    'скорость': [80, 80, 58, 130],
    'длина': [1.6, 2.1, 1.25, 1.3],
    'вес': [76, 190, 31, 46],
    'прод-ть\n жизни': [18.5, 12, 14.5, 20]
})

attr_cols = df.columns[1:]
for col in attr_cols:
    df[col] = 10 * (df[col] / max(df[col]))  # отнормировали данные, привели к 10-бальной шкале

def show_radar_plot(row, title, color):
    categories = list(df)[1:]
    N = len(categories)

    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]

    ax = plt.subplot(2, 2, row + 1, polar=True)
    ax.set_theta_offset(pi / 2)
    ax.set_theta_direction(-1)
    plt.xticks(angles[:-1], categories, color='grey', size=10)
    ax.set_rlabel_position(0)
    plt.yticks([2, 4, 6, 8], ["2", "4", "6", "8", ], color="grey", size=10)
    plt.ylim(1, 10)

    values = df.loc[row].drop('вид').values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, color=color, linewidth=2, linestyle='solid')
    ax.fill(angles, values, color=color, alpha=0.4)

    plt.title(title, size=15, color=color, y=1.1)

plt.figure(figsize=(15, 15))

my_palette = plt.cm.get_cmap("Set1", len(df.index))

for row in range(0, len(df.index)):
    show_radar_plot(row=row, title=df['вид'][row], color=my_palette(row))
plt.show()