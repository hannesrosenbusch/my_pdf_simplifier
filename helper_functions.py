from openai import OpenAI
from PyPDF2 import PdfReader

def extract_text_from_pdf(pdf_file):
    """Function to extract text from the first few pages of a PDF."""
    pdf_reader = PdfReader(pdf_file)
    text = ""
    for page in pdf_reader.pages[:3]:  # Extract text from the first 3 pages
        text += page.extract_text()
    return text


def simplify_text(text):
    client = OpenAI()

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": f"Simplify the language in this text, so a 12 year old can understand it."},
            {"role": "user", "content": f"{text}"}
        ]
    )

    return completion.choices[0].message.content