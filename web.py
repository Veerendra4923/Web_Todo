import streamlit as st
import functions
def add_todo():
    tod=st.session_state['input']+"\n"
    todos.append(tod)
    functions.write_todos(todos)

todos=functions.get_todos()
st.title("My todo app")
st.subheader("Created by creators of WNW!")
st.write("This to increase your productivity")
for i,j in enumerate(todos):
    cb=st.checkbox(j,key=j)
    if cb:
        todos.pop(i)
        functions.write_todos(todos)
        del st.session_state[j]
        st.rerun()


st.text_input(label="",placeholder="Add a todo",key="input",
              on_change=add_todo)
