import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

rg = np.random.RandomState(0)

#generear un rando de valores en el eje x
x = np.linspace(0, 10, 500)
#calcular valores aleatorios y calcular suma de valores aleatorios
y = np.cumsum(rg.randn(500, 6), axis=0)
#graficar los datos
plt.plot(x, y)
plt.legend('ABCDEF', ncol=2, loc='upper left')
plt.show()

sns.set()
plt.plot(x,y)
plt.legend('ABCDEF', ncol=2, loc='upper left')
plt.show()

y_val = x ** 2

plt.scatter(x,y_val, marker ="s" , color="g")
plt.title("Grafico de dispersión")
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.show()
