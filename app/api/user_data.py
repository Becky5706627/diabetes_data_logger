from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, current_user
from werkzeug.utils import secure_filename
import os
from app.utils.database import db

from app.models.user_data import UserData

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))  # Get the absolute path to the directory of the current file
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'uploads')
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

user_data_blueprint = Blueprint('user_data', __name__)


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@user_data_blueprint.route('/upload_image', methods=['POST'])
@jwt_required()
def upload_image():
    if 'file' not in request.files:
        return jsonify({"message": "No file part"}), 400
    file = request.files['file']

    if file.filename == '':
        return jsonify({"message": "No selected file"}), 400

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(UPLOAD_FOLDER, filename))

        # Save to database
        data_entry = UserData(user_id=current_user.id, image_filename=filename)
        db.session.add(data_entry)
        db.session.commit()

        return jsonify({"message": "Image uploaded successfully", "filename": filename, "data_id": data_entry.id}), 201
    else:
        return jsonify({"message": "Invalid file type"}), 400

