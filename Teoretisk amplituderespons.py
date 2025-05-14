import numpy as np
import matplotlib.pyplot as plt

R = 100000        
L = 100e-3         
C = 20e-9      

frequencies = np.logspace(2, 5, 1000)  
omega = 2 * np.pi * frequencies
j = 1j 

teller = j * omega * L
nevner = j * omega * L + R * (1 - (omega**2) * L * C)
H = teller / nevner
amplitude_db = 20 * np.log10(np.abs(H))

plt.figure(figsize=(10, 6))
plt.semilogx(frequencies, amplitude_db, color='blue', label='Amplituderespons')
plt.title("Teoretisk Amplituderespons")
plt.xlabel("Frekvens (Hz)")
plt.ylabel("Amplitude (dB)")
plt.grid(True, which="both", ls="--")
plt.legend()
plt.show()
