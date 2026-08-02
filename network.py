from neuron import LIFNeuron

class SimpleNetwork:
    def __init__(self):
        self.A = LIFNeuron()
        self.B = LIFNeuron()
        self.C = LIFNeuron()

        self.wAB = 1.2
        self.wBC = 1.0


    def step(self, external_input):
        resultA = self.A.step(external_input)
        input_B = resultA["spike"]*self.wAB
        resultB = self.B.step(input_B)
        input_C = resultB["spike"]*self.wBC
        resultC = self.C.step(input_C)

        return {"A": resultA, "B": resultB, "C": resultC}
    

