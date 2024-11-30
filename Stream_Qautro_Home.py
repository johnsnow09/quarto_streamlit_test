import streamlit as st
import os

import subprocess
import sys


st.session_state.variable_check = 7+3
st.write(f"variable_check value is {st.session_state.variable_check}")



subprocess.run([f"{sys.executable}", "script.py"])

cmd_str = "quarto render test-4.qmd --output test4_cmd_out.html"

subprocess.call(cmd_str)