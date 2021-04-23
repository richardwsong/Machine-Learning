import sys; args = sys.argv[1:]
# Richard Song - FF Lab
import math


def dot(x, y):
    dotHelper = zip(x, y)
    dotProduct = 0
    for i in dotHelper:
        dotProduct += (i[0]*i[1])
    return dotProduct


def t1(x):
    return x


def t2(x):
    return x if x > 0 else 0


def t3(x):
    return 1/(1+math.exp(-1*x))


def t4(x):
    return 2/(1+math.e**(-1*x)) - 1


file = sys.argv[1]
activationFunction = sys.argv[2]
inputLayer = [float(i) for i in sys.argv[3:]]

# file = "text.txt"
# activationFunction = "T3"
# inputLayer = [-0.5, -0.9, -0.9, 1.9, 1.4]


activationFunctionMap = {'T1': t1, 'T2': t2, 'T3': t3, 'T4': t4}
weights = dict()  # layer number maps to matrices of weights per node in hidden layer
sizes = []  # size of each hidden layer + output layer
layerNumber = 1

line = [0]
with open(file, 'r') as reader:
    layerSize = -1
    inputSize = len(inputLayer)
    while len(line) != 0:
        temp = [float(i) for i in reader.readline().split()]  # splice each number, convert to float
        if len(temp) == 0:
            break
        line = temp
        layerSize = len(line)/inputSize  # layer size is current layer divided my previous layer
        sizes.append(layerSize)
        weights[layerNumber] = []
        for i in range(0, int(layerSize)):
            weights[layerNumber].append([])  # initialize weight matrix
        index = 0
        for i in range(0, len(line)):
            if i % inputSize == 0 and i != 0:  # if mod is 0, move to next node in layer
                index += 1
            weights[layerNumber][index].append(line[i])
        inputSize = layerSize
        layerNumber += 1

for i in range(0, layerNumber-2):
    output = []
    for j in range(int(sizes[i])):
        dotProduct = dot(inputLayer, weights[i+1][j])  # dot the weights of each hidden layer node with input
        output.append(activationFunctionMap[activationFunction](dotProduct))  # convert output with activation function
    inputLayer = output  # output becomes the new input layer

for i in range(0, len(inputLayer)):
    inputLayer[i] = inputLayer[i]*line[i]

print(' '.join(str(x) for x in inputLayer))


