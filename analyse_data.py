import pandas as pd
import matplotlib.pyplot as plt

CSV_FILE = "teamstats.csv"
BASE_YEAR = 2018
END_YEAR = 2022

# Loading dataset
df = pd.read_csv(CSV_FILE)

# Aggregating the duplicate rows (by adding totals, average percentages)
agg_funcs = {
    "gp":"sum","w":"sum","l":"sum","win_percent":"mean","ppg":"mean","fgm":"mean","fga":"mean","fg_percent":"mean",
    "threepoint_fgm":"mean","threepoint_fga":"mean","threepoint_fg_percent":"mean","ftm":"mean","fta":"mean","ft_percent":"mean",
    "oreb":"mean","dreb":"mean","reb":"mean","ast":"mean","tov":"mean","stl":"mean","blk":"mean","pf":"mean","pfd":"mean"
}
team_year = (
    df.groupby(["team","season"], as_index=False)
      .agg(agg_funcs)
)

# 1) Improvement 2018 -> 2022
base = team_year[team_year["season"] == BASE_YEAR][["team","win_percent"]].rename(columns={"win_percent": f"winpct_{BASE_YEAR}"})
end  = team_year[team_year["season"] == END_YEAR][["team","win_percent"]].rename(columns={"win_percent": f"winpct_{END_YEAR}"})
improve = (
    end.merge(base, on="team", how="inner")
       .assign(improvement=lambda d: d[f"winpct_{END_YEAR}"] - d[f"winpct_{BASE_YEAR}"])
       .sort_values("improvement", ascending=False, ignore_index=True)
)

# 2) Top 3 teams by total wins
total_wins = (
    team_year.groupby("team", as_index=False)["w"].sum()
             .rename(columns={"w":"total_wins"})
             .sort_values("total_wins", ascending=False, ignore_index=True)
)

# 3) Correlations
num = team_year.select_dtypes("number").copy()
if "season" in num.columns:
    num = num.drop(columns=["season"])
corr = num.corr(numeric_only=True)
pos_corr = corr["win_percent"].drop(labels=["win_percent"]).sort_values(ascending=False)
neg_corr = pos_corr.sort_values(ascending=True)

# results to be printed
print("\n=== MOST IMPROVED (2018 → 2022) ===")
print(improve.head(3).to_string(index=False))

print("\n=== TOP 3 TEAMS BY TOTAL WINS ===")
print(total_wins.head(3).to_string(index=False))

print("\n=== STRONGEST POSITIVE CORRELATIONS WITH WIN% ===")
print(pos_corr.head(5).to_string())

print("\n=== STRONGEST NEGATIVE CORRELATIONS WITH WIN% ===")
print(neg_corr.head(5).to_string())

# Saving the correlation plot
plt.figure(figsize=(10,8))
plt.imshow(corr, cmap="coolwarm", interpolation="none")
plt.colorbar(label="Correlation")
plt.xticks(range(len(corr.columns)), corr.columns, rotation=90)
plt.yticks(range(len(corr.columns)), corr.columns)
plt.title("Correlation Matrix of WNBA Stats")
plt.tight_layout()
plt.savefig("correlation_plot.png")
plt.close()

print("\nSaved correlation plot as correlation_plot.png")
