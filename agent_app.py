import streamlit as st
import agent_lib as glib


st.set_page_config(page_title="Agent", page_icon="🤖")
st.title("Agent")


prompt = st.text_input("Ask me about weather in any city in the world")

if prompt:
    next_step = glib.TOOL_PROMPT.format(
        tools_string=glib.tools_string, user_input=prompt)

    for i in range(5):
        output = glib.invoke_model(next_step).strip()
        done, next_step = glib.single_agent_step(next_step, output)

        if not done:
            st.write('Not done yet ' + output)
        else:
            st.write('Final answer is ' + next_step)
            break
