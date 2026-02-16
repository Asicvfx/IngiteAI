import pdfplumber
import openpyxl
import io
import os

class KnowledgeService:
    @staticmethod
    def extract_text_from_file(file_obj):
        """Extracts text content from PDF or Excel files."""
        ext = os.path.splitext(file_obj.name)[1].lower()
        content = ""

        try:
            if ext == '.pdf':
                with pdfplumber.open(file_obj) as pdf:
                    pages = [page.extract_text() for page in pdf.pages if page.extract_text()]
                    content = "\n\n".join(pages)
            
            elif ext in ['.xlsx', '.xls']:
                wb = openpyxl.load_workbook(file_obj, data_only=True)
                all_text = []
                for sheet in wb.worksheets:
                    all_text.append(f"Sheet: {sheet.title}")
                    for row in sheet.iter_rows(values_only=True):
                        row_text = " | ".join([str(cell) if cell is not None else "" for cell in row])
                        if row_text.strip():
                            all_text.append(row_text)
                content = "\n".join(all_text)
            
            elif ext == '.txt':
                content = file_obj.read().decode('utf-8')
                
        except Exception as e:
            print(f"Error parsing file {file_obj.name}: {e}")
            content = f"Error parsing file: {str(e)}"

        return content.strip()
