import random
import streamlit as st
import time

ss = st.session_state

st.set_page_config(page_title="Tafels oefenen", page_icon="🧮", layout="centered")



STICKERS = ["🐶", "🐱", "🐭", "🐹", "🐰", "🦊", "🐻", "🐼", "🐸", "🦄"]

GIFS = [ 
    "https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExemwwZXVlOXprZHpoenl6dDU4c2FnZXZ3dmQ3MmduY2sydmZwcGN5dCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3UkqVq3F50bVCi9URl/giphy.gif",
]

# ----------------------------
# Session state
# ----------------------------
st.session_state.setdefault("tafel", 2)
st.session_state.setdefault("factor", random.randint(1, 10))
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
    st.session_state.feedback = None
    st.session_state.show_answer = None
    st.session_state.celebrate = False
    st.session_state.gif_i = (st.session_state.gif_i + 1) % len(GIFS)
    st.session_state.factor = random.randint(1, 10)
    st.session_state.input_key += 1

def reset_game2():
    st.session_state.stickers = 0
    st.session_state.feedback = None
    st.session_state.show_answer = None
    st.session_state.celebrate = False
    st.session_state.gif_i = (st.session_state.gif_i + 1) % len(GIFS)
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


    if (answer == correct) & (ss.stickers >= 10):
        feest(correct)

    elif answer == correct:
        goed(correct)
        st.session_state.stickers = min(10, st.session_state.stickers + 1)
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
for i in range(10):
    circles += f"<div class='circle'>{STICKERS[i] if i < st.session_state.stickers else ''}</div>"
circles += "</div>"
st.markdown(circles, unsafe_allow_html=True)

# ----------------------------
# Celebration
# ----------------------------

@st.dialog(title = 'Oeps')
def verkeerd(correct):
    container = st.empty()
    container.error("Oh nee")  # Create a success alert
    container.info(f"Het goede antwoord was: **{correct}**")
    time.sleep(1)  # Wait 2 seconds
    container.empty()

@st.dialog(title = 'Goed zo!')
def goed(correct):
    container = st.empty()
    container.success("Goed zo!")  # Create a success alert
    container.info(f"Het goede antwoord was: **{correct}**")
    time.sleep(1)  # Wait 2 seconds
    container.empty()

@st.dialog(title = 'Hoera!')
def feest(correct):
    st.success("Goed zo!")  # Create a success alert
    st.info(f"Het goede antwoord was: **{correct}**")
    st.balloons()
    st.image(GIFS[st.session_state.gif_i])
    if st.button("Nieuwe ronde ▶️"):
        reset_game2()


# ----------------------------
# QUESTION FRAGMENT
# ----------------------------
def question(tafel, factor):
    st.markdown(
        f"<div style='text-align:center; font-size:56px; font-weight:800;'>"
        f"{factor} × {tafel} = ?</div>",
        unsafe_allow_html=True,
    )

    with st.form("answer_form"):
        key = f"antwoord_{st.session_state.input_key}"
        st.text_input("Antwoord", key=key, label_visibility="collapsed")
        if st.form_submit_button("Check"):
            check_answer(st.session_state[key], tafel, factor)

question(ss.tafel, ss.factor)


