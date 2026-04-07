import streamlit as st

st.set_page_config(
    page_title="Austin 4 Days",
    page_icon="🤘",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ── STYLES ─────────────────────────────────────────────────────
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=DM+Sans:wght@300;400;500;600&family=DM+Serif+Display:ital@0;1&display=swap" rel="stylesheet">
<style>
/* Hide Streamlit chrome */
#MainMenu, footer, header, .stDeployButton { display:none !important; }
.block-container { padding: 0 !important; max-width: 100% !important; }
section[data-testid="stSidebar"] { display:none; }

:root {
  --c1: #E8602A; --c2: #0FA88F; --c3: #E84470; --c4: #3D2FA0;
  --olive: #6B7C3F; --dark: #1A1814; --off: #FAF8F4;
  --cream: #F2EFE8; --gray: #7A7670; --light: #E8E4DC;
}
body { background: var(--off); color: var(--dark); font-family: 'DM Sans', sans-serif; }

.hero { background:var(--cream); padding:56px 48px 64px; border-bottom:2px solid var(--light); }
.hero h1 { font-family:'DM Serif Display',serif; font-size:clamp(40px,6vw,80px); font-weight:400; line-height:.95; letter-spacing:-.03em; margin-bottom:10px; }
.hero .sub { font-size:15px; font-weight:600; color:var(--olive); margin-bottom:6px; }
.hero .dates { font-size:13px; color:var(--gray); letter-spacing:.08em; font-weight:600; }

.sticky-nav { position:sticky; top:0; z-index:999; background:white; display:flex; border-bottom:2px solid var(--light); box-shadow:0 2px 8px rgba(0,0,0,.05); }
.sticky-nav a { flex:1; padding:14px 8px; text-align:center; text-decoration:none; border-bottom:3px solid transparent; transition:all .15s; display:block; }
.sticky-nav a:hover { opacity:.7; }
.sticky-nav a .num { display:block; font-size:9px; letter-spacing:.2em; text-transform:uppercase; color:var(--gray); margin-bottom:2px; }
.sticky-nav a .name { display:block; font-family:'DM Serif Display',serif; font-size:13px; }
.nav-thu { color:var(--c1) !important; border-bottom-color:var(--c1) !important; }
.nav-fri { color:var(--c2) !important; }
.nav-sat { color:var(--c3) !important; }
.nav-sun { color:var(--c4) !important; }

.legend { background:var(--cream); padding:10px 48px; display:flex; gap:16px; border-bottom:1px solid var(--light); flex-wrap:wrap; }
.tag { padding:2px 9px; border-radius:20px; font-size:8px; font-weight:500; letter-spacing:.1em; text-transform:uppercase; display:inline-block; }
.tag-r { background:#D4EDDA; color:#1A6B35; }
.tag-c { background:#FCE8D5; color:#A03B0A; }
.tag-t { background:#FFF3CD; color:#856404; }

.day { padding:0 0 60px; border-bottom:2px solid var(--light); }
.day-header { padding:40px 48px 32px; }
.day-label { font-size:10px; font-weight:500; letter-spacing:.2em; text-transform:uppercase; margin-bottom:8px; }
.day-header h2 { font-family:'DM Serif Display',serif; font-size:clamp(28px,4vw,48px); font-weight:400; line-height:1; letter-spacing:-.02em; }
.day-header h2 em { font-style:italic; }

.timeline { padding:0 48px; position:relative; }
.timeline::before { content:''; position:absolute; left:80px; top:0; bottom:0; width:2px; background:var(--light); }
.trow { display:grid; grid-template-columns:80px 1fr; position:relative; }
.trow+.trow { border-top:1px solid var(--light); }
.trow::before { content:''; position:absolute; left:72px; top:22px; width:16px; height:16px; border-radius:50%; background:white; border:2px solid var(--light); z-index:2; }
.ttime { padding:18px 24px 18px 0; text-align:right; font-size:10px; font-weight:600; color:var(--gray); letter-spacing:.05em; line-height:1.4; }
.tcontent { padding:16px 0 16px 28px; }
.tname { font-family:'DM Serif Display',serif; font-size:16px; font-weight:400; margin-bottom:4px; }
.taddr { font-size:11px; color:var(--gray); margin-bottom:6px; }
.tmap { font-size:9px; font-weight:500; letter-spacing:.1em; text-transform:uppercase; color:var(--dark); text-decoration:none; border-bottom:1px solid var(--light); padding-bottom:1px; }
.tmap:hover { border-color:var(--dark); }
.tnote { font-size:11px; color:var(--gray); font-style:italic; margin-top:4px; }
.pax { display:inline-flex; align-items:flex-end; gap:1px; margin-left:6px; vertical-align:middle; }
.tmeta { display:flex; align-items:center; gap:8px; flex-wrap:wrap; margin-top:4px; }

.topts { margin-top:8px; display:flex; flex-direction:column; gap:8px; }
.topt { background:var(--cream); border-radius:8px; padding:10px 14px; }
.topt-label { font-size:9px; font-weight:500; letter-spacing:.15em; text-transform:uppercase; margin-bottom:4px; }
.topt-name { font-family:'DM Serif Display',serif; font-size:14px; font-weight:400; margin-bottom:2px; }
.topt-det { font-size:11px; color:var(--gray); }
.topt-foot { display:flex; align-items:center; gap:10px; margin-top:6px; flex-wrap:wrap; }

.shops { display:flex; flex-direction:column; gap:5px; margin-top:6px; }
.shops a { font-size:11px; font-weight:600; color:var(--dark); text-decoration:none; }
.shops a:hover { text-decoration:underline; }
.shops a small { font-size:9px; color:var(--gray); }

.notes-section { padding:0 0 60px; border-bottom:none; }

footer.custom { background:var(--cream); border-top:2px solid var(--light); padding:48px; text-align:center; }
footer.custom .ft { font-family:'DM Serif Display',serif; font-size:clamp(22px,3.5vw,40px); font-weight:400; margin-bottom:6px; }
footer.custom .fs { font-size:11px; color:var(--gray); letter-spacing:.08em; }
footer.custom .sig { margin-top:20px; font-size:12px; color:var(--gray); letter-spacing:.06em; font-style:italic; }

@media(max-width:640px) {
  .hero, .day-header, .timeline, .legend { padding-left:20px; padding-right:20px; }
  .timeline::before { left:52px; }
  .trow { grid-template-columns:52px 1fr; }
  .trow::before { left:44px; }
  .ttime { font-size:9px; padding-right:14px; }
  .tcontent { padding-left:20px; }
}
</style>
""", unsafe_allow_html=True)

# ── PASSWORD ────────────────────────────────────────────────────
def check_password():
    if st.session_state.get("authenticated"):
        return True
    st.markdown("""
    <div style="max-width:380px;margin:15vh auto 0;text-align:center;">
      <h2 style="font-family:'DM Serif Display',serif;font-weight:400;margin-bottom:8px;">Welcome to Austin</h2>
      <p style="color:#7A7670;font-size:14px;margin-bottom:24px;">Enter the password to view the itinerary.</p>
    </div>
    """, unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
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

# ── HELPERS ─────────────────────────────────────────────────────
PIN = """<svg style="flex-shrink:0;margin-top:1px" width="10" height="13" viewBox="0 0 10 13" fill="none"><path d="M5 0C2.24 0 0 2.24 0 5c0 3.75 5 8 5 8s5-4.25 5-8C10 2.24 7.76 0 5 0zm0 6.5C4.17 6.5 3.5 5.83 3.5 5S4.17 3.5 5 3.5 6.5 4.17 6.5 5 5.83 6.5 5 6.5z" fill="#7A7670"/></svg>"""

def sf(n, c):
    fig = f'<svg width="11" height="20" viewBox="0 0 12 22"><circle cx="6" cy="3" r="2.5" fill="{c}"/><line x1="6" y1="6" x2="6" y2="14" stroke="{c}" stroke-width="1.8" stroke-linecap="round"/><line x1="6" y1="9" x2="1.5" y2="12.5" stroke="{c}" stroke-width="1.8" stroke-linecap="round"/><line x1="6" y1="9" x2="10.5" y2="12.5" stroke="{c}" stroke-width="1.8" stroke-linecap="round"/><line x1="6" y1="14" x2="2.5" y2="21" stroke="{c}" stroke-width="1.8" stroke-linecap="round"/><line x1="6" y1="14" x2="9.5" y2="21" stroke="{c}" stroke-width="1.8" stroke-linecap="round"/></svg>'
    return f'<span class="pax">{"".join([fig]*n)}</span>'

def tag(label, kind):
    return f'<span class="tag tag-{kind}" style="font-size:8px;vertical-align:middle;">{label}</span>'

def mlink(url, label="Maps →"):
    return f'<a href="{url}" target="_blank" class="tmap">{label}</a>'

def trow(time, name, addr=None, badge=None, note=None, pax=None, maps=None, opts=None, dot_color="var(--c1)"):
    dot_style = f"border-color:{dot_color};"
    nm = name
    if badge:
        nm += " " + badge
    html = f"""
    <div class="trow" style="--dot-color:{dot_color};">
      <style>.trow[style*="{dot_color}"]::before {{ border-color:{dot_color}; }}</style>
      <div class="ttime">{time}</div>
      <div class="tcontent">
        <p class="tname">{nm}</p>
    """
    if addr:
        html += f'<p class="taddr" style="display:flex;align-items:flex-start;gap:4px;">{PIN}{addr}</p>'
    if note:
        html += f'<p class="tnote">{note}</p>'
    if opts:
        html += '<div class="topts">'
        for o in opts:
            lbl, oname, odet, ourl, opax = o
            html += f"""
            <div class="topt">
              <p class="topt-label">{lbl}</p>
              <p class="topt-name">{oname}</p>
              <p class="topt-det">{odet}</p>
              <div class="topt-foot">{mlink(ourl)}{sf(*opax)}</div>
            </div>"""
        html += '</div>'
    if maps or pax:
        html += '<div class="tmeta">'
        if maps: html += mlink(maps)
        if pax:  html += sf(*pax)
        html += '</div>'
    html += '</div></div>'
    return html

def shops_list(items):
    html = '<div class="shops">'
    for name, url in items:
        html += f'<a href="{url}" target="_blank">{name} <small>→ Maps</small></a>'
    html += '</div>'
    return html

# ── RENDER ──────────────────────────────────────────────────────
M = "https://www.google.com/maps/search/"

# HERO
st.markdown("""
<section class="hero">
  <h1>Welcome to<br>Austin!</h1>
  <p class="sub">Keep Austin Weird.</p>
  <p class="dates">Thursday April 9th — Sunday April 12th</p>
</section>""", unsafe_allow_html=True)

# NAV — uses JS to scroll to anchor
st.markdown(f"""
<div class="sticky-nav">
  <a href="#thu" class="nav-thu"><span class="num">Day 01</span><span class="name">Thursday</span></a>
  <a href="#fri" class="nav-fri"><span class="num">Day 02</span><span class="name">Friday</span></a>
  <a href="#sat" class="nav-sat"><span class="num">Day 03</span><span class="name">Saturday</span></a>
  <a href="#sun" class="nav-sun"><span class="num">Day 04</span><span class="name">Sunday</span></a>
</div>
<div class="legend">
  <span class="tag tag-r">Reserved</span>
  <span class="tag tag-c">Purchased ✓</span>
  <span class="tag tag-t">Tentative</span>
</div>
""", unsafe_allow_html=True)

# ── THURSDAY ────────────────────────────────────────────────────
st.markdown("""
<div id="thu" class="day">
<div class="day-header">
  <p class="day-label" style="color:var(--c1)">Day 01 — Thursday</p>
  <h2>Arrival &amp; <em style="color:var(--c1)">First Bites</em></h2>
</div>
<div class="timeline">
""", unsafe_allow_html=True)

st.markdown(trow("12 pm", "Lunch — Pick one", opts=[
    ("Option A", "La Santa Barbacha", "1214 W 6th St, Ste 100 · Closes 3 pm · Michelin Bib Gourmand", M+"Desnudo+Coffee+1214+W+6th+St+Austin+TX", (2,"#E8602A")),
    ("Option B", "Mercado Sin Nombre", "408 N Pleasant Valley · Closes 2 pm · Cash only", M+"Mercado+Sin+Nombre+Austin+TX", (2,"#E8602A")),
    ("Option C", "Tacos D/10", "206 Trinity St · Opens 11:30 am · Taco speakeasy, enter through the alley", M+"Tacos+D10+206+Trinity+St+Austin+TX", (2,"#E8602A")),
], dot_color="var(--c1)"), unsafe_allow_html=True)

st.markdown(trow("Afternoon", "Desnudo Coffee", "1214 W 6th St #110 · Specialty coffee",
    maps=M+"Desnudo+Coffee+1214+W+6th+St+Austin+TX", pax=(2,"#E8602A"), dot_color="var(--c1)"), unsafe_allow_html=True)

st.markdown(trow("Afternoon", "Westside Market " + tag("Tentative","t"), "1214 W 6th St — same building as Desnudo",
    maps=M+"Westside+Market+1214+W+6th+St+Austin+TX", pax=(2,"#E8602A"), dot_color="var(--c1)"), unsafe_allow_html=True)

st.markdown(trow("Afternoon", "Target", maps=M+"Target+Austin+TX", pax=(2,"#E8602A"), dot_color="var(--c1)"), unsafe_allow_html=True)

st.markdown(trow("Night", "The Cavalier — Wings &amp; Drinks", "2400 Webberville Rd · East Austin · American Bar &amp; Grill · Closes 12 am",
    maps=M+"The+Cavalier+Austin+TX", pax=(3,"#E8602A"), dot_color="var(--c1)"), unsafe_allow_html=True)

st.markdown("</div></div>", unsafe_allow_html=True)

# ── FRIDAY ──────────────────────────────────────────────────────
st.markdown("""
<div id="fri" class="day">
<div class="day-header">
  <p class="day-label" style="color:var(--c2)">Day 02 — Friday</p>
  <h2><em style="color:var(--c2)">SoCo</em> Day</h2>
</div>
<div class="timeline">
""", unsafe_allow_html=True)

st.markdown(trow("7–9 am", "Lady Bird Lake Trail — Run", "S Lakeshore Blvd, Austin",
    maps=M+"Lady+Bird+Lake+Trail+Austin", pax=(2,"#0FA88F"), dot_color="var(--c2)"), unsafe_allow_html=True)

st.markdown(trow("9–10 am", "Café + Breakfast Taco — Pick one", opts=[
    ("Option A", "Noble Joe Co.", "Southshore · Near Lady Bird Lake · Coffee &amp; breakfast tacos", M+"Noble+Joe+Coffee+Austin+TX", (2,"#0FA88F")),
    ("Option B", "Mozart's Coffee Roasters", "3825 Lake Austin Blvd · Lakeside patio · Opens 7 am", M+"Mozarts+Coffee+Austin+TX", (2,"#0FA88F")),
], dot_color="var(--c2)"), unsafe_allow_html=True)

shops_html = trow("11 am+", "East 11th Street — Shopping", dot_color="var(--c2)")
shops_html = shops_html.replace("</div></div>", shops_list([
    ("Lovecraft", M+"Lovecraft+Bar+Austin+TX"),
    ("Kindred Spirits", M+"Kindred+Spirits+Austin+TX"),
    ("Apartment F", M+"Apartment+F+Austin+TX"),
    ("Take Heart", M+"Take+Heart+Austin+TX"),
    ("Pecos &amp; Jane", M+"Pecos+Jane+Austin+TX"),
]) + '<div class="tmeta">' + sf(2,"#0FA88F") + '</div></div></div>')
st.markdown(shops_html, unsafe_allow_html=True)

st.markdown(trow("1:15 pm", "Paperboy East " + tag("Reserved","r"),
    "1203 E 11th St · American Brunch · Closes 3 pm",
    maps=M+"Paperboy+East+Austin+TX", pax=(2,"#0FA88F"), dot_color="var(--c2)"), unsafe_allow_html=True)

st.markdown(trow("Afternoon", "South Congress Ave — Shopping &amp; Walk",
    "S Congress Ave, Austin TX",
    note="Allen's Boots · \"I love you so much\" mural · boutiques",
    maps=M+"South+Congress+Avenue+Austin+TX", pax=(2,"#0FA88F"), dot_color="var(--c2)"), unsafe_allow_html=True)

st.markdown(trow("9 pm", "Odd Duck " + tag("Reserved","r"),
    "1201 S Lamar Blvd · American Farm-to-Table · Closes 9 pm · Michelin Guide ⭐",
    maps=M+"Odd+Duck+Austin+TX", pax=(3,"#0FA88F"), dot_color="var(--c2)"), unsafe_allow_html=True)

st.markdown("</div></div>", unsafe_allow_html=True)

# ── SATURDAY ────────────────────────────────────────────────────
st.markdown("""
<div id="sat" class="day">
<div class="day-header">
  <p class="day-label" style="color:var(--c3)">Day 03 — Saturday</p>
  <h2>BBQ, <em style="color:var(--c3)">Barre</em> &amp; Dancing</h2>
</div>
<div class="timeline">
""", unsafe_allow_html=True)

st.markdown(trow("Morning", "Barre Class", pax=(2,"#E84470"), dot_color="var(--c3)"), unsafe_allow_html=True)
st.markdown(trow("Post-class", "Veracruz All Natural",
    "Mueller neighborhood · Mexican · Michelin Bib Gourmand",
    maps=M+"1905+Aldrich+St+125+Austin+TX+78723", pax=(2,"#E84470"), dot_color="var(--c3)"), unsafe_allow_html=True)
st.markdown(trow("Afternoon", "South Lamar / East Side " + tag("Tentative","t"),
    maps=M+"South+Lamar+Blvd+Austin+TX", pax=(2,"#E84470"), dot_color="var(--c3)"), unsafe_allow_html=True)

st.markdown(trow("5 pm", "BBQ — Pick one", opts=[
    ("Option A", "La Barbecue", "2027 E Cesar Chavez St · Texas BBQ · Closes 9 pm · Michelin Guide ⭐", M+"La+Barbecue+Austin+TX", (4,"#E84470")),
    ("Option B", "Terry Black's BBQ", "1003 Barton Springs Rd · Texas BBQ · Closes 10 pm · Walk-in friendly", M+"Terry+Blacks+BBQ+Austin+TX", (4,"#E84470")),
    ("Option C", "LeRoy &amp; Lewis", "5621 Emerald Forest Dr · New School BBQ · Closes 9 pm · Michelin Guide ⭐", M+"LeRoy+Lewis+BBQ+Austin+TX", (4,"#E84470")),
], dot_color="var(--c3)"), unsafe_allow_html=True)

st.markdown(trow("Night", "Dance Hall — Pick one", opts=[
    ("Option A · Legendary", "Broken Spoke", "3201 S Lamar Blvd · $20 cash · Two-step lessons Sat 8 pm", M+"Broken+Spoke+Austin+TX", (5,"#E84470")),
    ("Option B · Livelier", "White Horse", "500 Comal St · East Austin · Live music every night", M+"White+Horse+Austin+TX", (5,"#E84470")),
], dot_color="var(--c3)"), unsafe_allow_html=True)

st.markdown(trow("Late Night", "Bar Hopping — East 6th",
    note="Whisler's · Nickel City · Ah Sing Den",
    maps=M+"Whislers+Austin+TX", pax=(5,"#E84470"), dot_color="var(--c3)"), unsafe_allow_html=True)

st.markdown("</div></div>", unsafe_allow_html=True)

# ── SUNDAY ──────────────────────────────────────────────────────
st.markdown("""
<div id="sun" class="day">
<div class="day-header">
  <p class="day-label" style="color:var(--c4)">Day 04 — Sunday</p>
  <h2>Market, <em style="color:var(--c4)">Oysters</em> &amp; Goodbye</h2>
</div>
<div class="timeline">
""", unsafe_allow_html=True)

st.markdown(trow("9–11 am", "Mueller Farmers' Market", "2006 Philomena St · Sundays only",
    maps=M+"Mueller+Farmers+Market+Austin", pax=(3,"#3D2FA0"), dot_color="var(--c4)"), unsafe_allow_html=True)
st.markdown(trow("12–1 pm", "The Range Austin " + tag("Purchased ✓","c"), "8301 S I-35 Frontage Rd",
    maps=M+"The+Range+Austin+TX", pax=(5,"#3D2FA0"), dot_color="var(--c4)"), unsafe_allow_html=True)
st.markdown(trow("1:30 pm", "Skipjack Oyster Bar " + tag("Reserved","r"), "East 5th St · Seafood · Closes 3 pm",
    maps=M+"Skipjack+Oyster+Bar+Austin+TX", pax=(5,"#3D2FA0"), dot_color="var(--c4)"), unsafe_allow_html=True)
st.markdown(trow("After 3 pm", "Capitol &amp; Downtown " + tag("Tentative","t"), "1100 Congress Ave · Free entry",
    maps=M+"Texas+State+Capitol+Austin", pax=(5,"#3D2FA0"), dot_color="var(--c4)"), unsafe_allow_html=True)
st.markdown(trow("After 3 pm", "Rainy Street " + tag("Tentative","t"), "Rainey St, Austin TX",
    maps=M+"Rainey+Street+Austin+TX", pax=(5,"#3D2FA0"), dot_color="var(--c4)"), unsafe_allow_html=True)
st.markdown(trow("7 pm", "Nido " + tag("Reserved","r"),
    "1211 W Riverside Dr · Loren Hotel Rooftop · American / Italian · Closes 10 pm",
    maps=M+"Nido+Loren+Hotel+Austin+TX", pax=(3,"#3D2FA0"), dot_color="var(--c4)"), unsafe_allow_html=True)

st.markdown("</div></div>", unsafe_allow_html=True)

# ── IF IT RAINS ─────────────────────────────────────────────────
st.markdown("""
<div class="notes-section">
<div class="day-header">
  <p class="day-label" style="color:var(--gray)">Notes</p>
  <h2 style="font-size:clamp(22px,3vw,36px);">If it rains</h2>
</div>
<div class="timeline">
""", unsafe_allow_html=True)

st.markdown(trow("Option A", "Blanton Museum of Art", "200 E MLK Jr Blvd · UT Campus · Latin American art collection",
    maps=M+"Blanton+Museum+of+Art+Austin+TX", dot_color="var(--gray)"), unsafe_allow_html=True)
st.markdown(trow("Option B", "Pinballz Arcade", "Austin TX · Huge arcade bar · Perfect for groups",
    maps=M+"Pinballz+Arcade+Austin+TX", dot_color="var(--gray)"), unsafe_allow_html=True)
st.markdown(trow("Option C", "Topgolf", "Austin TX · Covered bays · Food, drinks &amp; golf",
    maps=M+"Topgolf+Austin+TX", dot_color="var(--gray)"), unsafe_allow_html=True)

st.markdown("</div></div>", unsafe_allow_html=True)

# ── FOOTER ──────────────────────────────────────────────────────
st.markdown("""
<footer class="custom">
  <p class="ft">Happy to see you!</p>
  <p class="fs">Austin, TX · April 9–12</p>
  <p class="sig">with love,<br>Nicol Sau</p>
</footer>
""", unsafe_allow_html=True)
