import sys; args = sys.argv[1:]
# Richard Song - LGNN Lab
import math
import random

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

#
file = sys.argv[1]
# file = "text.txt"
activationFunction = 'T3'


activationFunctionMap = {'T1': t1, 'T2': t2, 'T3': t3, 'T4': t4}
weights = dict()  # layer number maps to matrices of weights per node in hidden layer
sizes = []  # size of each hidden layer + output layer

line = [0]
xVals = []
errors = []

inputs = []
outputs = []
inputSize = 0

errorSum = []
alpha = .1

def initIO():
    global inputs
    global outputs
    global inputSize
    global sizes
    with open(file, 'r') as reader:
        while True:
            temp = [i for i in reader.readline().split()]
            if len(temp) == 0:
                break
            inputVals = [int(i) for i in temp[0:len(temp)-2]] + [1]
            outputVals = [int(i) for i in temp[len(temp)-1]]
            inputs.append(inputVals)
            outputs.append(outputVals)
            inputSize = len(inputVals)
    sizes = [inputSize, 2, 1, 1]


def initXVals(index):
    global errors
    global inputs
    global xVals
    errors = []
    xVals = []
    for i in range(len(sizes)):
        xVals.append([])
        errors.append([])
        for j in range(0, int(sizes[i])):
            xVals[i].append(0)
            errors[i].append(0)
        if i == 0:
            xVals[i] = inputs[index]


def initWeights():
   layerNumber = 1
   global weights
   global sizes
   for i in range(1, 4):
       weights[i] = []
       for j in range(0, int(sizes[i])):
           weights[i].append([])  # initialize weight matrix
           for k in range(0, int(sizes[i-1])):
               weights[i][j].append(4*random.random()-2)


def ff(inputLayer):
    global xVals
    for i in range(0, 3):
        output = []
        for j in range(int(sizes[i+1])):
            dotProduct = dot(inputLayer, weights[i+1][j])  # dot the weights of each hidden layer node with input
            if i != 2:
                xVals[i+1][j] = activationFunctionMap[activationFunction](dotProduct)
            else:
                xVals[i+1][j] = dotProduct
            output.append(xVals[i + 1][j])  # convert output with activation function
        inputLayer = output  # output becomes the new input layer
    return inputLayer
    # print(' '.join(str(x) for x in inputLayer))


def backProp(out):
    global weights
    global errors
    global xVals
    for i in range(3, -1, -1):
        if i == 3:
            errors[i][0] = (out[0]-xVals[i][0])
            errorSum.append(.5*abs(errors[i][0])**2)
        else:
            for j in range(0, int(sizes[i])):
                totalError = 0
                for k in range(0, int(sizes[i+1])):
                    w = weights[i+1][k][j]
                    e = errors[i+1][k]
                    totalError += (w*e)
                    weights[i+1][k][j] += e*xVals[i][j]*alpha
                totalError *= (xVals[i][j] * (1-xVals[i][j]))
                errors[i][j] = totalError


def printWeights():
    global weights
    for i in weights:
        temp = []
        for k in weights[i]:
            temp += k
        print(temp)


def run():
    global inputs
    global outputs
    global errorSum
    initIO()
    initWeights()
    reps = 0
    while True:
        reps+=1
        errorSum = []
        for j in range(len(inputs)):
            initXVals(j)
            ff(inputs[j])
            backProp(outputs[j])
        if sum(errorSum) < 0.005:
            print('Layer cts:', sizes)
            print('Errors:', errorSum)
            print('Weights:')
            printWeights()
            break
        if reps == 45000:
            reps = 0
            initWeights()
    # print()
    # print()
    #
    # for j in range(len(inputs)):
    #     initXVals(j)
    #     print(inputs[j], end=' ')
    #     print(ff(inputs[j]))
    #     # backProp(outputs[j])
    #     # print(errors)

run()
print(inputs)
