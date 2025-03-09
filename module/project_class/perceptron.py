import numpy as np

class Perceptron:
    def __init__(self):
        self.__weights = [0, 0]
        self.__bias = 0

        self.randomize_weights_and_bias()

    def activation(self, net: int) -> int:
        return 1 if net >= 0 else 0
    
    def train(self, inputs : list, results : list, alpha : float, iterations : int, randomize_values = 0) -> bool:
        
        totalError = 0

        if randomize_values:
            self.randomize_weights_and_bias()

        for _ in range(iterations):
            totalError = 0

            for i in range(len(inputs)):
                net = inputs[i][0]*self.__weights[0] + inputs[i][1]*self.__weights[1] + self.__bias[0]

                y = self.activation(net)

                e = results[i] - y
                totalError += abs(e)

                if(e != 0):
                    self.__weights[0] = self.__weights[0] + e * alpha * inputs[i][0]
                    self.__weights[1] = self.__weights[1] + e * alpha * inputs[i][1]
                    self.__bias[0] = self.__bias[0] + e * alpha

            if totalError == 0:
                return True
        
        return False

    def predict(self, x : int, y : int) -> int:
        net = x*self.__weights[0] + y*self.__weights[1] + self.__bias[0]

        return self.activation(net)
    
    def predict(self, inputs : list) -> list:
        results = []

        for i in range(len(inputs)):
            net = inputs[i][0]*self.__weights[0] + inputs[i][1]*self.__weights[1] + self.__bias[0]
            results.append(self.activation(net))

        return results

    def get_MB_equation_line(self):
        if self.__weights[1]:
            m = -(self.__weights[0] / self.__weights[1])
            c = -(self.__bias[0] / self.__weights[1])

            return (m,c)
        else:
            return None
        
    @property
    def weights(self):
        return self.__weights
    
    @property
    def bias(self):
        return self.__bias[0]

    def randomize_weights_and_bias(self):
        self.__weights = np.random.rand(2)
        self.__bias = np.random.rand(1)