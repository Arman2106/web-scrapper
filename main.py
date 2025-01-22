import streamlit as st
import pandas as pd
import numpy as np

# Set page configuration
st.set_page_config(
    page_title="Data Analysis App",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Add a custom header
st.markdown(
    """
    <style>
    .main-header {
        font-size: 40px;
        color: #4CAF50;
        text-align: center;
        font-weight: bold;
        margin-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)
st.markdown('<p class="main-header">📊 Data Analysis Web App</p>', unsafe_allow_html=True)

# Sidebar
st.sidebar.header("Upload Your File")
uploaded_file = st.sidebar.file_uploader("Upload a CSV File", type=["csv"])

# Sidebar: Customize appearance
st.sidebar.markdown("---")
st.sidebar.subheader("About This App")
st.sidebar.info("This app allows you to upload a CSV file, analyze the data, and visualize it interactively.")

# Main Content
if uploaded_file:
    # Read and process the data
    df = pd.read_csv(uploaded_file)

    # Layout with two columns
    col1, col2, col3 = st.columns(3)

    # Display a dataset overview
    col1.subheader("Header of the dataset")
    col1.dataframe(df.head(), height=300)

    # Display basic statistics
    col2.subheader("Dataset Statistics")
    col2.dataframe(df.describe())

    # Display tail of Dataset
    col3.subheader("Tail of the Dataset")
    col3.dataframe(df.tail(), height=300)

    # Metrics display
    st.markdown("### Key Metrics")
    st.write("---")
    total_rows = len(df)
    total_columns = len(df.columns)
    st.columns(3)[1].metric("Total Rows", f"{total_rows}")
    st.columns(3)[2].metric("Total Columns", f"{total_columns}")

    # Add visualization options
    st.markdown("### Visualization")
    st.write("---")
    selected_column = st.selectbox("Select a column for visualization", df.columns)
    chart_type = st.radio("Choose a chart type", ["Line Chart", "Bar Chart", "Area Chart", "plotly chart"])

    if chart_type == "Line Chart":
        st.line_chart(df[selected_column])
    elif chart_type == "Bar Chart":
        st.bar_chart(df[selected_column])
    elif chart_type == "Area Chart":
        st.area_chart(df[selected_column])
    elif chart_type == "plotly Chart":
        st.plotly_chart(df[selected_column])

else:
    # Display a message for no uploaded file
    st.markdown("### Please upload a CSV file to get started! 📂")
    st.image("https://via.placeholder.com/600x400?text=Upload+CSV", use_column_width=True)
