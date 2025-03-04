import streamlit as st
import os
import tempfile
import requests
# import markdown2
# from weasyprint import HTML
from summarize_docs_project.main import run
import asyncio

try:
    asyncio.get_running_loop()
except RuntimeError:
    asyncio.run(asyncio.sleep(0))  # Força a criação de um loop


st.title("📄 Resuma seus Docs com IA")
st.write("Escolha entre fazer upload de um documento ou inserir uma URL para resumir.")

option = st.radio("Escolha a origem do documento:",
                  ["Upload do Arquivo", "Inserir URL"])
summary = None

if option == "Upload do Arquivo":
    
    #Upload do arquivo
    uploaded_file = st.file_uploader("Faça upload de um documento", 
                                    type=["pdf", "txt","csv", "docx"])
    if uploaded_file:
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp_file:
            temp_file.write(uploaded_file.read())
            temp_path = temp_file.name
            
        st.write(f"📂 Arquivo salvo temporariamente em: {temp_path}")   
        
        
        with st.spinner("Processando o Arquivo ..."):
            try:
                summary = str(run(temp_path))
                os.remove(temp_path)
                
            except Exception as e:
                st.error(f"Erro ao processar o documento: {e}")
                os.remove(temp_path)
elif option == "Inserir URL":
    url = st.text_input("Cole aqui a URL da página para resumir:")
    
    if st.button("Gerar Resumo"):
        if url:
            with st.spinner("Extraindo conteúdo da URL ..."):
                try:
                    response = requests.get(url)
                    if response.status_code == 200:
    
                        summary = str(run(url))
                    
                    else:
                        st.error(f"Erro ao acessar a URL: {response.status_code}")
                except Exception as e:
                    st.error(f"Erro ao processar a URL: {e}")
                    
if summary:
    st.success("Resumo gerado com sucesso!")
    st.write(summary)
                        
    filename_input = st.text_input("Escolha o nome do arquivo de saída (sem extensão):","resumo")
                        
    md_filename = f"{filename_input.strip()}.md" if filename_input.strip() else "resumo.md"
    pdf_filename = f"{filename_input.strip()}.pdf" if filename_input.strip() else "resumo.pdf"
    
    with open(md_filename,"w", encoding="utf-8") as md_file:
        md_file.write(summary)
        
    # def markdown_to_pdf(md_text, filename):
    #     html = markdown2.markdown(md_text)
    #     HTML(string=html).write_pdf(filename)
        
    # markdown_to_pdf(summary, pdf_filename)
                            
    with open(md_filename, "rb") as file:
        st.download_button(
            label="📥 Baixar Resumo em Markdown",
            data= file,
            file_name=md_filename,
            mime="text/markdown"
        )
        
    with open(pdf_filename, "rb") as file:
        st.download_button(
            label="📥 Baixar Resumo em PDF",
            data= file,
            file_name=pdf_filename,
            mime="application/pdf"
        )
    os.remove(md_filename)  # Remove o arquivo markdown após o download
    os.remove(pdf_filename)