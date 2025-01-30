import streamlit as st

st.set_page_config(layout="wide")  # Enables wide layout for better display

st.title("Zone Data Streamlit Applications Dashboard")

# List of Streamlit app URLs with embed parameter
streamlit_apps = {
    "75 Minute Data": "https://zonedatatodb75minute.streamlit.app/?embed=true",
    "Daily Data": "https://zonedatatodbdaily.streamlit.app/?embed=true",
    "Monthly Data": "https://zonedatatodbmonthly.streamlit.app/?embed=true",
    "Weekly Data": "https://zonedatatodbweekly.streamlit.app/?embed=true"
}

# Responsive grid layout for iframes
cols = st.columns(2)  # Two-column layout for better visualization

for i, (app_name, app_url) in enumerate(streamlit_apps.items()):
    with cols[i % 2]:
        st.subheader(app_name)
        st.write(
            f'<iframe src="{app_url}" width="100%" height="300" frameborder="0"></iframe>', 
            unsafe_allow_html=True
        )
