from flask import Blueprint, jsonify, request
from models import Laptops
from laptops_crud import *

laptops_bp = Blueprint('laptops', __name__)
# laptopscrud = LaptopsCrud(session)

'''Endpoints for laptops blueprint'''

# endpoint to add a laptop
@laptops_bp.route('/laptops/add', methods = ['POST'])
def add_laptop():
    data = request.get_json()
    required_fields = ['laptop_name', 'laptop_number', 'specification']
    missing_fields = [field for field in required_fields if field not in data]

    if missing_fields:
        return jsonify({
            'Error': 'Required field(s) is missing!',
            'Missing fields': missing_fields
            }), 400
    
    laptop_name = data['laptop_name']
    laptop_number = data['laptop_number']
    specification = data['specification']

    existing_laptop = laptopscrud.select_laptop_by_number(laptop_number)
    if existing_laptop:
        return jsonify({
            'Error': 'Laptop number must be unique'
        }), 400
    
    try:
        message = laptopscrud.insert_laptop(laptop_name, laptop_number, specification)
        return jsonify({
            'Message': message
        }), 201
    except Exception as e:
        return jsonify({
            'Error': f'There was an error inserting the new laptop: {e}.'
        }), 500
    

#endpoint to get all laptops
@laptops_bp.route('/laptops', methods = ['GET'])
def get_laptops():
    laptops = laptopscrud.select_all_laptop()

    laptops_list = [{
        'laptop_name': laptop.laptop_name,
        'laptop_number': laptop.laptop_number,
        'specification': laptop.specification
    } for laptop in laptops]

    return jsonify({
        'Laptop': laptops_list
    }), 200


# endpoint to get a laptop by name
@laptops_bp.route('/laptops/name/<string:laptop_name>', methods=['GET'])
def get_laptop_by_name(laptop_name):
    try:
        # query database for the laptop
        laptop = laptopscrud.select_laptop_by_name(laptop_name)

        if laptop:
            return jsonify({
                'laptop_name': laptop.laptop_name,
                'laptop_number': laptop.laptop_number,
                'specification': laptop.specification
            }), 200
        else:
            return jsonify({
                'Error': f'Laptop with name "{laptop_name}" does not exist.'
            }), 404
        
    except Exception as e:
        return jsonify({
            'Error': f'There was an error: {e}'
        }), 500



# endpoint to get a laptop by number
@laptops_bp.route('/laptops/number/<int:laptop_number>', methods=['GET'])
def get_laptop_by_number(laptop_number):
    try:
        # query database for the laptop
        laptop = laptopscrud.select_laptop_by_number(laptop_number)

        if laptop:
            return jsonify({
                'laptop_name': laptop.laptop_name,
                'laptop_number': laptop.laptop_number,
                'specification': laptop.specification
            }), 200
        else:
            return jsonify({
                'Error': f'Laptop with number {laptop_number} does not exist.'
            }), 404
        
    except Exception as e:
        return jsonify({
            'Error': f'There was an error: {e}'
        }), 500



# endpoint to update laptop
@laptops_bp.route('/laptops/number/<int:laptop_number>', methods=['PUT'])
def update_laptop_by_number(laptop_number):
    try:
        data = request.get_json()
        laptop_name = data.get('laptop_name')
        specification = data.get('specification')

        laptop_to_update = laptopscrud.update_laptop(
            laptop_name = laptop_name,
            laptop_number = laptop_number,
            specification = specification
            )

        if laptop_to_update:

            return jsonify({
                'Message': f"Laptop with number {laptop_number} updated successfully.",
                'updated_data': {
                    'laptop_name': laptop_to_update.laptop_name,
                    'laptop_number': laptop_to_update.laptop_number,
                    'specification': laptop_to_update.specification
                }
            }), 200
        
        else:
            return jsonify({'Error': f"Laptop with number {laptop_number} not found."}), 404
        
    except Exception as e:
        return jsonify({'rEror': f'There was an error: {e}'}), 500


# endpoint to delete a laptop
@laptops_bp.route('/laptops/delete/<int:laptop_number>', methods=['DELETE'])
def delete_laptop_by_number(laptop_number):
    try:
        
        laptop = laptopscrud.delete_laptop(laptop_number)
        
        if laptop:
            return jsonify({
                'Message': laptop
                }), 200
        
        else:
            return jsonify({
                'Error': 'Laptop not Found'
                }), 404

    except Exception as e:
        return jsonify({'Error': f'There was an error: {e}'}), 500


