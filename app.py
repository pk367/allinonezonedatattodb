import streamlit as st

st.set_page_config(layout="wide")  # Enables wide layout for better display

st.title("Zone Data Streamlit Applications Dashboard")

# List of Streamlit app URLs with embed parameter
streamlit_apps = {
    "1 Minute Data": "https://zonedatatodb75minute.streamlit.app/?embed=true",
    "3 Minute Data": "https://zonedatatodb75minute.streamlit.app/?embed=true",
    "5 Minute Data": "https://zonedatatodb75minute.streamlit.app/?embed=true",
    "10 Minute Data": "https://zonedatatodb75minute.streamlit.app/?embed=true",
    "15 Minute Data": "https://zonedatatodb75minute.streamlit.app/?embed=true",
    "30 Minute Data": "https://zonedatatodb75minute.streamlit.app/?embed=true",
    "1 Hour Data": "https://zonedatatodb75minute.streamlit.app/?embed=true",
    "75 Minute Data": "https://zonedatatodb75minute.streamlit.app/?embed=true",
    "2 Hour Data": "https://zonedatatodb75minute.streamlit.app/?embed=true",
    "125 Minute Data": "https://zonedatatodb75minute.streamlit.app/?embed=true",
    "Daily Data": "https://zonedatatodbdaily.streamlit.app/?embed=true",
    "Monthly Data": "https://zonedatatodbmonthly.streamlit.app/?embed=true",
    "Weekly Data": "https://zonedatatodbweekly.streamlit.app/?embed=true"
}

# Define the number of columns for the grid layout
num_columns = 4
cols = st.columns(num_columns)

# Adjust iframe size for better fit
iframe_height = 200

# Display iframes in a grid layout
for i, (app_name, app_url) in enumerate(streamlit_apps.items()):
    col_index = i % num_columns
    with cols[col_index]:
        st.subheader(app_name)
        st.markdown(
            f'<iframe src="{app_url}" width="100%" height="{iframe_height}" frameborder="0"></iframe>', 
            unsafe_allow_html=True
        )
