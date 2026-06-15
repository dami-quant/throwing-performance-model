import statistics as stat
import matplotlib.pyplot as plt
import pandas as pd

THROW_COLS = [
    "best throw",
    "2nd best throw",
    "3rd best throw",
    "4th best throw",
    "5th best throw"
]
def best_throw(df):
    print("best_throw called")
    print("Type:", type(df))
    print("Columns:", df.columns.tolist())

    return df[THROW_COLS].max().max()

def improvement(df):
    """Calculate improvement from first to last throw"""
    # Get the best throw from each row
    throws = df[THROW_COLS].max(axis=1).tolist()
    
    change = throws[-1] - throws[0]
    
    if change > 0:
        return f"You improved by {change:.2f}m"
    else:
        return f"No improvement. You are {-change:.2f}m behind your best throw"

def average(df):
    return df[
        ["best throw", "2nd best throw", "3rd best throw", "4th best throw", "5th best throw"]
    ].to_numpy().mean()
def comparison(df):
    throws = df["best throw"].tolist()
    if len(throws) < 2:
        return "Need at least 2 throws for trend comparison"

    mid = len(throws) // 2

    first_half = throws[:mid]
    second_half = throws[mid:]

    avg1 = sum(first_half) / len(first_half)
    avg2 = sum(second_half) / len(second_half)

    if avg2 > avg1:
        return f"Increasing trend by {avg2 - avg1:.2f}m"
    else:
        return f"Declining trend by {avg1 - avg2:.2f}m"
def median(df):
    throws = df["best throw"].tolist()
    return f"Median: {stat.median(throws):.1f}m"
def consistency(df):
    throws = df["best throw"].tolist()
    if len(throws) < 2:
        return "Need at least 2 throws to measure consistency"

    std = stat.stdev(throws)
    if std < 0.5:
        return f"Very consistent performance (Low standard deviation) {std:.2f}"
    elif std < 0.7:
        return f"Moderately consistent performance (Moderate standard deviation) {std:.2f}"
    else:
        return f"High variability in performance (High standard deviation) {std:.2f}"    
    
def line_graph(df):
    plt.figure()
    throws = df["best throw"].tolist()
    plt.plot(throws, marker='o')

    plt.title("Shot Put Performance Over Time")
    plt.xlabel("Attempt number")
    plt.ylabel("Distance (m)")

    fig = plt.gcf()
    return fig
def histogram(df):
        plt.figure()
        throws = df["best throw"].tolist()
        plt.hist(throws, bins=5, edgecolor='black')

        plt.title("Distribution of Shot Put Throws")
        plt.xlabel("Distance (m)")
        plt.ylabel("Frequency")

        fig = plt.gcf()
        return fig
def improvement_visualisation(df):
        plt.figure()
        throws = df["best throw"].tolist()
        colors = ["green" if t > throws[0] else "red" for t in throws]

        plt.bar(range(len(throws)), throws, color=colors)

        plt.title("Improvement Tracking")
        plt.xlabel("Attempt")
        plt.ylabel("Distance (m)")

        fig = plt.gcf()
        return fig
def benchmark(df):
        plt.figure()
        throws = df["best throw"].tolist()
        avg = sum(throws) / len(throws)

        plt.plot(throws, marker='o', label="Throws")
        plt.axhline(avg, color='red', linestyle='--', label="Average")

        plt.title("Throws vs Average Performance")
        plt.xlabel("Attempt number")
        plt.ylabel("Distance (m)")
        plt.legend()

        fig = plt.gcf()
        return fig 
 
 
def strength_index(row):
    return (
        0.4 * row["squat"] +
        0.4 * row["deadlift"] +
        0.2 * row["bench"]
    ) / row["bodyweight"]

def technique_score(base_score, style):
    multipliers = {
        "spin": 1.1,
        "glide": 1.0,
        "standing": 0.9
    }
    return base_score * multipliers.get(str(style).strip().lower(), 1.0)

def fatigue_score(row):
    return (
        row["number of throws in past 3 days"] * 0.15 +
        row["number of gym sessions in past 3 days"] * 1.0 -
        row["number of rest days since"] * 0.8
    )




def predict_row(row, base_level):
    strength = strength_index(row)

    tech_base = pd.to_numeric(pd.Series([row["technique"]]), errors="coerce").iloc[0]
    if pd.isna(tech_base):
        tech_base = 1.0

    tech = technique_score(tech_base, row["style"])

    fatigue = max(0, fatigue_score(row))

    prediction = (
        base_level
        + (0.5 * strength)
        + (0.6 * tech)
        - (0.4 * fatigue)
    )

    return prediction





