# Flask CRUD API for Laptop Management

This project demonstrates how to create and test RESTful APIs using Flask. The API provides CRUD operations for managing laptops.

## Table of Contents
1. [Getting Started](#getting-started)
2. [API Endpoints and Instructions](#api-endpoints-and-instructions)
   1. [Add a Laptop](#add-a-laptop)
   2. [Get All Laptops](#get-all-laptops)
   3. [Get a Laptop by Name](#get-a-laptop-by-name)
   4. [Get a Laptop by Laptop Number](#get-a-laptop-by-laptop-number)
   5. [Update a Laptop by Laptop Number](#update-a-laptop-by-laptop-number)
   6. [Delete a Laptop by Laptop Number](#delete-a-laptop-by-laptop-number)
   7. [Search Laptops by Partial Matches](#search-laptops-by-partial-matches)
3. [Testing the API Using Postman](#testing-the-api-using-postman)
4. [Error Handling](#error-handling)
5. [Run the Application](#run-the-application)

## Getting Started

Follow the steps below to set up and test the API.

### Prerequisites

- Python 3
- Flask (`pip install flask`)
- Postman (or any API testing tool)

### Project Structure
Flask_CRUD_API/
- app.py
- config.py
- laptops_blueprint.py
- laptops_crud.py
- models.py
- README.md


## API Endpoints and Instructions
### Add a Laptop
- Route: /laptops/add
- Method: POST
- Description: Adds a new laptop.
- Request Example:
```json
{
  "name": "Dell Inspiron",
  "laptop_number": "12345",
  "specifications": "16GB RAM, 1TB SSD, Intel i7"
}
```
Response:
Success (201 Created):
```json
{
  "message": "Laptop added successfully."
}
```

Error (400 Bad Request):
```json
{
  "error": "Laptop number must be unique or required fields are missing."
}
```
### Get All Laptops
- Route: /laptops
- Method: GET
- Description: Retrieves all laptops.
- Response:
Success (200 OK):
```json
[
  {
    "name": "Dell Inspiron",
    "laptop_number": "12345",
    "specifications": "16GB RAM, 1TB SSD, Intel i7"
  },
  ...
]
```
### Get a Laptop by Name
- Route: /laptops/name/<name>
- Method: GET
- Description: Retrieves a laptop with the specified name.
- Response:
Success (200 OK):
```json
{
  "name": "Dell Inspiron",
  "laptop_number": "12345",
  "specifications": "16GB RAM, 1TB SSD, Intel i7"
}
```
Error (404 Not Found):
```json
{
  "error": "Laptop not found."
}
```
### Get a Laptop by Laptop Number
- Route: /laptops/number/<laptop_number>
- Method: GET
- Description: Retrieves a laptop with the specified laptop number.
- Response:
Success (200 OK):
```json
{
  "name": "Dell Inspiron",
  "laptop_number": "12345",
  "specifications": "16GB RAM, 1TB SSD, Intel i7"
}
```
Error (404 Not Found):
```json
{
  "error": "Laptop not found."
}
```

### Update a Laptop by Laptop Number
- Route: /laptops/update/<laptop_number>
- Method: PUT
- Description: Updates a laptop's details.
- Request Example:
```json
{
  "name": "Dell Inspiron 15",
  "specifications": "32GB RAM, 2TB SSD, Intel i9"
}
```
Response:
Success (200 OK):
```json
{
  "message": "Laptop updated successfully."
}
```
Error (404 Not Found):
```json
{
  "error": "Laptop not found."
}
```

### Delete a Laptop by Laptop Number
- Route: /laptops/delete/<laptop_number>
- Method: DELETE
- Description: Deletes a laptop.
- Response:
- Success (200 OK):
```json
{
  "message": "Laptop deleted successfully."
}
```
Error (404 Not Found):
```json
{
  "error": "Laptop not found."
}
```
### Search Laptops by Partial Matches:
- Route: /laptops/search
- Method: GET
- Description: Searches laptops by partial matches in name or specifications.
- Example Search: http://localhost:5000/laptops/search/item_searched
- Response:
```json
{
"name": "Dell Inspiron",
"laptop_number": "12345",
"specifications": "16GB RAM, 1TB SSD, Intel i7"
}
```

## Testing the API Using Postman
### Add a Laptop

- Select POST method and enter http://localhost:5000/laptops/add
- Add a JSON body with laptop details.
- Click Send and verify the response.

### Get All Laptops
- Select GET method and enter http://localhost:5000/laptops
- Click Send to retrieve the list of laptops.

### Get a Laptop by Name
- Select GET method and enter http://localhost:5000/laptops/name/name-to-select-by
- Replace <name> with the laptop's name.
- Click Send and verify the response.

### Get a Laptop by Laptop Number
- Select GET method and enter http://localhost:5000/laptops/number/laptop-number-to-select-by
- Replace <laptop_number> with the desired laptop number.
- Click Send and verify the response.

### Update a Laptop
- Select PUT method and enter http://localhost:5000/laptops/update/laptop-number-to-select-by
- Replace <laptop_number> with the laptop's number.
- Add a JSON body with updated details.
- Click Send and verify the response.

### Delete a Laptop
- Select DELETE method and enter http://localhost:5000/laptops/delete/laptop-number-to-select-by
- Replace <laptop_number> with the laptop's number.
- Click Send and verify the response.

### Search for a Laptop
- 

## Error Handling
- Ensure all responses are in JSON format with appropriate status codes.
- Invalid JSON inputs or missing fields return a 400 Bad Request error.

## Run the Application
- Clone the repository.
- Navigate to the Flask_CRUD_API directory.
- Run the following command:
```bash
python app.py
```
- Test the API on http://localhost:5000 using Postman.