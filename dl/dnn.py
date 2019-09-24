# 搭建神经网络的思路和步骤：
# 定义网络结构
# 初始化模型参数
# 循环计算：前向传播/计算当前损失/反向传播/权值更新

# 初始化模型参数
def initialize_parameters_deep(layer_dims):
    np.random.seed(3)
    parameters = {}    
    # number of layers in the network
    L = len(layer_dims)            

    for l in range(1, L):
        parameters['W' + str(l)] = np.random.randn(layer_dims[l], layer_dims[l-1])*0.01
        parameters['b' + str(l)] = np.zeros((layer_dims[l], 1))  
      
    assert(parameters['W' + str(l)].shape == (layer_dims[l], layer_dims[l-1]))        
    assert(parameters['b' + str(l)].shape == (layer_dims[l], 1))
    return parameters

# 前向传播
def linear_activation_forward(A_prev, W, b, activation):
    if activation == "sigmoid":
        Z, linear_cache = linear_forward(A_prev, W, b)
        A, activation_cache = sigmoid(Z)    
    elif activation == "relu":
        Z, linear_cache = linear_forward(A_prev, W, b)
        A, activation_cache = relu(Z)   
     
    assert (A.shape == (W.shape[0], A_prev.shape[1]))
    cache = (linear_cache, activation_cache)    
    return A, cache

# L层神经网络的前向计算函数
def L_model_forward(X, parameters):
    caches = []
    A = X    
    # number of layers in the neural network
    L = len(parameters) // 2                 

    # Implement [LINEAR -> RELU]*(L-1)
    for l in range(1, L):
        A_prev = A 
        A, cache = linear_activation_forward(A_prev, parameters["W"+str(l)], parameters["b"+str(l)], "relu")
        caches.append(cache)    
    # Implement LINEAR -> SIGMOID
    AL, cache = linear_activation_forward(A, parameters["W"+str(L)], parameters["b"+str(L)], "sigmoid")
    caches.append(cache)    
    
    assert(AL.shape == (1,X.shape[1]))    
    return AL, caches

# 计算当前损失
def compute_cost(AL, Y):
    m = Y.shape[1]    
    # Compute loss from aL and y.
    cost = -np.sum(np.multiply(Y,np.log(AL))+np.multiply(1-Y,np.log(1-AL)))/m

    cost = np.squeeze(cost)  
       
    assert(cost.shape == ())    
    return cost

# 执行反向传播
# 线性反向传播函数、线性激活反向传播函数
def linear_backward(dZ, cache):
    A_prev, W, b = cache
    m = A_prev.shape[1]

    dW = np.dot(dZ, A_prev.T)/m
    db = np.sum(dZ, axis=1, keepdims=True)/m
    dA_prev = np.dot(W.T, dZ)    

    assert (dA_prev.shape == A_prev.shape)    
    assert (dW.shape == W.shape)    
    assert (db.shape == b.shape)    
    
    return dA_prev, dW, db
def linear_activation_backward(dA, cache, activation):
    linear_cache, activation_cache = cache    
    if activation == "relu":
        dZ = relu_backward(dA, activation_cache)
        dA_prev, dW, db = linear_backward(dZ, linear_cache)    
    elif activation == "sigmoid":
        dZ = sigmoid_backward(dA, activation_cache)
        dA_prev, dW, db = linear_backward(dZ, linear_cache)    
    return dA_prev, dW, db
# L层网络的反向传播函数
def L_model_backward(AL, Y, caches):
    grads = {}
    L = len(caches) 
    # the number of layers
    m = AL.shape[1]
    Y = Y.reshape(AL.shape) 
    # after this line, Y is the same shape as AL

    # Initializing the backpropagation
    dAL = - (np.divide(Y, AL) - np.divide(1 - Y, 1 - AL))    
    # Lth layer (SIGMOID -> LINEAR) gradients
    current_cache = caches[L-1]
    grads["dA" + str(L)], grads["dW" + str(L)], grads["db" + str(L)] = linear_activation_backward(dAL, current_cache, "sigmoid")    
    for l in reversed(range(L - 1)):
        current_cache = caches[l]
        dA_prev_temp, dW_temp, db_temp = linear_activation_backward(grads["dA" + str(l + 2)], current_cache, "relu")
        grads["dA" + str(l + 1)] = dA_prev_temp
        grads["dW" + str(l + 1)] = dW_temp
        grads["db" + str(l + 1)] = db_temp    
    return grads
# 权值更新
def update_parameters(parameters, grads, learning_rate):
    # number of layers in the neural network
    L = len(parameters) // 2 
    # Update rule for each parameter. Use a for loop.
    for l in range(L):
        parameters["W" + str(l+1)] = parameters["W"+str(l+1)] - learning_rate*grads["dW"+str(l+1)]
        parameters["b" + str(l+1)] = parameters["b"+str(l+1)] - learning_rate*grads["db"+str(l+1)]    
    return parameters

# 封装搭建过程
def L_layer_model(X, Y, layers_dims, learning_rate = 0.0075, num_iterations = 3000, print_cost=False):
    np.random.seed(1)
    costs = []    

    # Parameters initialization.
    parameters = initialize_parameters_deep(layers_dims)    
    # Loop (gradient descent)
    for i in range(0, num_iterations):        
        # Forward propagation: 
        # [LINEAR -> RELU]*(L-1) -> LINEAR -> SIGMOID
        AL, caches = L_model_forward(X, parameters)        
        # Compute cost.
        cost = compute_cost(AL, Y)        
        # Backward propagation.
        grads = L_model_backward(AL, Y, caches)        
        # Update parameters.
        parameters = update_parameters(parameters, grads, learning_rate)        
        # Print the cost every 100 training example
        if print_cost and i % 100 == 0:            
            print ("Cost after iteration %i: %f" %(i, cost))        if print_cost and i % 100 == 0:
            costs.append(cost)    
    # plot the cost
    plt.plot(np.squeeze(costs))
    plt.ylabel('cost')
    plt.xlabel('iterations (per tens)')
    plt.title("Learning rate =" + str(learning_rate))
    plt.show()    
    
    return parameters