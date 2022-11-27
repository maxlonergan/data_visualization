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
    _,axes = plt.subplots(nrows=2)

    axes[0].plot(old)
    axes[0].set(title='Rough')

    axes[1].set(xlabel='Smooth')
    axes[1].plot(new)
    plt.savefig(pdf)

def analyze(file):
    file_name = file.replace('dat', 'pdf')
    data = np.loadtxt(file)
    smoothed_data = smoothed_array(data)
    for num in smoothed_data:
        y = num
        y_one = 4
    plot(data, smoothed_data, file_name)

# def main():
#     for fname in glob.glob('*.dat'):
#         analyze(fname)

# main()


smoothed_data = np.array([1,2,3,4,5,6,7,8,9])
split_data = np.split(smoothed_data, 3)
for arr in split_data:
    for num in arr:
        pass
