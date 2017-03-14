from sklearn  import  svm
import matplotlib.pyplot as plt

def classify(X):
    Xs= []
    ys= []
    for [x,y,c] in X:
        if c == 1 or c==0:
            Xs.append([x,y])
            ys.append(c)
    clf = svm.SVC()
    clf.fit(Xs,ys)
    for i in range(len(X)):
        if X[i][2] == -1:
            X[i][2] = clf.predict([X[i][0],X[i][1]])
    return X


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
