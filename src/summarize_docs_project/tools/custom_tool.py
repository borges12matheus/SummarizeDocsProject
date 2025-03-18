from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from docling.document_converter import DocumentConverter
import pdfplumber
import os
import pytesseract
from pdf2image import convert_from_path

class File_to_Text_input(BaseModel):
    """Input schema for MyCustomTool."""
    filepath: str = Field(..., description="O caminho para o documento ou URL de um site do qual será extraído o texto")

class File_to_Text(BaseTool):
    name: str = "Conversor de Documentos em textos"
    description: str = (
        "Útil para extrair dados de documentos ou sites em vários formatos (PDF, CSV, TXT, HTML)"
    )
    args_schema: Type[BaseModel] = File_to_Text_input

    def _run(self, filepath: str) -> str:
        #Fazendo a leitura do arquivo no formato PDF
        def extract_text_with_pdfplumber(filepath):
            with pdfplumber.open(filepath) as pdf:
                text = "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
                return text

        def extract_text_from_image_pdf(pdf_path):
            """
            Extrai texto de um PDF baseado em imagens usando OCR.

            Parâmetros:
                pdf_path (str): Caminho para o arquivo PDF.

            Retorna:
                str: Texto extraído do PDF.
            """
            try:
                # Converte cada página do PDF em uma imagem
                pages = convert_from_path(pdf_path)
                text = ""

                for i, page in enumerate(pages):
                    print(f"Processando página {i+1}...")
                    text += pytesseract.image_to_string(page) + "\n"
                    print(text)
                # Verifica se algum texto foi extraído
                return text.strip() if text.strip() else "\nErro: Nenhum texto extraído.\n"

            except Exception as e:
                return f"Erro ao processar o PDF: {e}"

        #Fazer a leitura do arquivo usando o docling
        def extract_text(filepath):
            # Lista de formatos suportados
            supported_formats = {".pdf", ".docx", ".txt", ".csv", ".md"}

            # Obtém a extensão do arquivo
            _, file_extension = os.path.splitext(filepath)
            file_extension = file_extension.lower()  # Padroniza a extensão para minúsculas

            # Verifica se o arquivo está em um formato suportado
            if file_extension not in supported_formats:
                print(f"Erro: Formato de arquivo '{file_extension}' não suportado.")
                return None

            try:
                converter = DocumentConverter()
                process = converter.convert(filepath)

                if process and process.document:
                    text = process.document.export_to_text().strip() #Remove espaços em branco
                    
                    if not text or "<!-- missing-text -->" in text:
                        try:
                            text = extract_text_with_pdfplumber(filepath)
                            if not text or None in text:
                                extract_text_from_image_pdf(filepath)
                            else:
                                print("\nTexto extraído com sucesso usando PDFPLUMBER!\n")
                                print(text)
                            return text
                        except Exception as e:
                            print(f"Erro ao processar o arquivo: {e}")
                            return None
                    print("\nTexto extraído com sucesso usando Docling!\n")
                    print(text)
                    return text
                else:
                    print("\nErro: O documento não pôde ser processado.\n")
                    return None

            except Exception as e:
                print(f"Erro ao processar o arquivo: {e}")
                return None