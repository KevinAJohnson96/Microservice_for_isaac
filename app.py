from flask import Flask, send_file
from service import fetch_data_and_plot

app = Flask(__name__)

@app.route('/graphOfAverages')
def index():
    image_stream = fetch_data_and_plot()

    # Return the image as a response
    image_stream.seek(0)
    return send_file(image_stream, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True, port=8000)
