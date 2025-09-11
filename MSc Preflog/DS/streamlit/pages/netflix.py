import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set full-page width
st.set_page_config(page_title="Custom Chart Builder", layout="wide")

st.title("📊 Matplotlib")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.subheader("Preview of Uploaded Data")
    st.dataframe(df)

    chart_type = st.selectbox("Choose chart type", ["Bar Chart", "Pie Chart", "Histogram", "Line Chart"])

    # Let user select column
    selected_column = st.selectbox("Select a column to visualize", df.columns)

    # Optional row filter
    unique_vals = df[selected_column].dropna().unique()

    if len(unique_vals) < 100:
        selected_rows = st.multiselect(f"Filter rows (values in '{selected_column}')", unique_vals, default=unique_vals)
        filtered_df = df[df[selected_column].isin(selected_rows)]
    else:
        filtered_df = df

    st.subheader("Generated Chart")

    # Draw charts based on type
    if chart_type == "Pie Chart":
        # Works well if the column is categorical
        pie_data = filtered_df[selected_column].value_counts()
        fig, ax = plt.subplots(figsize=(5, 5))
        ax.pie(pie_data, labels=pie_data.index, autopct="%1.1f%%", startangle=90)
        ax.axis("equal")
        st.pyplot(fig)

    elif chart_type == "Bar Chart":
        bar_data = filtered_df[selected_column].value_counts()
        st.bar_chart(bar_data)

    elif chart_type == "Histogram":
        if pd.api.types.is_numeric_dtype(filtered_df[selected_column]):
            fig, ax = plt.subplots(figsize=(6, 4))
            ax.hist(filtered_df[selected_column].dropna(), bins=20, color="skyblue", edgecolor="black")
            ax.set_xlabel(selected_column)
            ax.set_ylabel("Frequency")
            st.pyplot(fig)
        else:
            st.warning("Histogram requires a numeric column.")

    elif chart_type == "Line Chart":
        if pd.api.types.is_numeric_dtype(filtered_df[selected_column]):
            st.line_chart(filtered_df[selected_column])
        else:
            st.warning("Line chart requires a numeric column.")
else:
    st.info("Please upload a CSV file to begin.")
