import sys
import os
import csv
from datetime import datetime

LOG_FILE = "usage_log.csv"

def log_usage(function_name):
    current_time = datetime.now().strftime("%H:%M:%S hrs %a %d/%m/%Y")
    with open(LOG_FILE, mode='a', newline='') as log_file:
        writer = csv.writer(log_file)
        writer.writerow([current_time, function_name])

def task1():
    print("Executing Text Analysis")
    log_usage("Text Analysis")
    module_directory = r'Python\text-analytics'
    sys.path.append(module_directory)
    from main_text_analyzer_script import perform_text_analysis
    perform_text_analysis()

def task2():
    print("Executing Speech Translation")
    log_usage("Speech Translation")
    module_directory = r'Python\speech-translation'
    sys.path.append(module_directory)
    from main_speech_translation_script import perform_translation
    perform_translation()

def task3():
    print("Executing Image Analysis")
    log_usage("Image Analysis")
    module_directory = r'Python\image-analysis'
    sys.path.append(module_directory)
    from main_image_analysis_script import perform_image_analysis
    perform_image_analysis()

def task4():
    print("Executing Text Translation")
    log_usage("Text Translation")
    module_directory = r'Python\text-translation'
    sys.path.append(module_directory)
    from main_text_translation_script import perform_text_translation
    perform_text_translation()


def main():
    try:
        user_input = int(input("\n\t    1. Text Analysis    \n\t    2. Speech Translation    \n\t    3. Image Analysis  \n\t    4. Text Translation \n\n Enter a number between 1 and 5: "))
        
        if 1 <= user_input <= 5:
            if user_input == 1:
                task1()
            elif user_input == 2:
                task2()
            elif user_input == 3:
                task3()
            elif user_input == 4:
                task4()
        else:
            print("Invalid input. Please enter a number between 1 and 5.")
    
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()
