import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("CFU  - Sheet5.csv")

sns.set_theme(style="white")
colors = sns.color_palette("tab10")

fig, ax = plt.subplots(figsize=(8, 5))

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
sns.despine()

plt.tight_layout()
plt.savefig("cfu_plot.png", dpi=150, bbox_inches="tight")
