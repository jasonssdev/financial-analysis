import os
import csv
import json
import pdfplumber
from openai import OpenAI
from dotenv import load_dotenv


# Load environment variables
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=OPENAI_API_KEY)

# Function to extract text from PDF file
def extract_text_from_pdf(pdf_path):
    """
    Extracts text page-by-page from a PDF file using pdfplumber.
    Returns a list of strings, each representing the text of a page.
    """
    pages_text = []
    with pdfplumber.open(pdf_path) as pdf_file:
        for page in pdf_file.pages:
            text = page.extract_text()
            if text:
                pages_text.append(text)
    return pages_text

def call_openai_api_for_card_data_extraction(text):
    """
    Sends 'text' to the OpenAI model with instructions to extract
    banking transactions from credit card statement in a JSON format.

    Returns a list of dictionaries with the following keys:
        - date
        - reference
        - description
        - amount (float)
    """
    # Define the system and user prompts
    system_prompt = (
        "You are an assistant that extracts banking transactions from credit card statement from text. "
        "Each credit card transaction typically appears in the format:\n\n"
        "DATE REFERENCE DESCRIPTION AMOUNT\n\n"
        "For example:\n"
        "AGO/04 08041440094965214 PEDIDOSYA $2,493.62-\n\n"
        "Instructions:\n"
        "1. Identify all lines that represent transactions.\n"
        "2. Return an array of JSON objects with these fields:\n"
        "   - date\n"
        "   - reference\n"
        "   - description\n"
        "   - amount (float)\n"
        "   (If the amount ends with '-', make it negative.)\n"
        "3. Return only the JSON, with no extra text.\n"
    )

    user_prompt = f"PDF text:\n\n{text}\n\nExtract the transactions in JSON."

    try:
        # Call the OpenAI API
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            temperature=0.0,
        )

        # Extract the data from the API response
        content = completion.choices[0].message.content
        transactions = json.loads(content)

        # return a list
        if isinstance(transactions, dict):
            transactions = [transactions]
        return transactions
    
    except Exception as e:
        print("Error when processing text with OpenAI:", e)
        return []
    
def save_transactions_to_csv(transactions_list, csv_filename="extracted_transactions.csv"):
    """
    Creates the 'data/preprocessed' folder if it doesn't exist, 
    and saves the transactions to a CSV file inside that folder.
    """
    preprocessed_folder = "data/preprocessed"
    os.makedirs(preprocessed_folder, exist_ok=True)
    
    output_csv_path = os.path.join(preprocessed_folder, csv_filename)

    # Define the columns to write in the CSV
    fieldnames = ["date", "reference", "description", "amount", "file", "page"]

    # Write the CSV file
    with open(output_csv_path, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for transaction in transactions_list:
            writer.writerow(transaction)

    print(f"Transactions extracted and saved in '{output_csv_path}'.")

def process_pdfs_in_folder(input_folder):
    """
    Iterates over all PDF files in 'input_folder', extracts text page by page,
    calls the OpenAI API for each page to identify transactions, and accumulates them.
    Finally, saves the transactions to a CSV file in the 'data/preprocessed' folder.
    """
    all_transactions = []

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(input_folder, filename)
            print(f"Processing: {pdf_path}")

            # 1. Extract text from each page of the PDF
            pages_text = extract_text_from_pdf(pdf_path)

            # 2. For each page, call OpenAI to identify transactions
            for page_index, text in enumerate(pages_text, start=1):
                extracted_transactions = call_openai_api_for_card_data_extraction(text)
                
                # Add metadata for file and page
                for transaction in extracted_transactions:
                    transaction["file"] = filename
                    transaction["page"] = page_index
                
                all_transactions.extend(extracted_transactions)

    # 3. Save all transactions to a CSV
    save_transactions_to_csv(all_transactions, csv_filename="extracted_transactions.csv")

if __name__ == "__main__":
    input_folder_path = "/Users/jasonssdev/Dev/Projects/bank-transactions/data/raw/credit-card"
    process_pdfs_in_folder(input_folder_path)