import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-np.pi, np.pi, 1000)
y = np.sin(x)
plt.style.use('seaborn-whitegrid')
plt.title("LinePlot для sin(x)")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.plot(x,y, color="darkorange", linestyle="dotted", linewidth= 5, dash_capstyle="round")
plt.show()