import streamlit as st

st.title("Zone Data Streamlit Applications Dashboard")

# List of Streamlit app URLs with embed parameter
streamlit_apps = {
    "75 Minute Data": "https://zonedatatodb75minute.streamlit.app/?embed=true",
    "Daily Data": "https://zonedatatodbdaily.streamlit.app/?embed=true",
    "Monthly Data": "https://zonedatatodbmonthly.streamlit.app/?embed=true",
    "Weekly Data": "https://zonedatatodbweekly.streamlit.app/?embed=true"
}

# Display each application in an iframe
for app_name, app_url in streamlit_apps.items():
    st.subheader(app_name)
    st.components.v1.html(
        f'<iframe src="{app_url}" width="100%" height="600" frameborder="0" allowfullscreen></iframe>',
        height=600,
    )
