import streamlit as st
from random import choice

st.title('Random Name Generator')

fnames = ['Alex', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'George', 'Hannah', 'Ivan', 'Jenny', 'Karl', 'Linda', 'Mike', 'Nancy', 'Oscar', 'Pam', 'Quinn', 'Ralph', 'Sarah', 'Tom', 'Ursula', 'Victor', 'Wendy', 'Xavier', 'Yvonne', 'Zach']

lnames = ['Anderson', 'Baker', 'Clark', 'Davis', 'Evans', 'Foster', 'Garcia', 'Harris', 'Ivanov', 'Jones', 'King', 'Lopez', 'Miller', 'Nelson', 'Owens', 'Perez', 'Quinn', 'Roberts', 'Smith', 'Taylor', 'Upton', 'Vargas', 'Wright', 'Xu', 'Young']

btn = st.button('Generate name')

if btn:
    fn = choice(fnames)
    ln = choice(lnames)

    fullname = f'{fn} {ln}'

    st.success(fullname)


#streamlit run UI/app1.py ------- is used to run the program and is written in the Terminal.

#To kill the Terminal------ Ctrl+C or kill the terminal.