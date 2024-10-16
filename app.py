## this file is responsible for creating LLM application

from dotenv import load_dotenv

load_dotenv()

import streamlit as st
import os
import sqlite3
import google.generativeai as genai

#configure genai key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## function to load google gemini model and provide queries as response
def get_gemini_response(question,prompt):
    model= genai.GenerativeModel('gemini-pro')
    response= model.generate_content([prompt[0],question])
    return response.text

## function to retrieve query from database
def read_sql_query(sql,db):
    conn= sqlite3.connect(db)
    cur= conn.cursor()
    cur.execute(sql)
    rows= cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows
    
    
## Defining the prompt
prompt= [
    """
    You are an expert in converting a english text into sql query!
    The SQL database has the name Student and has the following columns - NAME, CLASS, SECTION
    \n\nFor example, \nExample 1: How many entries of records are present?,
    The SQL command will be something like this- SELECT COUNT(*) FROM STUDENT;
    \n Example 2: Tell me all students studying in data science class?
    The sql command will be something like this- SELECT * FROM STUDENT WHERE CLASS="Data Science";
    also the sql code should not have ''' in begining or end and sql word in output
    """
]

## Streamlit app

st.set_page_config(page_title="I can retrieve any SQL query")
st.header("Gemini app to retrieve SQL data")

question = st.text_input("Input: ", key="input")

submit= st.button("Ask the Question")

# if submit is clicked
if submit:
    response= get_gemini_response(question,prompt)
    print(response)
    response= read_sql_query(response,"student.db")
    st.subheader("The response is: ")
    for row in response:
        print(row)
        st.header(row)
        
