import streamlit as st

# Set up the page configuration
st.set_page_config(
    page_title="Main Page",
    page_icon="👋",
)

pages = [
    st.Page("1_welcome.py", title="Play", default=True, icon="🤗"),
    st.Page("2_play.py", title="Game", icon="🎮"),
    st.Page("3_stats.py", title="Statistics", icon="📊"),
    ]

pg = st.navigation(pages)

pg.run()

