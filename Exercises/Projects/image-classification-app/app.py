from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os
from app_helper import *

# Initialize Flask app
app = Flask(__name__)


# Define route for the home page
@app.route("/")
def index():
    return render_template("index.html")


# Define route for file upload and processing
@app.route('/uploader', methods=['POST'])
def upload_file():
    predictions = ""
    if request.method == 'POST':
        f = request.files['file']
        # Save the uploaded file to ./static/uploads directory
        basepath = os.path.dirname(__file__)

        file_path = os.path.join(basepath, 'static', 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Get predictions from the helper function
        predictions = get_classes(file_path)
        pred_strings = []
        for _, pred_class, pred_prob in predictions:
            pred_strings.append(str(pred_class).strip() + " : " + str(round(pred_prob, 5)).strip())

        preds = ", ".join(pred_strings)
        print("preds:::", preds)

    # Render upload page with prediction results
    return render_template("upload.html", predictions=preds, display_image=f.filename)

# Run the Flask app
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=4100)
