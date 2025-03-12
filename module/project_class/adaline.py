import numpy as np

# Preguntar, en que rango de valores en el eje y se encuentra la señal limpia y la señal con ruido
class Adaline:
    def __init__(self, number_of_inputs : int):
        self.__number_of_inputs = number_of_inputs
        self.__weights = np.zeros(number_of_inputs)
        self.__bias = 0

    def activation(self, net: float) -> float:
        return net
    
    def predict(self, inputs : list, result : float, alpha : float) -> list:
        net = np.dot(inputs, self.__weights) + self.__bias

        error = result - net

        for i in range(len(self.__weights)):
            self.__weights[i] = self.__weights[i] + error * alpha * inputs[i]
        self.__bias[0] = self.__bias[0] + error * alpha


        return self.activation(net)
        
    @property
    def weights(self):
        return self.__weights
    
    @property
    def bias(self):
        return self.__bias[0]

    def randomize_weights_and_bias(self):
        self.__weights = np.random.rand(self.__number_of_inputs)
        self.__bias = np.random.rand(1)