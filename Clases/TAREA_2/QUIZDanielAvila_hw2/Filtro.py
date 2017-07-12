import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack as fft
import scipy.io.wavfile as wav

ss , datos = wav.read("violin.wav")
frec = fft.fftfreq(np.size(datos),1.0/ss)
datos_T = fft.fft(datos)

f1 = plt.figure(figsize=(10,6))
plt.plot(frec,abs(datos_T))
plt.title("Transformada de Fourier para el Violin")
plt.xlim(-10,np.max(frec))
plt.savefig("Violin.pdf")


def pasabanda(F,A):
	a = A.copy()
	f = F.copy()
	for i in range(np.size(f)):
		fi = f[i]
		if(abs(fi)>=1000 and abs(fi)<=2000):
			continue
		a[i] = 0
	return a
pasabanda = pasabanda(frec,datos_T)

f2 , ax = plt.subplots(2,1, sharex = True, sharey=True)
ax[0].plot(frec,abs(datos_T))
ax[0].set_title("Datos originales en espacio de frecuencias")
ax[1].plot(frec,abs(pasabanda))
ax[1].set_title("Filtro pasabanda")
plt.savefig("ViolinFiltro.pdf")




