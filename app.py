import random
import streamlit as st
import time
import streamlit.components.v1 as components

ss = st.session_state

st.set_page_config(page_title="Tafels oefenen 2", page_icon="🧮", layout="centered")

STICKERS = [
    "🐶", "🐱", "🐭", "🐹", "🐰",
    "🦊", "🐻", "🐼", "🐸", "🦄",
    "🐯", "🦁", "🐨", "🐷", "🐵",
    "🐔", "🐧", "🐙", "🦋", "🐢" 
    "💩","🦔","🌈","🍭","⭐","🍩","🧁"
    ]

GIFS = [ 
    "https://cataas.com/cat/gif",
    "https://raw.githubusercontent.com/PCBons/tafels/refs/heads/main/gifs/ezgif-3fa7f2a99bc4d8aa.gif",
    "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExemwwZXVlOXprZHpoenl6dDU4c2FnZXZ3dmQ3MmduY2sydmZwcGN5dCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3UkqVq3F50bVCi9URl/giphy.gif",
    "http://raw.githubusercontent.com/PCBons/tafels/refs/heads/main/gifs/ezgif-668e3c8cd96be53a.gif",
    "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExZTY4NHNxbHlucTc1aG5zdDM0eDN2N3FibGpmNHQwZmR6amV3bGJmYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/pAHAgWYYjWIE9DNLcC/giphy.gif",
    "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExaXNnZXFuenYzcWo5Yzc4dmliYjU0NDliY2Rnc3FmMHZsb252MjI3byZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/tv4wFKOCoF11QNrn39/giphy.gif",
    "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExZWJkcXQzMDVmMjNpN3BmaWpzN3NyYm5oNWZiejhkbDVwNWlhbnU0dSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/auGFCmg6rM0eI/giphy.gif",
    "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExaW44M29vdzhxMGhzNWxqdGQwdTJlNTdjbzB3dDJmajd0eXluZ2pmYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/knLRouBQlkniWmx0hp/giphy.gif",
    "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExcnc0Z3dlczA0cjVkZ29tdGQzNzR1OWNidmRlNDE3YmY5aGZ0ZWUwdCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ewzF6uunnPn6L5amuW/giphy.gif",
    "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ2M4ZzA3emR3a2Vzano3MW95MWx2MDZtbzdtbTNzMGV3ZnY3enowbCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hwaFAsPi7wU6LHwn84/giphy.gif",
    "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExNXJweWEyOGZyb3Z3NTFtbXFscm9weHh6ZHZsb2dmZThoejAxdzllYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/jp2KXzsPtoKFG/giphy.gif",
    "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExemhuNWtwdHIyeWpzNzFrenc5Z3NrNm00Mm90djNpb2YzcHlwOW5tdiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/ZrkDWOSI2WHndH4bDk/giphy.gif",
    "https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExOXpxMjFxYWtleWVwbjh5OXJ1dWtnamR0bncxYmRkOHIzcTc4NHRoeiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/j6N49PBSQ5jYk/giphy.gif",
    "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExczM4Zm0zanZsYTBicG14azZ6M2E1bGF6a2w5dWFoMmVibTM0OWR0ZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/exUgjvyJF451IGaRpH/giphy.gif",
    "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDByaWZsazNtMm11NzNmMmlhd28wMnR4eHFuMTJvbzZka3oyZ200NSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/K64TYvCquNClUtF0dK/giphy.gif",
    "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExcW92YTAyenplNWZ0bHEzcG5uMDd6b3d2dzYyejY0ZzM4ZTVsMzA4MCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/13Fpy0743BgDuM/giphy.gif",
    "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ283cnhpdTRyZHRqdTM4cDQyZzFjYXhoMDFta2YwMzY0cDR1NGRuaSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/k6SImaefvartv71xUc/giphy.gif",
    "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExODh2aWZzcWR3NHd2Yno5YXAzOW1hejdpMzJyYTV0dTB0cHY5YnptYSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Y0G6gc8CJu1ynAZ1nr/giphy.gif",
    "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGduOGs0NjFvMWM0bzcydzJrejBnaWVpMzRlbTNvbGJ0YzZlbmI3MiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/10YpWPBU7GAYwM/giphy.gif",
    "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExdjQ5eGE0eGZnbmRlZXVnYnV2M2I1enk2b2FqbHh4dWJjemM5azFqNSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/OOKh3MLvb21vrHh1mw/giphy.gif",
    "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExY2NzZmN5cW01Mmpxc2dudm9jN2NxbXFmMmhtZGE1M3hhYXUyd21tMyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/YaP3iYxN3T8nIEN5rD/giphy.gif",
    "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGo1bGNuc3lkN3ViY3p2MmxhdHlzb2E5dTNkajBuM2w2NTU5Y3A4ayZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/VFif0wu8xhKC6Kyj4m/giphy.gif",
    "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExOXN4ZjI3MmdoaXQ0dXBjM2luaWJ3a2c5Y2N4c2tkNGlmb201dW53dSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/kMdlyJ74u9khW/giphy.gif",
    "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExNm9maGxycW9tOHptYnA3eHMxNjk5eTk5MW5jc3kwNHVha3c1NXJqbiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/hQnhJO7sTUtufxxY0L/giphy.gif",
    "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExdzN0bjNkemlqaGlmbWx4ejYyOHBwa284eGh6czk5ZHduMmZjanpidSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/bnOIY81AEMa4llyfFI/giphy.gif",
    "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExMW5kNnZpOG00aWNmNGJwdW5hdWx1ZjFuNmhzbmhra2VrdW1xZzQ1ciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/KyYIA8dlA6x6hLGrbn/giphy.gif",
    "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExZzM0anE1aWNoanlvNGl4cmptdHYyMXFndjJ3aDM2cGU1YjRodnpxcCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/rZ7A5ayCa2zVcMgsvl/giphy.gif",
    "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExY3lhY3p6ZXFyZnRrdmV3aXZvbHhlbTlnZ3FzcmNndjlocDBiaTBpdSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/7NNqJw0T3cb62PMzXR/giphy.gif",
    "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExajh4Y2R2eTJmZWFrZDdtZHgza2xlNXJtNGduNjJpdjh2bXNzaWl1eSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/u7bymITK1tbP3tSAEg/giphy.gif",
    "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExaDQxcjI4YjN3bHQ2ZXNndHR5eGFhaGc3Zzc3YmdibnZycDMwemlzeCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/LRgJfEddZxbYeOIeru/giphy.gif",
    "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExaDE4cWtyNDVtb3dhYXF1aGY5MDdzMDU5aGY3MG82eDk3bDN2a2hrZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/YOMXLnRL5MJidjrvYH/giphy.gif",
    "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExMXM5ZmZpYWt2czd5c255aWoxZzc4c3p6Z2tocnJ6ZmpkMTh5OXd2MyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Ybv6IEqXHeRdXd84eH/giphy.gif",
    "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExY3U1dWs4ZWoyNnVvNmdlZmhucXh1M3VxbGhpdndtajE3eTY4ZXg2dSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/aWpSIlUoSvcNa/giphy.gif",
    "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExcWZoM29yNzh6bWp1NDFzNTdmMmFtN2cwMHIxMjRremx1cHRyeHh1ZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/iAn1Wh7Fdnh6rKg4Tq/giphy.gif",
    "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExd3Q5NXBhYnQzMG4xYmJrZDI2aTE4ejd6cGR6bnEweno0aHB3cWNtZyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/jW6hk4hdly154d0NyM/giphy.gif",
    "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExYWg3eWFtaWtmcmg3MGp2ZWk0dTZ1Ynh1OTJvcnpoYXhlMWEwb2h0dSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/4asRlBKdJaPeBahjcL/giphy.gif",
    "https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExMzlneHZ6YzF6bThqZXQzY2Q1eDNwcDhmb29vb281MTFrZ2tiOTFmbyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/bXpgshfh5uxupxGFqd/giphy.gif",
    "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExZWU3bjZxZm56MzA4amtva2d6ZXFjcDNscmI2dThyanA4ZWM2M2RuZiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/FY5vhK1zpoJGqap917/giphy.gif",
    "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExd3ZpbmQ5ZmZ2cHJ6cXRiNTU0YjN5d20zNHRtYjRsMnJ0ZTRidm5teCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/u7bymITK1tbP3tSAEg/giphy.gif",
    "https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExcmNxMmVienVhd3I3Z2JsNDhkbjFpaWV0bWhyazZlZXczd2ZnOWJmciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/B0d6gzvPMfY5Qy8pva/giphy.gif"

]

