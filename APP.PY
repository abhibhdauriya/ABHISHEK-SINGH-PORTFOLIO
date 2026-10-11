import html as _html
import json
from datetime import datetime

import pandas as pd
import streamlit as st
import streamlit.components.v1 as components

# ───────────────────────── CONFIG ─────────────────────────
ADMIN_PASSCODE = "admin123"
GITHUB = "https://github.com/abhibhdauriya"
VIEW_USER = "User View (3D Portfolio)"
VIEW_ADMIN = "Admin Command Portal"
CATEGORIES = ["Industrial Automation", "Data & Analytics", "Business Platform", "Web App", "Other"]

st.set_page_config(page_title="Abhishek Singh | Portfolio", page_icon="⚡", layout="wide")

# ───────────────────────── STYLES ─────────────────────────
CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&family=JetBrains+Mono:wght@400;600&display=swap');
:root{--bg:#08090d;--cy:#00f0ff;--vi:#7000ff;--glass:rgba(255,255,255,.04);--bd:rgba(255,255,255,.10);--tx:#e8ecf4;--mut:#8b93a7}
html,body,[class*="css"],.stApp{font-family:'Space Grotesk',system-ui,sans-serif;color:var(--tx)}
.stApp{background:radial-gradient(900px 500px at 12% -5%,rgba(112,0,255,.22),transparent 60%),radial-gradient(800px 500px at 100% 10%,rgba(0,240,255,.14),transparent 60%),var(--bg)}
header[data-testid="stHeader"]{background:transparent}
.block-container{padding-top:1.5rem;max-width:1200px}
section[data-testid="stSidebar"]{background:rgba(10,12,18,.75);backdrop-filter:blur(18px);border-right:1px solid var(--bd)}
h1,h2,h3{letter-spacing:-.02em}
.glass{background:var(--glass);border:1px solid var(--bd);border-radius:18px;backdrop-filter:blur(16px);-webkit-backdrop-filter:blur(16px);box-shadow:0 8px 32px rgba(0,0,0,.45)}
.hero-wrap{border:1px solid var(--bd);border-radius:22px;overflow:hidden;box-shadow:0 0 40px rgba(112,0,255,.25),inset 0 0 40px rgba(0,240,255,.05);margin-bottom:1.2rem}
.profile{padding:1.8rem 2rem;margin-bottom:1.4rem}
.kicker{font-family:'JetBrains Mono',monospace;font-size:.78rem;color:var(--cy);letter-spacing:.18em;text-transform:uppercase}
.name{font-size:3rem;font-weight:700;line-height:1.05;margin:.3rem 0;background:linear-gradient(90deg,var(--cy),var(--vi));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.title{font-size:1.25rem;font-weight:500;color:var(--tx)}
.headline{color:var(--mut);margin-top:.5rem;font-size:1.02rem;max-width:760px}
.sec{font-family:'JetBrains Mono',monospace;font-size:.85rem;color:var(--cy);letter-spacing:.2em;text-transform:uppercase;margin:2rem 0 .8rem}
.skill{padding:.9rem 1rem;text-align:left;transition:all .25s ease;cursor:default;margin-bottom:.8rem}
.skill:hover{transform:translateY(-4px);border-color:var(--cy);box-shadow:0 0 22px rgba(0,240,255,.35)}
.skill .n{font-weight:700;font-size:1rem}.skill .d{color:var(--mut);font-size:.8rem;margin-top:.15rem}
.pcard{padding:1.3rem;height:100%;min-height:330px;display:flex;flex-direction:column;transition:all .25s ease;margin-bottom:1rem}
.pcard:hover{transform:translateY(-5px);border-color:var(--vi);box-shadow:0 0 28px rgba(112,0,255,.45)}
.cat{font-family:'JetBrains Mono',monospace;font-size:.7rem;color:var(--cy);letter-spacing:.14em;text-transform:uppercase}
.ptitle{font-size:1.15rem;font-weight:700;margin:.4rem 0 .5rem}
.pdesc{color:var(--mut);font-size:.9rem;flex:1;line-height:1.5}
.tag{display:inline-block;font-family:'JetBrains Mono',monospace;font-size:.7rem;padding:.2rem .55rem;margin:.15rem .25rem .15rem 0;border-radius:999px;border:1px solid rgba(0,240,255,.4);color:var(--cy);background:rgba(0,240,255,.07)}
.btns{margin-top:.9rem;display:flex;gap:.5rem;flex-wrap:wrap}
a.btn{text-decoration:none!important;font-size:.82rem;font-weight:600;padding:.5rem .9rem;border-radius:10px;transition:all .2s ease}
a.btn.p{color:#08090d!important;background:linear-gradient(90deg,var(--cy),#6ab7ff)}
a.btn.p:hover{box-shadow:0 0 18px rgba(0,240,255,.7);transform:translateY(-1px)}
a.btn.s{color:var(--tx)!important;border:1px solid var(--bd);background:var(--glass)}
a.btn.s:hover{border-color:var(--vi);box-shadow:0 0 14px rgba(112,0,255,.6)}
.stTextInput input,.stTextArea textarea,.stSelectbox div[data-baseweb="select"]>div{background:rgba(255,255,255,.05)!important;border:1px solid var(--bd)!important;color:var(--tx)!important;border-radius:12px!important}
.stTextInput input:focus,.stTextArea textarea:focus{border-color:var(--cy)!important;box-shadow:0 0 0 1px var(--cy)!important}
.stButton>button,.stFormSubmitButton>button,.stDownloadButton>button{background:linear-gradient(90deg,var(--vi),#3d5afe);color:#fff;border:0;border-radius:12px;font-weight:600;transition:all .2s ease}
.stButton>button:hover,.stFormSubmitButton>button:hover,.stDownloadButton>button:hover{box-shadow:0 0 20px rgba(112,0,255,.8);transform:translateY(-1px);color:#fff;border:0}
[data-testid="stForm"]{background:var(--glass);border:1px solid var(--bd);border-radius:18px;backdrop-filter:blur(16px);padding:1.4rem}
[data-testid="stMetric"]{background:var(--glass);border:1px solid var(--bd);border-radius:16px;padding:1rem 1.2rem;backdrop-filter:blur(14px)}
[data-testid="stMetricValue"]{color:var(--cy)}
.stTabs [data-baseweb="tab-list"]{gap:.4rem}
.stTabs [data-baseweb="tab"]{background:var(--glass);border:1px solid var(--bd);border-radius:12px;padding:.5rem 1rem}
.stTabs [aria-selected="true"]{border-color:var(--cy);color:var(--cy)}
.brand{font-weight:700;font-size:1.2rem;background:linear-gradient(90deg,var(--cy),var(--vi));-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}
.status{font-family:'JetBrains Mono',monospace;font-size:.75rem;color:#39ff88}
.footer{text-align:center;color:var(--mut);font-size:.8rem;margin:3rem 0 1rem;font-family:'JetBrains Mono',monospace}
@media(max-width:640px){.name{font-size:2.1rem}}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

# ───────────────────────── THREE.JS HERO ─────────────────────────
THREE_HTML = """<!DOCTYPE html><html><head><meta charset="utf-8"><style>
html,body{margin:0;height:100%;background:transparent;overflow:hidden;font-family:monospace}
canvas{display:block;width:100%;height:100%;touch-action:none;cursor:grab}canvas:active{cursor:grabbing}
#h{position:absolute;left:0;right:0;bottom:12px;text-align:center;color:#00f0ff;font-size:11px;letter-spacing:.25em;opacity:.7;pointer-events:none;text-transform:uppercase}
</style></head><body><canvas id="c"></canvas><div id="h">drag &middot; move cursor &middot; interact</div>
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<script>
(function(){var cv=document.getElementById('c'),hint=document.getElementById('h');
if(!window.THREE){hint.textContent='3D library failed to load';return}
var W=function(){return window.innerWidth},H=function(){return window.innerHeight};
var scene=new THREE.Scene(),cam=new THREE.PerspectiveCamera(55,W()/H(),.1,100);cam.position.z=3.8;
var ren;try{ren=new THREE.WebGLRenderer({canvas:cv,alpha:true,antialias:true})}catch(e){hint.textContent='WebGL not supported';return}
ren.setPixelRatio(Math.min(window.devicePixelRatio||1,2));ren.setSize(W(),H());
var g=new THREE.Group();scene.add(g);
var N=4200,p=new Float32Array(N*3),c=new Float32Array(N*3),c1=new THREE.Color(0x00f0ff),c2=new THREE.Color(0x7000ff),t=new THREE.Color();
for(var i=0;i<N;i++){var k=(i+.5)/N,ph=Math.acos(1-2*k),th=Math.PI*(1+Math.sqrt(5))*(i+.5),r=1.45+(Math.random()-.5)*.07;
p[3*i]=r*Math.cos(th)*Math.sin(ph);p[3*i+1]=r*Math.sin(th)*Math.sin(ph);p[3*i+2]=r*Math.cos(ph);
t.copy(c1).lerp(c2,k);c[3*i]=t.r;c[3*i+1]=t.g;c[3*i+2]=t.b}
var geo=new THREE.BufferGeometry();geo.setAttribute('position',new THREE.BufferAttribute(p,3));geo.setAttribute('color',new THREE.BufferAttribute(c,3));
g.add(new THREE.Points(geo,new THREE.PointsMaterial({size:.026,vertexColors:true,transparent:true,opacity:.92,blending:THREE.AdditiveBlending,depthWrite:false})));
var wire=new THREE.Mesh(new THREE.IcosahedronGeometry(1,2),new THREE.MeshBasicMaterial({color:0x7000ff,wireframe:true,transparent:true,opacity:.38}));g.add(wire);
var ring=new THREE.Mesh(new THREE.TorusGeometry(2,.006,8,180),new THREE.MeshBasicMaterial({color:0x00f0ff,transparent:true,opacity:.7}));ring.rotation.x=1.2;g.add(ring);
var ring2=new THREE.Mesh(new THREE.TorusGeometry(2.3,.004,8,180),new THREE.MeshBasicMaterial({color:0x7000ff,transparent:true,opacity:.6}));ring2.rotation.y=1.2;g.add(ring2);
var tx=0,ty=0,rx=0,ry=0,mx=0,my=0,drag=false,lx=0,ly=0;
cv.addEventListener('pointerdown',function(e){drag=true;lx=e.clientX;ly=e.clientY;try{cv.setPointerCapture(e.pointerId)}catch(_){}});
window.addEventListener('pointerup',function(){drag=false});
cv.addEventListener('pointermove',function(e){if(drag){ty+=(e.clientX-lx)*.01;tx+=(e.clientY-ly)*.01;lx=e.clientX;ly=e.clientY}
var b=cv.getBoundingClientRect();mx=(e.clientX-b.left)/b.width-.5;my=(e.clientY-b.top)/b.height-.5});
cv.addEventListener('pointerleave',function(){mx=0;my=0});
window.addEventListener('resize',function(){cam.aspect=W()/H();cam.updateProjectionMatrix();ren.setSize(W(),H())});
var clock=new THREE.Clock();
(function loop(){requestAnimationFrame(loop);var T=clock.getElapsedTime();if(!drag)ty+=.0026;
ry+=(ty+mx*.9-ry)*.06;rx+=(tx+my*.9-rx)*.06;g.rotation.y=ry;g.rotation.x=rx;
wire.rotation.y-=.004;ring.rotation.z+=.004;ring2.rotation.x-=.003;
var s=1+Math.sin(T*1.4)*.025;g.scale.set(s,s,s);ren.render(scene,cam)})()})();
</script></body></html>"""

# ───────────────────────── STATE ─────────────────────────
def init_state():
    ss = st.session_state
    if "projects" not in ss:
        ss.projects = [
            {"id": 1, "title": "Industrial CNC Shop-Floor Production Tracker",
             "tech": ["Excel VBA", "OpenPyXL", "KPI Dashboards", "28+ CNC Lines"],
             "desc": "Real-time production tracking system monitoring 28+ CNC lines with automated KPI dashboards, shift-wise output, downtime analysis and one-click reporting.",
             "link": GITHUB, "category": "Industrial Automation"},
            {"id": 2, "title": "Interactive Financial & Statement Analytics Engine",
             "tech": ["Streamlit", "Pandas", "UPI Parsing", "Bank Statements"],
             "desc": "Upload UPI and bank statements to auto-parse, categorize and visualize income, expenses and spending trends through an interactive Streamlit dashboard.",
             "link": GITHUB, "category": "Data & Analytics"},
            {"id": 3, "title": "Local B2B Business Automation Platform",
             "tech": ["Node.js", "REST APIs", "Custom Workflows"],
             "desc": "Lightweight B2B platform automating orders, invoicing and follow-ups for local businesses via REST APIs and configurable workflow engines.",
             "link": GITHUB, "category": "Business Platform"},
        ]
    ss.setdefault("next_id", 4)
    ss.setdefault("messages", [])
    ss.setdefault("flash", None)
    ss.setdefault("boot", datetime.now())


init_state()


def esc(x):
    return _html.escape(str(x), quote=True)


def safe_url(u):
    u = (u or "").strip()
    return u if u.lower().startswith(("http://", "https://")) else GITHUB


# ───────────────────────── SIDEBAR ─────────────────────────
with st.sidebar:
    st.markdown('<div class="brand">⚡ ABHI.DEV</div><div class="status">● SYSTEM ONLINE</div>', unsafe_allow_html=True)
    st.write("")
    view = st.radio("Navigation", [VIEW_USER, VIEW_ADMIN], label_visibility="collapsed")
    passcode = ""
    if view == VIEW_ADMIN:
        st.divider()
        passcode = st.text_input("Admin Passcode", type="password", placeholder="Enter passcode")
    st.divider()
    st.caption(f"Projects: {len(st.session_state.projects)} · Inquiries: {len(st.session_state.messages)}")


# ───────────────────────── PAGE 1: USER VIEW ─────────────────────────
def render_user_view():
    st.markdown('<div class="hero-wrap">', unsafe_allow_html=True)
    components.html(THREE_HTML, height=460)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="glass profile"><div class="kicker">// Hello World, I am</div>'
        '<div class="name">Abhishek Singh</div>'
        '<div class="title">Full-Stack Developer &amp; Data Automation Engineer</div>'
        '<div class="headline">Specializing in Python automation, high-performance Streamlit tools, and industrial Excel VBA systems.</div></div>',
        unsafe_allow_html=True,
    )

    st.markdown('<div class="sec">// Skill Matrix</div>', unsafe_allow_html=True)
    skills = [
        ("🐍", "Python", "Automation, scripting, Pandas"),
        ("🚀", "Streamlit", "Fast data apps & dashboards"),
        ("📊", "Excel VBA / Macros", "Industrial reporting systems"),
        ("📑", "OpenPyXL", "Programmatic Excel pipelines"),
        ("🟢", "Node.js", "REST APIs & backends"),
        ("🗄️", "SQL", "Queries, joins, analytics"),
    ]
    cols = st.columns(3)
    for i, (ic, n, d) in enumerate(skills):
        with cols[i % 3]:
            st.markdown(f'<div class="glass skill"><div class="n">{ic} {esc(n)}</div><div class="d">{esc(d)}</div></div>', unsafe_allow_html=True)

    st.markdown('<div class="sec">// Featured Projects</div>', unsafe_allow_html=True)
    projects = st.session_state.projects
    if not projects:
        st.info("No projects yet. Add some from the Admin Command Portal.")
    for start in range(0, len(projects), 3):
        row = projects[start:start + 3]
        cols = st.columns(3)
        for col, p in zip(cols, row):
            tags = "".join(f'<span class="tag">{esc(t)}</span>' for t in p["tech"])
            card = (
                '<div class="glass pcard">'
                f'<div class="cat">{esc(p["category"])}</div>'
                f'<div class="ptitle">{esc(p["title"])}</div>'
                f'<div class="pdesc">{esc(p["desc"])}</div>'
                f'<div style="margin-top:.8rem">{tags}</div>'
                '<div class="btns">'
                f'<a class="btn p" href="{esc(safe_url(p["link"]))}" target="_blank" rel="noopener noreferrer">View Project ↗</a>'
                f'<a class="btn s" href="{esc(GITHUB)}" target="_blank" rel="noopener noreferrer">Source Code</a>'
                '</div></div>'
            )
            with col:
                st.markdown(card, unsafe_allow_html=True)

    st.markdown('<div class="sec">// Initiate Contact</div>', unsafe_allow_html=True)
    with st.form("contact_form", clear_on_submit=True):
        c1, c2 = st.columns(2)
        name = c1.text_input("Your Name")
        email = c2.text_input("Your Email")
        msg = st.text_area("Message", height=140)
        sent = st.form_submit_button("Send Message ⚡")
    if sent:
        if not name.strip() or not msg.strip() or "@" not in email or "." not in email:
            st.error("Please provide a name, a valid email and a message.")
        else:
            st.session_state.messages.append({
                "id": len(st.session_state.messages) + 1,
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "name": name.strip(), "email": email.strip(), "message": msg.strip(),
            })
            st.success("Message transmitted. I will get back to you soon!")

    st.markdown('<div class="footer">© 2026 Abhishek Singh · Built with Python, Streamlit &amp; Three.js</div>', unsafe_allow_html=True)


# ───────────────────────── PAGE 2: ADMIN ─────────────────────────
def render_admin_view():
    st.markdown('<div class="kicker">// restricted area</div><h2 style="margin-top:.2rem">Admin Command Portal</h2>', unsafe_allow_html=True)
    if passcode != ADMIN_PASSCODE:
        st.markdown('<div class="glass" style="padding:1.5rem">🔒 <b>Access locked.</b> Enter the admin passcode in the sidebar to continue.</div>', unsafe_allow_html=True)
        if passcode:
            st.error("Invalid passcode.")
        return

    if st.session_state.flash:
        st.success(st.session_state.flash)
        st.session_state.flash = None

    t1, t2, t3 = st.tabs(["📈 Metrics", "🛠️ Project Manager", "📬 Inbound Messages"])

    with t1:
        m1, m2, m3, m4 = st.columns(4)
        m1.metric("Total Projects", len(st.session_state.projects))
        m2.metric("Inquiries", len(st.session_state.messages))
        m3.metric("Server Status", "ONLINE")
        up = datetime.now() - st.session_state.boot
        m4.metric("Session Uptime", f"{int(up.total_seconds() // 60)} min")
        st.markdown('<div class="sec">// Projects by category</div>', unsafe_allow_html=True)
        if st.session_state.projects:
            df = pd.DataFrame(st.session_state.projects)
            st.bar_chart(df["category"].value_counts())
        else:
            st.info("No project data to chart.")

    with t2:
        st.markdown('<div class="sec">// Add new project</div>', unsafe_allow_html=True)
        with st.form("add_project", clear_on_submit=True):
            a, b = st.columns(2)
            title = a.text_input("Title")
            category = b.selectbox("Category", CATEGORIES)
            tech = st.text_input("Tech Stack (comma separated)", placeholder="Python, Pandas, Streamlit")
            link = st.text_input("Link", placeholder="https://github.com/...")
            desc = st.text_area("Description", height=110)
            add = st.form_submit_button("Deploy Project 🚀")
        if add:
            techs = [t.strip() for t in tech.split(",") if t.strip()]
            if not title.strip() or not desc.strip() or not techs:
                st.error("Title, tech stack and description are required.")
            else:
                st.session_state.projects.append({
                    "id": st.session_state.next_id, "title": title.strip(), "tech": techs,
                    "desc": desc.strip(), "link": safe_url(link), "category": category,
                })
                st.session_state.next_id += 1
                st.session_state.flash = f"Project '{title.strip()}' added to the portfolio."
                st.rerun()

        st.markdown('<div class="sec">// Existing projects</div>', unsafe_allow_html=True)
        if not st.session_state.projects:
            st.info("No projects to manage.")
        for p in list(st.session_state.projects):
            c1, c2 = st.columns([5, 1])
            c1.markdown(
                f'<div class="glass" style="padding:.8rem 1rem;margin-bottom:.5rem"><b>{esc(p["title"])}</b>'
                f'<div class="cat" style="margin-top:.2rem">{esc(p["category"])} · {esc(", ".join(p["tech"]))}</div></div>',
                unsafe_allow_html=True,
            )
            if c2.button("🗑️ Delete", key=f"del_{p['id']}"):
                st.session_state.projects = [x for x in st.session_state.projects if x["id"] != p["id"]]
                st.session_state.flash = f"Project '{p['title']}' deleted."
                st.rerun()

    with t3:
        msgs = st.session_state.messages
        if not msgs:
            st.info("No inbound messages yet. Submissions from the User View contact form appear here.")
        else:
            df = pd.DataFrame(msgs)[["id", "time", "name", "email", "message"]]
            st.dataframe(df, hide_index=True)
            for m in reversed(msgs):
                with st.expander(f"#{m['id']} · {m['name']} · {m['time']}"):
                    st.markdown(f"**Email:** {m['email']}")
                    st.write(m["message"])
            d1, d2 = st.columns(2)
            d1.download_button("⬇️ Export JSON", json.dumps(msgs, indent=2), "messages.json", "application/json")
            if d2.button("Clear all messages"):
                st.session_state.messages = []
                st.session_state.flash = "All messages cleared."
                st.rerun()


# ───────────────────────── ROUTER ─────────────────────────
if view == VIEW_USER:
    render_user_view()
else:
    render_admin_view()
