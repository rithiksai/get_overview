import streamlit as st
from io import StringIO
import PyPDF2
import first as bot

st.title("topic summarizer")

uploaded_file = st.file_uploader("upload your syllabus pdf to get an overview of the topics",type='pdf')

#function to extract text from a pdf file and returns a list of words in the pdf file
def extract_text_from_pdf(pdf):

    #opens the pdf with a read bytes mode
    with open(pdf, "rb") as f:
        reader = PyPDF2.PdfReader(pdf)
        pdf_text = []

        #reads the text in the pdf file
        for page in reader.pages:
            content = page.extract_text()
            pdf_text.append(content)
    
    return pdf_text

#this will work once you upload a pdf file
if uploaded_file is not None:
    #get the pdf file name
    file_name = uploaded_file.name

    #write the pdf file to the same folder as the code is in
    with open(file_name, "wb") as f:
            f.write(uploaded_file.getbuffer())
    
    #calss the extract function and stores it in a variable
    extracted_text = extract_text_from_pdf(file_name)

    #writes all the extracted text to a text file 
    file = open("text.txt", "w")
    for text in extracted_text:
         file.write(text)
    file.close()

    with open("text.txt", "r") as f:
        txt = f.read()
        st.subheader("Extracted Text:")
        st.text_area("Extracted Text", value=txt, height=300)
        
        start_word = st.text_input("Start Word (e.g., Module:3)", "Module:3")
        end_word = st.text_input("End Word (e.g., Module:6)", "Module:6")

           

        #extracting 
        if(st.button("Get Overview")):
            #result = extract_text_between_words(txt, start_word, end_word)
            
            query1 = f"from the given below text can you give me the list of topics unedr the modules {start_word} to {end_word}.and By taking all the below given topics, can you explain in brief about them as if making me preparing for an exam. Give real world expamles to relate for the topics and if any topic has a numerical problem please explain with examples: {txt}"
            result = bot.callAPI(query1)
            link = result

            st.subheader("Overview")
            st.text_area("A brief overview of all the topics", value=result, height=600)

        


           

           


    

        
            