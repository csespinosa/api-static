"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def get_all_members():
    """Get all family members"""
    members = jackson_family.get_all_members()
    return jsonify(members), 200

@app.route('/member/<int:member_id>', methods=['GET'])
def get_member(member_id):
    """Get a specific family member by ID"""
    member = jackson_family.get_member(member_id)
    if member is None:
        return jsonify({"message": "Member not found"}), 404
    return jsonify(member), 200

@app.route('/member', methods=['POST'])
def add_member():
    """Add a new family member """

    member_data = request.get_json()
    
 
    if not all(key in member_data for key in ["first_name", "age", "lucky_numbers"]):
        return jsonify({"message": "Missing required fields"}), 400
    

    jackson_family.add_member(member_data)
    

    return jsonify({}), 200

@app.route('/member/<int:member_id>', methods=['DELETE'])
def delete_member(member_id):
    """
    Delete a family member by ID
    """
    success = jackson_family.delete_member(member_id)
    if not success:
        return jsonify({"message": "Member not found"}), 404
    
    return jsonify({"done": True}), 200


if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)