import pandas as pd
import matplotlib.pyplot as plt

df_compare = pd.read_csv("Sammlikningfrekvens.csv", delimiter=',', decimal='.', comment='#', header=None, encoding='latin1')
df_compare.columns = ['Time_s', 'x_t', 'x_hat_t']

mask = (df_compare['Time_s'] >= -0.005) & (df_compare['Time_s'] <= 0.005)
df_zoomed = df_compare[mask].copy()
df_zoomed['Time_ms'] = df_zoomed['Time_s'] * 1000  # konverter til millisekunder

plt.figure(figsize=(12, 5))
plt.plot(df_zoomed['Time_ms'], df_zoomed['x_t'], label='x(t) – Kanal 1 (1.75 kHz)', color='navy')
plt.plot(df_zoomed['Time_ms'], df_zoomed['x_hat_t'], label='x̂(t) – Kanal 2 (3.5 kHz)', color='darkorange')

plt.title("x(t) og x̂(t) med tilhørende frekvenser")
plt.xlabel("Tid [ms]")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.xlim(-5, 5)
plt.tight_layout()
plt.show()