# ----------------------------
# Session state
# ----------------------------
st.session_state.setdefault("tafel", 3)
st.session_state.setdefault("factor", random.randint(1, 10))
ss.setdefault('sticker_5', random.sample(STICKERS, 5))
ss.setdefault('gifs_shuffle', random.sample(GIFS, len(GIFS)))
st.session_state.setdefault("stickers", 0)

st.session_state.setdefault("feedback", None)
st.session_state.setdefault("show_answer", None)

st.session_state.setdefault("input_key", 0)
st.session_state.setdefault("celebrate", False)
st.session_state.setdefault("gif_i", 0)


# ----------------------------
# Logic helpers
# ----------------------------
def new_problem():
    st.session_state.factor = random.randint(1, 10)
    st.session_state.input_key += 1
    st.rerun()

def reset_game():
    st.session_state.stickers = 0
    ss.sticker_5 = random.sample(STICKERS, 5)
    #ss.gifs_shuffle = random.sample(GIFS, len(GIFS))
    st.session_state.feedback = None
    st.session_state.show_answer = None
    st.session_state.celebrate = False
    st.session_state.gif_i = (st.session_state.gif_i + 1) % len(ss.gifs_shuffle)
    st.session_state.factor = random.randint(1, 10)
    st.session_state.input_key += 1

