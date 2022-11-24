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

def analyze(file):
    file_name = file
    print(file_name)
    data = np.loadtxt(file)
    smoothed_data = smoothed_array(data)
    plt.plot(data)
    plt.plot(smoothed_data)
    # plt.savefig()

def main():
    for fname in glob.glob('*.dat'):
        analyze(fname)

main()

# plt.plot(data_one)
# plt.plot(data_two)
# plt.show()

