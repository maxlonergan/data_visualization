'''
data visualization project
'''
import math
import glob
import numpy as np
import matplotlib.pyplot as plt
WIDTH = 50

def smoothed_array(arr):
    smoothed_data = np.array([])
    for i in range(3,len(arr)-3):
        smooth_point = math.floor((arr[i-3] + 2 * arr[i-2] + 3 * arr[i-1] + 3 * arr[i] + 3 * arr[i+1] + 2 * arr[i+2] + arr[i+3])/15)
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
    raw_data = np.loadtxt(file)
    smoothed_data = smoothed_array(raw_data)
    pulses = []
    voltage_threshold = 100

    for i in range(len(smoothed_data)-2):
        y = abs(smoothed_data[i])
        y_plus_two = abs(smoothed_data[i+2])
        if y_plus_two - y > voltage_threshold:
            pulse_start = i
            pulses.append(pulse_start)

    # for i in range(len(pulses)):
    #     start_position = pulses[i]
    #     real_width = WIDTH

    #     if i < len(pulses) - 1 and pulses[i] + real_width > pulses[i + 1]:
    #         real_width = pulses[i +1] - start_position
    #     real_width = min(real_width, len(smoothed_data) - start_position)
    #     area = int(sum(raw_data[start_position:start_position + real_width]))
    #     output_string = f'Pulse {i+1}: {start_position+1} ({area})\n'
    #     print(output_string)

    for i in range(1016,1021):
        print(smoothed_data[i])
    print(pulses)
    plot(raw_data, smoothed_data, file_name)

def main():
    for fname in glob.glob('*.dat'):
        analyze(fname)

# main()


analyze('2_Record2308.dat')





