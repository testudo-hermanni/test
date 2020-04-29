import numpy as np
def AND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.7
    tmp = np.sum(w*x)+b
    if tmp <= 0:
        return 0
    else:
        return 1

def NAND(x1,x2):
    x = np.array([x1,x2])
    w = np.array([-0.5,-0.5])
    b = 0.7
    tmp = np.sum(w*x)+b
    if tmp <= 0:
        return 0
    else:
        return 1

def OR(x1,x2):
    x = np.array([x1,x2])
    w = np.array([0.5,0.5])
    b = -0.1
    tmp = np.sum(w*x)+b
    if tmp <= 0:
        return 0
    else:
        return 1

def XOR(x1,x2):
    s1=NAND(x1,x2)
    s2=OR(x1,x2)
    y=AND(s1,s2)
    return y

print('-AND Gate-')
print(AND(0,0))
print(AND(0,1))
print(AND(1,0))
print(AND(1,1))

print('-NAND Gate-')
print(NAND(0,0))
print(NAND(0,1))
print(NAND(1,0))
print(NAND(1,1))


print('-OR Gate-')
print(OR(0,0))
print(OR(0,1))
print(OR(1,0))
print(OR(1,1))

print('-XOR Gate-')
print(XOR(0,0))
print(XOR(0,1))
print(XOR(1,0))
print(XOR(1,1))

hoge=np.array([0.1,0,4,2.5,3.1])
print(np.argmin(hoge))
print(np.argmax(hoge))
