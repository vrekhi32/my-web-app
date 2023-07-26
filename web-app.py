import streamlit as st
import functions

works = functions.get_works()

def add_work():
    work = st.session_state["new_work"] + "\n"
    works.append(work)
    functions.write_works(works)


st.title("My Works to do app")
st.subheader("This is my works to be done page")
st.write("This app is to increase your productivity")

for index, work in enumerate(works):
    checkbox = st.checkbox(work, key=work)
    if checkbox:
        works.pop(index)
        functions.write_works(works)
        del st.session_state[work]
        st.experimental_rerun()

st.text_input(label="", placeholder="Enter the work", on_change=add_work, key='new_work')



