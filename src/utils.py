import os

def ensure_directory_exists(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def save_text(text, filename):
    with open (filename, "w") as file:
        file.write(text)

if __name__ == "__main__":
    ensure_directory_exists("output")
    ensure_directory_exists("data")
