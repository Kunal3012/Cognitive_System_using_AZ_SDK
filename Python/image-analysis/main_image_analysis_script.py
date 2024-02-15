# image_analysis_module.py

from dotenv import load_dotenv
import os
from tkinter import Tk, filedialog
from image_analyzer_module import ImageAnalyzer
import sys

class ImageAnalysis:
    def __init__(self):
        try:
            # Get Configuration Settings
            load_dotenv()
            self.cog_endpoint = os.getenv('COG_SERVICE_ENDPOINT')
            self.cog_key = os.getenv('COG_SERVICE_KEY')

        except Exception as ex:
            print(ex)

    def get_image_file(self):
        root = Tk()
        root.withdraw()  # Hide the main window

        image_file = filedialog.askopenfilename(
            title="Select an Image File",
            filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.gif"), ("All Files", "*.*")]
        )

        root.destroy()  # Close the main window

        return image_file

    def analyze_image(self):
        try:
            # Get the image file path using the file dialog
            image_file = self.get_image_file()

            if not image_file:
                print("No image selected. Exiting.")
                return

            # Create an instance of ImageAnalyzer
            image_analyzer = ImageAnalyzer(self.cog_endpoint, self.cog_key)

            # Analyze the image
            image_analyzer.analyze_image(image_file)

        except Exception as ex:
            print(ex)

def perform_image_analysis():
    image_analysis = ImageAnalysis()
    image_analysis.analyze_image()

if __name__ == "__main__":
    perform_image_analysis()
