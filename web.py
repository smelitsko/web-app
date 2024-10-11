import streamlit as st
import functions
# para detener: ctrl +c en la terminal
todos = functions.get_todos()


def add_todo():
    todo_local = st.session_state['new_todo'] + '\n'
    print(todo_local)
    todos.append(todo_local)
    functions.write_todos(todos)


st.title("My todo app")
st.subheader("This is my subheader")
st.write("This software is to increase my productivity")

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()



st.text_input(label="",placeholder="add a todo...", on_change=add_todo, key="new_todo")

print("Hello")

