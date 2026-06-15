import pandas as pd
import streamlit as st

import pandas as pd
import streamlit as st
from shotput_Statistics import (
    best_throw, improvement, average, consistency, comparison,
    line_graph, histogram, benchmark, improvement_visualisation, predict_row, median
)

# ============ PAGE CONFIG ============
st.set_page_config(page_title="Shot Put Analytics", layout="wide")
# ============ LOAD DATA ============
try:
    df = pd.read_excel("shotput_data.xlsx")
    df.columns = df.columns.str.strip().str.lower()
except FileNotFoundError:
    st.error("Error: shotput_data.xlsx not found")
    st.stop()

# ============ SIDEBAR NAVIGATION ============
page = st.sidebar.radio("Select Section", ["Overview", "Statistics", "Visualizations", "Predictions"])

# ============ OVERVIEW PAGE ============
if page == "Overview":
    st.title("Shot Put Performance Dashboard")

    #=========== EDITABLE DATA ============
    st.subheader("Original Data")
    st.dataframe(df)

  
    st.subheader("Edit Your Data")

    edited_df = st.data_editor(
        df,
        num_rows="dynamic"
    )

    st.subheader("Preview After Editing")
    st.dataframe(edited_df)

    
    if st.button("Save changes to Excel"):

        edited_df.to_excel("shotput_data.xlsx", index=False)

        st.success("Saved successfully to shotput_data.xlsx!")



# ============ STATISTICS PAGE ============
elif page == "Statistics":
    st.header("Performance Statistics")
    st.write(f"Best throw: {best_throw(df):.2f}")
    st.write(f"Improvement: {improvement(df)}")
    st.write(f"Average: {average(df):.2f}")
    st.write(f"Median: {median(df)}")
    st.write(f"Consistency: {consistency(df)}")
    st.write(f"Comparison: {comparison(df)}")

# ---------------- VISUALISATIONS ----------------
elif page == "Visualizations":    
    st.header("Visualizations")

    st.pyplot(line_graph(df))
    st.pyplot(histogram(df))
    st.pyplot(benchmark(df))
    st.pyplot(improvement_visualisation(df))

# ---------------- PREDICTION ----------------
elif page == "Predictions":
    st.header("Predictions")
    base_level = best_throw(df)

    df["prediction"] = df.apply(
        lambda row: predict_row(row, base_level),
        axis=1
    )

    df["target"] = df[
        ["best throw", "2nd best throw", "3rd best throw", "4th best throw", "5th best throw"]
    ].mean(axis=1)

    df["error"] = df["prediction"] - df["target"]

    st.subheader("Prediction Results")
    st.dataframe(df[["prediction", "target", "error"]])

