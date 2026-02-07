import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

import streamlit as st
import time
from app import Pipeline

st.set_page_config(page_title="PPE Context Vision", layout="wide")

st.title("🦺 PPE Context-Aware Safety System")
st.caption("Simulated Industrial Safety Intelligence Demo")

pipeline = Pipeline()

run = st.toggle("▶ Run Simulation", key="run_toggle")


log_placeholder = st.empty()

while run:
    pipeline.step()
    time.sleep(0.5)

    logs = pipeline.logger.get_recent()

    with log_placeholder.container():
        st.subheader("Live Events")
        for row in logs[-10:]:
            st.json(row)

    run = st.session_state["run_toggle"]

