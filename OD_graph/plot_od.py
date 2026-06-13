import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

full_df = pd.read_csv("_L.lactis vs pMGI OD graph - flat_data.csv")

tab10 = plt.colormaps["tab10"]
palette = {
    "L.lactis NZ9000": tab10(0),
    "L.lactis pMGI": tab10(1),
    "S.hominis": tab10(2),
}
sns.set_style("white")

time_cols = ["0 hr", "2hr", "4h4", "6hr", "8hr", "10hr", "24 h", "27 h", "30 h"]
time_map = dict(zip(time_cols, [0, 2, 4, 6, 8, 10, 24, 27, 30]))

long_df = full_df.melt(
    id_vars=["Concentration", "Sample", "Replicates"],
    value_vars=time_cols,
    var_name="Time_raw",
    value_name="OD600",
)
long_df["Time_hr"] = long_df["Time_raw"].map(time_map)

for conc in full_df["Concentration"].unique():
    subset = long_df[long_df["Concentration"] == conc]

    fig, ax = plt.subplots(figsize=(9, 5))

    sns.lineplot(
        data=subset,
        x="Time_hr",
        y="OD600",
        hue="Sample",
        palette=palette,
        marker="o",
        err_style="bars",
        err_kws={"capsize": 4},
        ax=ax,
    )

    ax.set_xlabel("Time (hr)")
    ax.set_ylabel("OD600")
    ax.set_xticks(range(0, 31, 2))
    ax.set_ylim(0, 2.5)

    sns.despine(ax=ax)

    legend = ax.get_legend()
    for text in legend.get_texts():
        text.set_fontstyle("italic")

    plt.tight_layout()
    safe_name = conc.replace("^", "pow").replace(" ", "_")
    filename = f"plot_{safe_name}.png"
    plt.savefig(filename, dpi=150)
    plt.close(fig)
    print(f"Saved {filename}")
