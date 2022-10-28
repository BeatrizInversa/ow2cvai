# This is a sample Python script.
import cv2
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'A, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('tebi')
    asset_path = './assets/img/'
    image = cv2.imread(asset_path + 'valtest.jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    RMatrix = cv2.cornerHarris(gray, 3, 3, 0.04)
    plt.imshow(image, cmap='gray')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
