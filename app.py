import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Austin 4 Days",
    page_icon="🤘",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit chrome
st.markdown("""
<style>
#MainMenu, footer, header, .stDeployButton, .stToolbar { display:none !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }
section[data-testid="stSidebar"] { display:none !important; }
.stApp { background: #FAF8F4; }
</style>
""", unsafe_allow_html=True)

# ── PASSWORD ────────────────────────────────────────────────────
def check_password():
    if st.session_state.get("authenticated"):
        return True
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown("### Welcome to Austin 🤘")
        st.markdown("*Enter the password to view the itinerary.*")
        pwd = st.text_input("", type="password", placeholder="Password...", label_visibility="collapsed")
        if st.button("Enter →", use_container_width=True):
            if pwd == st.secrets["PASSWORD"]:
                st.session_state.authenticated = True
                st.rerun()
            else:
                st.error("Incorrect password.")
    return False

if not check_password():
    st.stop()

# ── LOAD AND RENDER HTML ────────────────────────────────────────
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Inject JS to fix anchor scroll inside Streamlit
scroll_fix = """
<script>
document.querySelectorAll('a[href^="#"]').forEach(a => {
  a.addEventListener('click', function(e) {
    e.preventDefault();
    const id = this.getAttribute('href').slice(1);
    const el = document.getElementById(id);
    if (el) el.scrollIntoView({ behavior: 'smooth', block: 'start' });
  });
});
</script>
"""
html = html.replace("</body>", scroll_fix + "</body>")

components.html(html, height=9000, scrolling=False)
