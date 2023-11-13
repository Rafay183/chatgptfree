import subprocess

# Define the path to the "run.py" script within the "gui" folder
script_path = 'g4f/gui/run.py'

# Function to run the "run.py" script
def run_gui_app():
    try:
        subprocess.run(['python', script_path], check=True)
    except subprocess.CalledProcessError:
        print("An error occurred while running the script.")

if __name__ == '__main__':
    run_gui_app()
