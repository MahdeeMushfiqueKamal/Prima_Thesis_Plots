import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from scipy.interpolate import make_interp_spline

df = pd.read_csv("CFU  - Sheet5.csv")

sns.set_theme(style="white")
colors = sns.color_palette("tab10")

fig, ax = plt.subplots(figsize=(6, 5))

strains = ["L.lactis", "L.lactis pMGI", "S.hominis"]

for i, strain in enumerate(strains):
    ax.plot(df["Time"], df[strain], marker="o", label=strain, color=colors[i])

ax.set_xlabel("Time (h)")
ax.set_ylabel("$\\log_{10}$ CFU/mL")
ax.set_xticks(range(0, int(df["Time"].max()) + 1, 2))
ax.set_ylim(7.5, 14)

legend = ax.legend()
for text in legend.get_texts():
    text.set_fontstyle("italic")

plt.tight_layout()
plt.savefig("cfu_plot.png", dpi=150, bbox_inches="tight")


# generate the same plot, with smooth lines instead of points
fig, ax = plt.subplots(figsize=(6, 5))

for i, strain in enumerate(strains):
    x = df["Time"].values
    y = df[strain].values
    x_smooth = np.linspace(x.min(), x.max(), 300)
    spline = make_interp_spline(x, y, k=3)
    y_smooth = spline(x_smooth)
    ax.plot(x_smooth, y_smooth, label=strain, color=colors[i])
    ax.plot(x, y, marker="o", linestyle="none", color=colors[i])

ax.set_xlabel("Time (h)")
ax.set_ylabel("$\\log_{10}$ CFU/mL")
ax.set_xticks(range(0, int(df["Time"].max()) + 1, 2))
ax.set_ylim(7.5, 14)

legend = ax.legend()
for text in legend.get_texts():
    text.set_fontstyle("italic")

plt.tight_layout()
plt.savefig("cfu_plot_smoothed.png", dpi=150, bbox_inches="tight")
