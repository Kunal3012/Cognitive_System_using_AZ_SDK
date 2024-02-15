import sys
import os
'''


'''




def task1():
    print("Executing Task 1")
    # Full path to the directory containing the module
    module_directory = r'Python\text-analytics'

    # Add the module directory to sys.path
    sys.path.append(module_directory)

    # Import the module
    from main_text_analyzer_script import perform_text_analysis

    # Now you can use functions or classes from main_text_analyzer_script
    perform_text_analysis()
def task2():
    print("Executing Task 2")
    # Full path to the directory containing the module
    module_directory = r'Python\speech-translation'

    # Add the module directory to sys.path
    sys.path.append(module_directory)

    # Import the module
    from main_speech_translation_script import perform_translation

    # Now you can use functions or classes from main_text_analyzer_script
    perform_translation()

def task3():
    print("Executing Task 3")

def task4():
    print("Executing Task 4")

def task5():
    print("Executing Task 5")

def main():
    try:
        user_input = int(input("Enter a number between 1 and 5: "))
        
        if 1 <= user_input <= 5:
            if user_input == 1:
                task1()
            elif user_input == 2:
                task2()
            elif user_input == 3:
                task3()
            elif user_input == 4:
                task4()
            elif user_input == 5:
                task5()
        else:
            print("Invalid input. Please enter a number between 1 and 5.")
    
    except ValueError:
        print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    main()

