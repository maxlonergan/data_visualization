'''
data visualization project
'''
import math
import glob
import numpy as np
import matplotlib.pyplot as plt


def smoothed_array(arr):
    smoothed_data = np.array([])
    for i in range(3,len(arr)-4):
        smooth_point = math.floor((arr[i-3]+arr[i-2]+arr[i-1]+arr[i]+arr[i+1]+arr[i+2]+arr[i+3])/15)
        smoothed_data = np.append(smoothed_data, smooth_point)
    return smoothed_data

def plot(old, new, pdf):
    plt.subplot(2,1,1)
    plt.plot(old)
    plt.title('Rough')
    plt.subplot(2,1,2)
    
    plt.plot(new)
    plt.xlabel('Smooth')
    plt.savefig(pdf)

def analyze(file):
    file_name = file.replace('dat', 'pdf')
    data = np.loadtxt(file)
    smoothed_data = smoothed_array(data)
    plot(data, smoothed_data, file_name)
    # plt.subplot(2,1,1)
    # plt.plot(data)
    # plt.title('Rough')
    # plt.subplot(2,1,2)
    # plt.plot(smoothed_data)
    # plt.xlabel('Smooth')
    # plt.savefig(file_name)
    

def main():
    for fname in glob.glob('*.dat'):
        analyze(fname)

main()

