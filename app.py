from flask import Flask, render_template
import os

app = Flask(__name__)

# Path to your text and WAV files
TEXT_FILE_PATH = 'output_files/Sherlock-short_annotated_fixed.txt'
AUDIO_FILE_PATH = 'output_wavs/Sherlock_audiobook.wav'

@app.route('/')
def home():
    # Read the content of your text file
    audio_filename = os.path.basename(AUDIO_FILE_PATH)
    
    with open(TEXT_FILE_PATH, 'r') as file:
        text_content = file.read()
        
    # Make the audio file path accessible from the HTML template
    

    return render_template('index.html', audio_filename=audio_filename,text_content=text_content)

if __name__ == '__main__':
    app.run(debug=True)
