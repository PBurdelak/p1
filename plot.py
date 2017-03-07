import matplotlib.pyplot as plt

def load_data(filename):
    X = []
    f = open(filename)
    for line in f:
        tokens = line.split()
        X.append([float(tokens[0]),float(tokens[1]),float(tokens[2])])
    return  X

def draw_data(X):
    x1 = []
    y1 = []
    x0 = []
    y0 = []
    x_1 = []
    y_1 = []
    for [x, y, c] in X:
        if c == 1:
            x1.append(x)
            y1.append(y)
        if c == 0:
            x0.append(x)
            y0.append(y)

        if c == -1:
            x_1.append(x)
            y_1.append(y)

    plt.axis([-10,10,-10,10])
    plt.plot(x1,y1,'ro',color='red')
    plt.plot(x_1,y_1,'ro',color='black')
    plt.plot(x0,y0,'ro',color='yellow')

    plt.show()


draw_data(load_data('train'))
