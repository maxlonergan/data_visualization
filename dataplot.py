'''
data visualization project
'''
import math
import glob
import numpy as np
import matplotlib.pyplot as plt
WIDTH = 50

def smoothed_array(arr):
    # smoothed_data = np.array([])
    smoothed_data = []
    array_len = len(arr)
    for i in range(len(arr)):
        if i >= 3 and i < array_len - 3:
            num = (arr[i-3] + 2 * arr[i-2] + 3 * arr[i-1] + 3 * arr[i] + 3 * arr[i+1] + 2 * arr[i+2] + arr[i+3])//15
            # smoothed_data = np.append(smoothed_data, smooth_point)
        else:
            num = arr[i]
        smoothed_data.append(num)
    return np.array(smoothed_data)

def plot(old, new, pdf):
    _,axes = plt.subplots(nrows=2)

    axes[0].plot(old)
    axes[0].set(title='Rough')

    axes[1].set(xlabel='Smooth')
    axes[1].plot(new)
    plt.savefig(pdf)

def analyze(file):
    file_dat = file
    file_pdf = file.replace('dat', 'pdf')
    raw_data = np.loadtxt(file)
    smoothed_data = smoothed_array(raw_data)
    pulses = []
    voltage_threshold = 100
    i = 0
    while i < len(smoothed_data) - 2:
        if smoothed_data[i + 2] - smoothed_data[i] > voltage_threshold:
            pulses.append(i)
            i += 1
            while i < len(smoothed_data) - 2 and smoothed_data[i + 1] > smoothed_data[i]:
                i += 1
        i += 1
    if not pulses:
        return
    output_string = f'{file_dat}:\n'
    for i in range(len(pulses)):
        start_position = pulses[i]
        real_width = WIDTH

        if i < len(pulses) - 1 and pulses[i] + real_width > pulses[i + 1]:
            real_width = pulses[i +1] - start_position
        real_width = min(real_width, len(smoothed_data) - start_position)
        area = int(sum(raw_data[start_position:start_position + real_width]))
        output_string += f'Pulse {i+1}: {start_position} ({area})\n'

    with open(file_dat[:-3] + 'out', 'w') as out:
        print(output_string, file=out, end='')

    print(len(smoothed_data))

    plot(raw_data, smoothed_data, file_pdf)
def main():
    for fname in glob.glob('*.dat'):
        analyze(fname)

main()
