import pandas as pd
import matplotlib.pyplot as plt

df_rms_v2 = pd.read_csv("RMSx_hat(t).v2.csv", delimiter=',', decimal='.', comment='#', header=None, encoding='latin1')
df_rms_v2.columns = ['Time_s', 'RMS']

rms_value_v2 = 0.32866

plt.figure(figsize=(10, 4))
plt.plot(df_rms_v2['Time_s'], df_rms_v2['RMS'], label='RMS-signal', color='teal')
plt.axhline(rms_value_v2, color='crimson', linestyle='--', linewidth=1.5, label=f'Målt RMS = {rms_value_v2:.5f} V')

text_x = df_rms_v2['Time_s'].iloc[int(len(df_rms_v2) * 0.8)]
plt.text(text_x, rms_value_v2 + 0.005, f"{rms_value_v2:.5f} V", color='crimson', ha='left')

plt.title("RMS-signal med målt verdi. x_hat(t)")
plt.xlabel("Tid [s]")
plt.ylabel("Amplitude [V RMS]")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
