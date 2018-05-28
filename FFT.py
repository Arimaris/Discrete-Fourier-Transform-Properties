from numpy import fft
import numpy as np
from matplotlib import pyplot as plt

Nf = 64 # N- DFT size
fs = 64 # sampling frequency
f = 10 # one signal
t = np.arange(0,1,1/fs) # time-domain samples
deltaf = 1/2. # second nearby frequency

# keep x and y-axes on same respective scale
fig,ax = plt.subplots(2,1,sharex=True,sharey=True)
fig.set_size_inches((8,3))

x=np.cos(2*np.pi*f*t) + np.cos(2*np.pi*(f+2)*t) # 2 Hz frequency difference
X = fft.fft(x,Nf)/np.sqrt(Nf)
ax[0].stem(np.linspace(0,fs,Nf),np.abs(X),'-o')
ax[0].set_title(r'$\delta f = 2$ Hz, $T=1$ s',fontsize=18)
ax[0].set_ylabel(r'$|X(f)|$',fontsize=18)
ax[0].grid()
x=np.cos(2*np.pi*f*t) + np.cos(2*np.pi*(f+deltaf)*t) # delta_f frequency difference
X = fft.fft(x,Nf)/np.sqrt(Nf)
ax[1].stem(np.linspace(0,fs,Nf),abs(X),'-o')
ax[1].set_title(r'$\delta f = 1/2$ Hz, $T=1$ s',fontsize=14)
ax[1].set_ylabel(r'$|X(f)|$',fontsize=18)
plt.show()