from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from docling.document_converter import DocumentConverter


class File_to_Text_input(BaseModel):
    """Input schema for MyCustomTool."""
    filepath: str = Field(..., description="O caminho para o documento que será extraído o texto")

class File_to_Text(BaseTool):
    name: str = "Conversor de Documentos em textos"
    description: str = (
        "Útil para extrair dados de documentos em vários formatos (PDF, TXT, HTML)"
    )
    args_schema: Type[BaseModel] = File_to_Text_input

    def _run(self, filepath: str) -> str:
        #Fazer a leitura do arquivo usando o docling
        converter = DocumentConverter()
        process = converter.convert(filepath)
        text = process.document.export_to_text()
        return text.split()