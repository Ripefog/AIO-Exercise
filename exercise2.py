import math

alpha = 0.01

# Ham kiem tra co phai la number k
def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True

# Ham sigmoid
def sigmoid(x):
    return 1/(1 + math.e**(-x))

# Ham relu
def relu(x):
    if x <= 0:
        return 0
    else: 
        return x

# Ham elu
def elu(x):
    if x <= 0:
        return alpha * (math.e**x - 1)
    else:
        return x

#Ham chinh
def exercise2():  
    # Nhap x tu useer
    x = input("Input x = ")

    if not is_number(x):
        print("x must be a number")
        return

    x = float(x) # Chuyen x sang float

    # Nhap activation function tu user
    fun = input("Input activation Function ( sigmoid | relu | elu ) : ").strip().lower()

    # Kiem tra xem ham co hop le hay khong
    if fun not in ["sigmoid", "relu", "elu"]:
        print(f"{fun} is not supported")
        return
    
    # Tinh toan ket qua f(x) theo ham tuong ung
    if fun == "sigmoid":
        result = sigmoid(x)
    elif fun == "relu":
        result = relu(x)
    elif fun == "elu":
        result = elu(x)

    print(f"{fun}: f({x}) = {result}")

# Chay ham
exercise2()