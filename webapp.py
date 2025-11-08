import streamlit as st
import functions

tasks = functions.get_todos()

def add_task():
    task = st.session_state['new_todo'] + '\n'
    print(task)
    tasks.append(task.capitalize())
    functions.write_todos(tasks)
    st.session_state['new_todo'] = ""
st.title('To-Do Web App')
st.write('This is a minimalistic To-Do app coded on python and hosted on '
         'Streamlit')
st.text_input(label="Enter your task : ",placeholder='New task...',
              on_change=add_task, key = "new_todo")

for index,task in enumerate(tasks):
    checkbox = st.checkbox(task, key=task)
    if checkbox:
        tasks.pop(index)
        functions.write_todos(tasks)
        del st.session_state[task]
        st.rerun()