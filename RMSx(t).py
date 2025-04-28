import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("SpekrumRMS.csv", 
                 delimiter=',', 
                 decimal='.', 
                 comment='#', 
                 header=None, 
                 encoding='latin1')

df.columns = ['Frequency_Hz', 'Amplitude_V', 'Phase_deg']
df['Frequency_kHz'] = df['Frequency_Hz'] / 1000

target_freq = 3.5
closest_idx = (df['Frequency_kHz'] - target_freq).abs().idxmin()
peak_freq_kHz = df['Frequency_kHz'][closest_idx]
peak_value = df['Amplitude_V'][closest_idx]

closest_4_5_idx = (df['Frequency_kHz'] - 4.5).abs().idxmin()
freq_4_5 = df['Frequency_kHz'][closest_4_5_idx]
amp_4_5 = df['Amplitude_V'][closest_4_5_idx]

plt.figure(figsize=(10, 5))
plt.plot(df['Frequency_kHz'], df['Amplitude_V'], color='firebrick')  

plt.plot(peak_freq_kHz, peak_value, 'o', color='black')
plt.axhline(peak_value, linestyle='--', color='gray', linewidth=1)
plt.text(2.52, peak_value + 0.015, "0.3243 V", va='bottom', ha='left', fontsize=10)

plt.plot(freq_4_5, amp_4_5, 'o', color='black')

xticks = list(plt.xticks()[0])
xticks += [3.5, 4.5]
xticks = sorted(set(xticks))
plt.xticks(xticks)

plt.title("Frekvensspekter (RMS)")
plt.xlabel("Frekvens [kHz]")
plt.ylabel("Amplitude [V RMS]")
plt.grid(True)
plt.ylim(0, 0.5)
plt.xlim(2.5, 4.5)
plt.tight_layout()
plt.show()
