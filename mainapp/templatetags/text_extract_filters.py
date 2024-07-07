# your_app/templatetags/text_extract_filters.py

from django import template
import os
from PyPDF2 import PdfReader
from docx import Document

register = template.Library()

@register.filter
def extract_text(file_path):
    file_extension = os.path.splitext(file_path)[1].lower()
    if file_extension == '.pdf':
        return extract_text_from_pdf(file_path)
    elif file_extension in ['.doc', '.docx']:
        return extract_text_from_docx(file_path)
    elif file_extension == '.txt':
        return extract_text_from_txt(file_path)
    else:
        with open(file_path, 'r') as f:
            content = f.read()
        return content

def extract_text_from_pdf(file_path):
    text = ""
    reader = PdfReader(file_path)
    for page_num in range(len(reader.pages)):
        text += reader.pages[page_num].extract_text()
    return text

def extract_text_from_docx(file_path):
    doc = Document(file_path)
    return "\n".join([para.text for para in doc.paragraphs])

def extract_text_from_txt(file_path):
    with open(file_path, 'r') as file:
        return file.read()