def reset_game2():
    st.session_state.stickers = 0
    ss.sticker_5 = random.sample(STICKERS, 5)
    #ss.gifs_shuffle = random.sample(GIFS, len(GIFS))
    st.session_state.feedback = None
    st.session_state.show_answer = None
    st.session_state.celebrate = False
    st.session_state.gif_i = (st.session_state.gif_i + 1) % len(ss.gifs_shuffle)
    st.session_state.factor = random.randint(1, 10)
    st.session_state.input_key += 1
    st.rerun()


def check_answer(answer, tafel, factor):
    try:
        answer = int(answer)
    except Exception:
        answer = None
    
    correct = tafel * factor

    show_answer = f"{tafel} × {factor} = {correct}"


    if (answer == correct) & (ss.stickers >= 5):
        feest(correct)

    elif answer == correct:
        goed(correct)
        st.session_state.stickers = min(5, st.session_state.stickers + 1)
        new_problem()
    else:
        verkeerd(correct)
        st.session_state.stickers = max(0, st.session_state.stickers - 1)
        new_problem()



# ----------------------------
# Styling
# ----------------------------
st.markdown(
    """
    <style>
    .circle-row {
        display:flex;
        gap:10px;
        justify-content:center;
        margin:12px 0;
    }
    .circle {
        width:55px;
        height:55px;
        border-radius:50%;
        border:3px solid #e11d48;
        display:flex;
        align-items:center;
        justify-content:center;
        font-size:30px;
    }
    div[data-testid="stTextInput"] input {
        font-size:40px !important;
        height:90px !important;
        padding:20px !important;
        text-align:center !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# ----------------------------
# Sidebar
# ----------------------------
st.sidebar.header("Kies een tafel")
st.sidebar.selectbox(
    "Tafel:",
    list(range(1, 11)),
    key="tafel",
    on_change=reset_game,
)

# ----------------------------
# Stickers (outside fragment!)
# ----------------------------
circles = '<div class="circle-row">'
for i in range(5):
    circles += f"<div class='circle'>{ss.sticker_5[i] if i < st.session_state.stickers else ''}</div>"
circles += "</div>"
st.markdown(circles, unsafe_allow_html=True)

# ----------------------------
# Celebration
# ----------------------------

@st.dialog(title = 'Oeps')
def verkeerd(correct):
    container = st.empty()
    container.error(f"Oh nee, die was fout. Het goede antwoord was: **{correct}**")  # Create a success alert
    time.sleep(5)  # Wait 5 seconds
    container.empty()

@st.dialog(title = 'Goed zo!')
def goed(correct):
    container = st.empty()
    container.success("Dat was het goede antwoord!")  # Create a success alert
    #container.info(f"Het goede antwoord was: **{correct}**")
    time.sleep(2)  # Wait 2 seconds
    container.empty()

@st.dialog(title = 'Hoera!')
def feest(correct):
    st.success("Goed zo!")  # Create a success alert
    st.balloons()
    st.image(ss.gifs_shuffle[st.session_state.gif_i])
    if st.button("Nieuwe ronde ▶️"):
        reset_game2()


# ----------------------------
# QUESTION 
# ----------------------------
def question(tafel, factor):
    st.markdown(
        f"<div style='text-align:center; font-size:56px; font-weight:800;'>"
        f"{factor} × {tafel} = ?</div>",
        unsafe_allow_html=True,
    )

    with st.form("answer_form"):
        key = f"antwoord_{st.session_state.input_key}"
        ans = st.number_input(
            "Antwoord",
            key = key,
            value=None,              # starts empty
            min_value=0,
            step=1,
            format="%d",
            label_visibility="collapsed",
        )
        if st.form_submit_button("Check"):
            check_answer(ss[key], tafel, factor)

question(ss.tafel, ss.factor)
