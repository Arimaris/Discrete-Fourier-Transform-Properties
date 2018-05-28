from matplotlib import pyplot as plt
from matplotlib import image as img
print('Welcome to DFT Properties! The objective of this program is to visually demonstrate'
      ' the properties of the discrete Fourier Transform. ')
finished=False

while(finished==False):
    print('Options:\n'
      '1. View the signals g[n] and h[n].\n'
      '2. View the DFT properties table.\n'
      '3. View the linearity property.\n'
      '4. View the circular time-shifting property.\n'
      '5. View the circular frequency-shifting property.\n'
      '6. View the duality property.\n'
      '7. View the N-point circular convolution property.\n'
      '8. View the modulation property.\n'
      '9. View Parseval\'s theorem.\n'
      '10. Exit.')

    selection = int(input("Please select an option by typing the number beside it and pressing enter: "))
    #print("You chose option " + str(selection))

    if selection==3:
        left=img.imread('./Plots/LinearityLeft.png','r')
        right=img.imread('./Plots/LinearityRight.png','r')
        plt.figure(1)
        plt.figimage(left)
        plt.figure(2)
        plt.figimage(right)
        print("Now showing the linearity property. Close both figures to continue.")
        plt.show()
    elif selection==4:
        left=img.imread('./Plots/CircularTimeShiftingLeft.png','r')
        right=img.imread('./Plots/CircularTimeShiftingRight.png','r')
        plt.figure(1)
        plt.figimage(left)
        plt.figure(2)
        plt.figimage(right)
        print("Now showing the circular time-shifting property. Close both figures to continue.")
        plt.show()
    elif selection==5:
        left=img.imread('./Plots/CircularFrequencyShiftingLeft.png','r')
        right=img.imread('./Plots/CircularFrequencyShiftingRight.png','r')
        plt.figure(1)
        plt.figimage(left)
        plt.figure(2)
        plt.figimage(right)
        print("Now showing the circular frequency-shifting property. Close both figures to continue.")
        plt.show()
    elif selection==6:
        left=img.imread('./Plots/DualityLeft.png','r')
        right=img.imread('./Plots/DualityRight.png','r')
        plt.figure(1)
        plt.figimage(left)
        plt.figure(2)
        plt.figimage(right)
        print("Now showing the duality property. Close both figures to continue.")
        plt.show()
    elif selection==7:
        left=img.imread('./Plots/CircularConvolutionLeft.png','r')
        right=img.imread('./Plots/CircularConvolutionRight.png','r')
        plt.figure(1)
        plt.figimage(left)
        plt.figure(2)
        plt.figimage(right)
        print("Now showing the N-point circular convolution property. Close both figures to continue.")
        plt.show()
    elif selection==8:
        left=img.imread('./Plots/ModulationLeft.png','r')
        right=img.imread('./Plots/ModulationRight.png','r')
        plt.figure(1)
        plt.figimage(left)
        plt.figure(2)
        plt.figimage(right)
        print("Now showing the modulation property. Close both figures to continue.")
        plt.show()
    elif selection==9:
        left=img.imread('./Plots/ParsevalLeft.png','r')
        right=img.imread('./Plots/ParsevalRight.png','r')
        plt.figure(1)
        plt.figimage(left)
        plt.figure(2)
        plt.figimage(right)
        print("Now showing Parseval\'s theorem. Close both figures to continue.")
        plt.show()
    elif selection==10:
        print('Thank you for using DFT Properties!')
        finished=True
        break
    else:
        print('Please select a valid option.')

    done = int(input("Type 1 if you wish to continue or 0 to exit."))
    if done==0:
        print('Thank you for using DFT Properties!')
        finished=True