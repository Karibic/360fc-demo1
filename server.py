import os
from flask import Flask, render_template

app = Flask(__name__)

def print_files_in_directory(directory):
    for entry in os.scandir(directory):
        if entry.is_file():
            print(entry.path)
        elif entry.is_dir():
            print_files_in_directory(entry.path)

@app.route('/')
def hello_world():
    print("helloworld!")
    print_files_in_directory('/mnt/')
    return render_template('/mnt/data/index.html')

if __name__ == '__main__':
    app.run()
