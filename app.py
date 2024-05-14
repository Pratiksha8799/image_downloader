
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 18:47:52 2024

@author: Pr@t!ksha
"""
# Import necessary modules

from flask import Flask, render_template, request
from image_extracter import Image_Extraction

# Set up Flask application
app = Flask(__name__)
app.secret_key = "imp"

# # Configure logging to write to a log file
# logging.basicConfig(
#     filename='scraping_log.log',  # Specify the log file name
#     level=logging.INFO,           # Set the logging level (INFO or DEBUG)
#     format='%(asctime)s - %(levelname)s - %(message)s'  # Customize the log format
# )

# # Redirect stdout and stderr to the log file
# sys.stdout = sys.stderr = open('scraping_log.log', 'a')


    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['GET', 'POST'])
def download():
    print('yes')
    if request.method == 'POST':
            name = request.form['url']
            number = request.form['number']
            if number == '':
                 number = 1
            number = int(number)
            # print(type(number))
            # print(number)
            img = Image_Extraction()
            img.download_images(name,number)
            print('Thank you for your patience.')
    return render_template('download.html')


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)

    