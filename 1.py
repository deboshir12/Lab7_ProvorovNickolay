import numpy as np
import time
import random
import matplotlib.pyplot as plt
from matplotlib.animation import PillowWriter

def comparison(): # сравнивание стандартных списков и массивов в numpy
    m1,m2 = [],[]
    for i in range(1000000):
        m1.append(random.randint(1,100000))
    for i in range(1000000):
        m2.append(random.randint(1,100000))
        
    t_start_us = time.perf_counter()
    m3 = np.multiply(m1,m2)
    time_us = time.perf_counter() - t_start_us

    m4,m5 = np.array(m1, int),np.array(m2, int)

    t_start_np = time.perf_counter()
    m6 = np.multiply(m4,m5)
    time_np = time.perf_counter() - t_start_np

    if time_us > time_np: 
        print('numpy faster than standart')
    else:
        print('standat faster than numpy')


def histogramma(): # создание гистограммы 
    arr = np.genfromtxt('/Users/nikolajprovorov/Documents/dev/7lab/data2.csv', delimiter=',')
    arr = arr[1:]
    sulfate = np.array(arr[:,4], float)
    sulfate = sulfate[~np.isnan(sulfate)]
    
    fig = plt.figure(figsize=(10, 4))
    ax = plt.subplot(1,2,1)
    ax.hist(sulfate, 100, (100, 500),color= 'red', ec = 'blue')
    ax.grid()
    ax.set_title('Гистограмма')
    ax.set_xlabel('Sulfate')
    ax.set_ylabel('частота')
        
    ax1 = plt.subplot(1,2,2)
    ax1.hist(sulfate, 100, (100, 500),color= 'red', ec = 'blue', density= True)
    ax1.grid()
    ax1.set_title('Нормализованная гистограмма')
    ax1.set_xlabel('Sulfate')
    ax1.set_ylabel('частота')
    plt.show()
    
    print('Среднеквадратичное отклонение:\n' + str(np.std(sulfate)))
    
def plot3d(): # x∈(-3п;3п); y=x cos(x); z=sin(x)
    xs = np.linspace(-9.424, 9.424, 100)
    ys = np.cos(xs) * xs
    zs = np.sin(xs)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(xs, ys, zs, marker='x', c='red')
    plt.show()
    
def animation():
    fig = plt.figure()
    l, = plt.plot([], [])
    plt.xlim(-10, 10)
    plt.ylim((-1, 1))
    
    writer = PillowWriter(fps=15)

    xval = []
    yval = []

    with writer.saving(fig, "sin_function.gif", 100):
        for x in np.linspace(-10, 10, 100):
            xval.append(x)
            yval.append(np.sin(x))
            l.set_data(xval, yval)
            writer.grab_frame()

#comparison()
#histogramma()
#plot3d()
#animation()
