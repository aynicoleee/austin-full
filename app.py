import streamlit as st

st.set_page_config(
    page_title="Austin 4 Days",
    page_icon="🤘",
    layout="wide"
)

def check_password():
    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False

    if st.session_state.authenticated:
        return True

    st.markdown("""
        <style>
        .block-container { max-width: 400px; margin: auto; padding-top: 15vh; }
        h2 { font-family: serif; text-align: center; }
        p.sub { text-align: center; color: #7A7670; font-size: 14px; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("## Welcome to Austin 🤘")
    st.markdown('<p class="sub">Enter the password to view the itinerary.</p>', unsafe_allow_html=True)

    pwd = st.text_input("Password", type="password", placeholder="Enter password...")

    if st.button("Enter", use_container_width=True):
        if pwd == st.secrets["PASSWORD"]:
            st.session_state.authenticated = True
            st.rerun()
        else:
            st.error("Incorrect password. Try again.")

    return False

if check_password():
    with open("index.html", "r", encoding="utf-8") as f:
        html = f.read()
    st.components.v1.html(html, height=5000, scrolling=True)
