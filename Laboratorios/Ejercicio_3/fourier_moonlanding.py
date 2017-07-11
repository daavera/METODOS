import matplotlib.pyplot as plt
import numpy as np
import matplotlib.mlab as mlab

datos = plt.imread('moonlanding.png')

#Transformada
tf = np.fft.fft2(datos)

#FILTRO
F = tf.copy()
F[50:-50, :] = 0
F[:50,50:-50] =0
F[-50:,50:-50] =0

datos_F = np.fft.ifft2(F)

fig , ax = plt.subplots(2,2)
ax[0,0].imshow(datos, cmap='gray')
ax[0,0].set_title('Original Image')
power1 = abs(tf)**2
img1= ax[0,1].imshow(power1,cmap='GnBu')
ax[0,1].set_title('Power spectrum')
power_cut = 95.0
clipped_power = mlab.prctile(power1.flatten(), power_cut)
img1.set_clim(0, clipped_power)

ax[1,0].imshow(datos_F.real,cmap='gray')
ax[1,0].set_title('Reconstructed Image')
power2 = abs(F)**2
img2 = ax[1,1].imshow(abs(F)**2,cmap='GnBu')
ax[1,1].set_title('Filtered spectrum')
clipped_power = mlab.prctile(power1.flatten(), power_cut)
img2.set_clim(0, clipped_power)
plt.tight_layout()
plt.savefig('moon_landing.png')