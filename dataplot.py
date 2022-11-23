'''
data visualization project
'''

import numpy as np
import matplotlib.pyplot as plt
import glob 

data_one = np.loadtxt('2_Record2308.dat')
data_two = np.loadtxt('2_Record3388.dat')
data_three = np.loadtxt('as_ch01-0537xx_Record1042.dat')

xpoints = np.array([0,6])
ypoints = np.array([0,250])


plt.plot(data_one)
# plt.plot(data_two)
# # plt.savefig('2_Record2308.pdf')
plt.show()

# def main():
#     for fname in glob.glob('*.dat'):
#         analyze(fname)

# def analyze(file):
#     data = np.loadtxt(file)
#     plt.plot(data)
#     plt.show()