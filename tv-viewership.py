import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("sb.csv", parse_dates=["date"])
df["year"] = df["date"].dt.year

# Add simulcasts together (1967 CBS + NBC, 2024 CBS + Nickelodeon)
viewers = df.groupby("year")["avg_viewers_millions"].sum()

fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(viewers.index, viewers.values, color="#1f4e9c")

ax.set_title("Super Bowl U.S. TV Viewership, 1967–2026", fontsize=16, weight="bold", loc="left")
ax.set_ylabel("Average viewers (millions)")
ax.spines[["top", "right"]].set_visible(False)
ax.grid(axis="y", alpha=0.3)
ax.set_axisbelow(True)

fig.text(0.125, 0.01, "Source: Nielsen via Wikipedia", fontsize=9, color="gray")
fig.savefig("superbowl_viewership.png", dpi=200, bbox_inches="tight")