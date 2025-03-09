# from perceptron import Perceptron

# p = Perceptron()

# inputs = [[0, 0], [0, 1], [1, 0], [1, 1]]
# results = [0, 0, 0, 1]

# p.train(inputs, results, 0.1, 1000)

# print(p.predict(0, 0))
# print(p.predict(0, 1))
# print(p.predict(1, 0))
# print(p.predict(1, 1))


import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.metrics import confusion_matrix

# Datos de ejemplo (etiquetas verdaderas y predichas)
true_labels = [1, 0, 1, 1, 0, 1, 0, 0, 1, 0]
predicted_labels = [1, 0, 0, 1, 0, 1, 0, 1, 1, 0]

# Crear la matriz de confusión
cm = confusion_matrix(true_labels, predicted_labels)

print(cm)

# Configurar el gráfico
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', cbar=False, xticklabels=['Predicción: 0', 'Predicción: 1'], yticklabels=['Verdadero: 0', 'Verdadero: 1'])

# Añadir etiquetas y título
ax.set_xlabel('Etiqueta Predicha')
ax.set_ylabel('Etiqueta Verdadera')
ax.set_title('Matriz de Confusión')

# Mostrar el gráfico
plt.show()