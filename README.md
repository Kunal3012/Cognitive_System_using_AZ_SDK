# OmniCognitionSuite: Complete Project Outline


Project in two languages:

- Python 
- C#

The `main.py` file serves as the entry point for users to trigger specific tasks, allowing for flexibility and customization based on user requirements. The modular design ensures that each module can be employed independently or collaboratively, depending on the desired functionality.

###User Interface (UI)

- **Type:** Command-Line Interface (CLI)
  
- **Output:** Directly in the terminal for Text Analysis, Computer Vision, and Speech modules.

- **Image Processing:** Changes saved directly in the image file or as a new image.

```bash
# Example Commands:
text-analysis analyze -text "This is a sample text."
image-processing ocr -image path/to/image.jpg
speech-to-text -audio path/to/audio.wav
```

This CLI design ensures simplicity and efficiency, suitable for both individual users and automated processes.

---
Setting up a virtual environment for your project is a good practice to isolate dependencies and avoid conflicts between different projects. Here are general steps to set up a virtual environment using Python's `venv` module:

- **Navigate to your project directory:**
   Open a terminal or command prompt and navigate to the directory where you want to create your virtual environment.

   ```bash
   cd path/to/your/project
   ```

- **Activate the virtual environment:**
   Activate the virtual environment. The activation command depends on your operating system.

   On Linux/macOS:
   ```bash
   source venv/bin/activate
   ```

   On Windows:
   ```bash
   venv\Scripts\activate
   ```

   Once activated, your terminal prompt should change to indicate the virtual environment.

- **Install dependencies:**
   Now, you can install the required packages for your project using `pip`. For example:

   ```bash
    pip install python-dotenv
    pip install Pillow
    pip install matplotlib
    pip install numpy
    pip install azure-ai-textanalytics==5.3.0
    pip install azure-cognitiveservices-speech==1.30.0
    pip install azure-cognitiveservices-vision-computervision==0.7.0
    pip install tk
   ```

- **Deactivate the virtual environment:**
   When you're done working on your project, deactivate the virtual environment:

   ```bash
   deactivate
   ```

   This returns you to the global Python environment.