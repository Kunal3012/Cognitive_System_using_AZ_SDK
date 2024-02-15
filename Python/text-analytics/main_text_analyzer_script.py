# main_text_analyzer_script.py
import logging
from dotenv import load_dotenv
import os
from tkinter import Tk, filedialog
from text_analyzer_module import TextAnalyzer

def load_environment_variables():
    load_dotenv()
    cog_endpoint = os.getenv('COG_SERVICE_ENDPOINT')
    cog_key = os.getenv('COG_SERVICE_KEY')
    return cog_endpoint, cog_key

def initialize_text_analyzer(cog_endpoint, cog_key):
    text_analyzer = TextAnalyzer(cog_endpoint, cog_key)
    text_analyzer.initialize_client()
    return text_analyzer

def get_file_path():
    root = Tk()
    root.withdraw()  # Hide the main window

    file_path = filedialog.askopenfilename(
        title="Select a Text File",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )

    root.destroy()  # Close the main window

    return file_path

def perform_text_analysis():
    logging.basicConfig(level=logging.INFO)

    cog_endpoint, cog_key = load_environment_variables()

    if not cog_endpoint or not cog_key:
        logging.error("Missing environment variables. Please set COG_SERVICE_ENDPOINT and COG_SERVICE_KEY.")
        exit(1)

    text_analyzer = initialize_text_analyzer(cog_endpoint, cog_key)

    try:
        file_path = get_file_path()

        if file_path:
            # Analyze the text from the specified file
            text_analyzer.analyze_file(file_path)
        else:
            logging.info("No file selected. Exiting.")
    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    perform_text_analysis()
