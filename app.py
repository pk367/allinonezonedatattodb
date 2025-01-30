import streamlit as st

st.title("Zone Data Streamlit Applications Dashboard")

# List of Streamlit app URLs
streamlit_apps = {
    "75 Minute Data": "https://zonedatatodb75minute.streamlit.app/",
    "Daily Data": "https://zonedatatodbdaily.streamlit.app/",
    "Monthly Data": "https://zonedatatodbmonthly.streamlit.app/",
    "Weekly Data": "https://zonedatatodbweekly.streamlit.app/"
}

# Display each application in an iframe
for app_name, app_url in streamlit_apps.items():
    st.subheader(app_name)
    st.components.v1.iframe(app_url, height=600, scrolling=True)
