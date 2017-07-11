#TAREA 2 - Fourier
import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav

#Datos
ss_DO, DO = wav.read('Do.wav')
ss_SOL ,SOL = wav.read('Sol.wav')

#Transformada y tranformada inv. de Fourier propia
def Fourier (y):
    t = np.arange(np.size(y))
    N = np.size(y)
    n = np.arange(0,N,1).reshape(-1,1)
    R = np.exp(-2*np.pi*1j*n*t/N)
    return np.dot(R,y)

def Fourier_inversa (y):
    t = np.arange(np.size(y))
    N = np.size(y)
    n = np.arange(0,N,1).reshape(-1,1)
    R = np.exp(2*np.pi*1j*n*t/N)
    return np.dot(R,y)

#Datos con t.fourier
DO_F = np.fft.fft(DO)
f_DO = np.fft.fftfreq(np.size(DO),1/ss_DO)
SOL_F = np.fft.fft(SOL)
f_SOL = np.fft.fftfreq(np.size(SOL),1/ss_SOL)

#FILTROS
###filtro 1
def f_mayor(f_I,A_I):
    A = A_I.copy()
    F = f_I.copy()
    A_max = np.max(abs(A))
    i_max = np.where(abs(A) > A_max-0.1)[0]
    for i in i_max:
        index = np.arange(i-100,i+100,1)
        #Al igualarlo simpemente a cero quedaba un poco cortado.
        A[index] = 0
    return A
###filtro 2
def f_1000HZ(f_I,A_I):
    A = A_I.copy()
    F = f_I.copy()
    index = np.where(abs(F) > 1000)[0]
    A[index] = 0 
    return A
A_filtro1 = f_mayor(f_DO,DO_F)
A_filtro2 = f_1000HZ(f_DO,DO_F)

#Grafica con filtros
f1 , ax = plt.subplots(3,1,figsize=(10,6), sharex=True)
ax[0].plot(f_DO, abs(DO_F), color='greenyellow')
ax[0].set_title('Transformada de Fourier',fontweight="bold", fontsize=14)
ax[1].plot(f_DO,abs(A_filtro1), color='springgreen')
ax[1].set_title('Filtro para la frecuencia con mayor amplitud',fontweight="bold", fontsize=14)
ax[2].plot(f_DO,abs(A_filtro2), color='orangered')
ax[2].set_title('Filtro para frecuencias superiores a 1000Hz',fontweight="bold", fontsize=14)
#---
ax[0].ticklabel_format(style='sci',scilimits=(1,6),axis='both')
ax[1].ticklabel_format(style='sci',scilimits=(1,6),axis='both')
ax[2].ticklabel_format(style='sci',scilimits=(1,6),axis='both')
ax[1].set_ylabel('Amplitudes')
ax[2].set_xlabel('Frecuencia (Hz)', fontsize=10)
XLIMS = [[0, 3000]] * 3
for j, xlim in enumerate(XLIMS):
    ax[j].set_xlim(xlim)
f1.tight_layout()
plt.savefig('DoFiltros.pdf')

#DO to SOL
index = np.where(f_DO == 260)
YA = False
new_ssDO = ss_DO
new_fDO = 0
while not(YA):
    new_fDO = np.fft.fftfreq(np.size(DO),1/new_ssDO)
    if(new_fDO[index] > 390 and new_fDO[index] < 392 ):
        YA = not(YA)
    else:
        new_ssDO = new_ssDO+1

f2 , ax1 = plt.subplots(1,1,figsize=(10,6))
ax1.ticklabel_format(style='sci',scilimits=(1,6),axis='both')
ax1.set_title('Comparación entre SOL natural y artificial')
ax1.plot(new_fDO,abs(DO_F), label='SOL artificial')
ax1.plot(f_SOL,abs(SOL_F), label='SOL')
ax1.set_xlim([-7500,7500])
ax1.legend(loc='best')
plt.savefig('DoSol.pdf')

#ARCHIVOS .WAV
###Datos con la transformada inversa
DO_pico = np.fft.ifft(A_filtro1)
DO_pasabajos = np.fft.ifft(A_filtro2)
###Generacion de archivos .wav
wav.write('DO_pico.wav', ss_DO, DO_pico.astype(DO.dtype))
wav.write('DO_pasabajos.wav', ss_DO, DO_pasabajos.astype(DO.dtype))
wav.write('DoSol.wav', new_ssDO, DO)

#Genera una advertencia, sin embargo era la 
# unica forma de que no se escucharan mal los sonidos.
