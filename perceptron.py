import numpy as np
# Setting the random seed, feel free to change it and see different solutions.
np.random.seed(42)

def stepFunction(t):
    if t >= 0:
        return 1
    return 0

def prediction(X, W, b):
    return stepFunction((np.matmul(X,W)+b)[0])

# TODO: Fill in the code below to implement the perceptron trick.
# The function should receive as inputs the data X, the labels y,
# the weights W (as an array), and the bias b,
# update the weights and bias W, b, according to the perceptron algorithm,
# and return W and b.
def perceptronStep(X, y, W, b, learn_rate = 0.01):
    # Fill in code
    
    # 'pred' is an int object.
    pred = prediction(X, W, b)
    
    ##############################################
    ## print out the input data structures
    #typ_x = type(X)
    #typ_y = type(y)
    #typ_w = type(W)
    #typ_b = type(b)
    
    #print('typ_x = ', typ_x, ', ', 'typ_y = ', typ_y, ', ', 'typ_w = ', ', ', typ_w, 'typ_b = ', typ_b)
    #print(type(X[0]))
    #print(np.shape(X))
    #print(np.shape(y))
    #print(np.shape(W))
    #print(np.shape(b))
    
    #print(np.int(y[0]))
    #print(X[0])
    #print(W[0], W[1])
    #print(b)
    #print(len(y))
    #print(len(X))
    ##############################################
    
    for i in range(len(X)):
        if (pred == 0 and y[i] == 0) or (pred == 1 and y[i] == 1):
            pass
        elif pred == 0 and y[i] == 1:
            W[0] = W[0] + (learn_rate * X[i][0])
            W[1] = W[1] + (learn_rate * X[i][1])
            b = b + learn_rate
        else:
            W[0] = W[0] - (learn_rate * X[i][0])
            W[1] = W[1] - (learn_rate * X[i][1])
            b = b - learn_rate
    print (W,b)
    return W, b
    
# This function runs the perceptron algorithm repeatedly on the dataset,
# and returns a few of the boundary lines obtained in the iterations,
# for plotting purposes.
# Feel free to play with the learning rate and the num_epochs,
# and see your results plotted below.
def trainPerceptronAlgorithm(X, y, learn_rate = 0.01, num_epochs = 50):
    x_min, x_max = min(X.T[0]), max(X.T[0])
    y_min, y_max = min(X.T[1]), max(X.T[1])
    W = np.array(np.random.rand(2,1))
    b = np.random.rand(1)[0] + x_max
    # These are the solution lines that get plotted below.
    boundary_lines = []
    for i in range(num_epochs):
        # In each epoch, we apply the perceptron step.
        W, b = perceptronStep(X, y, W, b, learn_rate)
        boundary_lines.append((-W[0]/W[1], -b/W[1]))
    return boundary_lines
