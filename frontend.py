import streamlit as st
import PyPDF2
import first as bot

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    pdf_text = []

    for page in reader.pages:
        content = page.extract_text()
        pdf_text.append(content)
    
    return pdf_text

# Function to get the topics between two modules
def extract_text_between_words(text, start_word, end_word):
    words = text.split()

    try:
        start_idx = words.index(start_word)
        end_idx = words.index(end_word, start_idx)
        
        return " ".join(words[start_idx:end_idx])
    
    except ValueError:
        return "Start word or end word not found in the text."

# Streamlit UI
def main():
    st.title("PDF Topic Extractor")
    
    uploaded_file = st.file_uploader("Upload a PDF file", type="pdf")
    
    if uploaded_file is not None:
        # Extract text from the PDF

        file_name = "syllabus1.pdf"

   

        with open(file_name, "wb") as f:
            f.write(uploaded_file.getbuffer())

        extracted_text = extract_text_from_pdf(file_name)
        file_text = " ".join(extracted_text)

        # Display the extracted text (optional)
        st.subheader("Extracted Text:")
        st.text_area("Extracted Text", value=file_text, height=300)

        # Choose start and end words
        start_word = st.text_input("Start Word (e.g., Module:3)", "Module:3")
        end_word = st.text_input("End Word (e.g., Module:6)", "Module:6")

        if st.button("Extract Topics"):
            # Extract the topics between the start and end words
            result = extract_text_between_words(file_text, start_word, end_word)

            # Display the extracted topics
            st.subheader("Extracted Topics")
            st.text_area("Topics between selected modules:", value=result, height=200)

            # Query the bot API (optional)
            query = f"From the given text, give me a numbered list of all the topics in all the different modules separated module-wise: {result}"
            response = bot.callAPI(query)
            
            st.subheader("API Response")
            st.text_area("API Response", value=response, height=200)

if __name__ == "__main__":
    main()
