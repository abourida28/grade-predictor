import numpy as np
import pandas as pd



def intializeDataset():
    dataset = np.array(ws)
    m = dataset.shape[0]

    x = np.zeros(shape=(m, 27))
    y = np.zeros(shape=(m))

    for i in range(m):
        x[i] = dataset[i][:27]
        y[i] = dataset[i][27]
    return x, y

def compute_cost(x, y, w, b):
    totalCost = 0
    m = x.shape[0]
    for i in range(m):
        totalCost = totalCost + (((np.dot(w, x[i]) + b) - y[i]) ** 2)
    totalCost = totalCost / (2 * m)
    return totalCost


def compute_gradient(x, y, w, b):
    m = x.shape[0]
    n = x.shape[1]
    dj_dw = np.zeros(w.shape)
    dj_db = 0

    for i in range(m):
        f_wb = np.dot(w, x[i]) + b
        for j in range(n):
            dj_dw[j] = dj_dw[j] + ((f_wb - y[i]) * x[i][j])
        dj_db = dj_db + (f_wb - y[i])

    dj_dw = dj_dw / m
    dj_db = dj_db / m
    return dj_dw, dj_db

def gradient_descent(x, y, w_init, b_init, alpha, num_iters):
    
    for i in range(num_iters):
        dj_dw , dj_db = compute_gradient(x, y, w_init, b_init)

        w_init = w_init - alpha * dj_dw
        b_init = b_init - alpha * dj_db

        if (i % 1000 == 0):
            print(f"{i}\tCost: {compute_cost(x, y, w_init, b_init)}\tW: {w_init}\tb: {b_init}")
    
    return w_init, b_init



ws = pd.read_excel("data/student.xlsx")
x, y = intializeDataset()
w = np.zeros(x.shape[1])
b = 0
w, b = gradient_descent(x, y, w, b, 0.003, 10000)

np.savez("saved.npz", w=w, b=b)