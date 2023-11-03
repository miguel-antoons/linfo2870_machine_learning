# -*-coding:Utf-8 -*

import numpy as np
import matplotlib.pyplot as plt


def visualize2d(train, test):
    (x_train, y_train, y_predict, loss) = train
    (x_tot, y_tot, y_predict_tot, loss_tot) = test
    
    # Plot result
    fig=plt.figure(figsize=(10,4))
    ax = plt.subplot(121)
    ax.plot(x_tot,y_tot)
    ax.scatter(x_train, y_train)
    ax.scatter(x_train, y_predict)
    ax.set_title(f"{loss:.3f}")

    ax = plt.subplot(122)
    ax.plot(x_tot, y_tot)
    ax.plot(x_tot, y_predict_tot)
    ax.set_title(f"{loss_tot:.3f}")
    plt.show()

