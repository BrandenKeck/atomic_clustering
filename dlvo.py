import math
import numpy as np
import matplotlib.pyplot as plt

# Get the DLVO result
def DLVO(d, c1, c2, c3, c4):    
    HA = (c1)/(np.exp(c2*d)) # Hamaker Attraction
    ER = -(c3)/(c4*(d)**2) # Electronic Repulsion
    Total = HA + ER
    return [Total, HA, ER]

if __name__ == "__main__":
    
    # Define DLVO parameters
    alpha1 = 1
    alpha2 = 1/2
    beta1 = 1/5
    beta2 = 1/3
    
    X = np.arange(0.5, 20, 0.001)
    Y1 = []
    Y2 = []
    Y3 = []
    
    for x in X:
        [y1, y2, y3] = DLVO(x, alpha1, alpha2, beta1, beta2)
        Y1.append(y1)
        Y2.append(y2)
        Y3.append(y3)

    print(X[Y1.index(max(Y1))])
    
    plt.plot(X,Y1,'r-')
    plt.plot(X,Y2,'b-')
    plt.plot(X,Y3,'g-')
    plt.show()