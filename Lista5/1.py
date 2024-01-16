### METODA LAGRANGE ###
xData = [0,3000,6000]
yData = [1.225,0.905,0.652]
x = 2000

def lagrange(x,xData,yData):
    n = len(xData)
    y = 0
    for i in range(n):
        w = 1.0
        for j in range(n):
            if i != j:
                w = w * (x - xData[j]) / (xData[i] - xData[j])
        y = y + w * yData[i]
    return y

print(lagrange(x,xData,yData))