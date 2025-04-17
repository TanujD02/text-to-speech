from flask import Flask, render_template, request, send_file
import edge_tts
import asyncio
import os
import time

app = Flask(__name__)
OUTPUT_FOLDER = "static"  # Save audio files in the static folder

# Function to convert text to speech
async def text_to_speech(text, output_file):
    tts = edge_tts.Communicate(text, "en-IN-NeerjaExpressiveNeural")
    await tts.save(output_file)

@app.route('/', methods=['GET', 'POST'])
def index():
    text = ""  # Initialize text variable
    audio_file = None

    if request.method == 'POST':
        text = request.form['text']
        if text.strip():
            timestamp = int(time.time())  # Generate a unique filename based on timestamp
            audio_file = f"{OUTPUT_FOLDER}/output_{timestamp}.mp3"

            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(text_to_speech(text, audio_file))

            return render_template('index.html', text=text, audio_file=audio_file)

    return render_template('index.html', text=text, audio_file=None)

@app.route('/download/<filename>')
def download(filename):
    return send_file(f"{OUTPUT_FOLDER}/{filename}", as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
