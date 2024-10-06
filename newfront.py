import streamlit as st
import read_pdf as rp
import os
import first as bot

st.title("PDF Topic Extractor")

uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")

if uploaded_file is not None:
    file_name = "syllabus1.pdf"

    #save_path = os.path.join("uploaded_files",file_name)
    #os.makedirs(os.path.dirname(save_path), exist_ok=True)

    with open(file_name, "wb") as f:
            f.write(uploaded_file.getbuffer())
    #st.write(save_path)
    
    et = rp.extract_text_from_pdf(file_name)
    file_text = " ".join(et)

        # Display the extracted text (optional)
    st.subheader("Extracted Text:")
    st.text_area("Extracted Text", value=file_text, height=300)

        # Choose start and end words
    start_word = st.text_input("Start Word (e.g., Module:3)", "Module:3")
    end_word = st.text_input("End Word (e.g., Module:6)", "Module:6")

    if st.button("Extract Topics"):
            # Extract the topics between the start and end words
        result = rp.extract_text_between_words(file_text, start_word, end_word)

            # Display the extracted topics
        st.subheader("Extracted Topics")
        st.text_area("Topics between selected modules:", value=result, height=200)

            # Query the bot API (optional)
        query = f"From the given text, give me a numbered list of all the topics in all the different modules separated module-wise: {result}"
        response = bot.callAPI(query)
            
        st.subheader("API Response")
        st.text_area("API Response", value=response, height=200)


