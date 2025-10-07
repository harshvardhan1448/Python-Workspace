from flask import Flask, render_template, jsonify, request


###WSGI Application
app = Flask(__name__)

#initial data in my do list
items = [
    {"id": 1, "name":"Item 1", "description": "This is item 1"},
    {"id": 2, "name":"Item 2", "description": "This is item 2"},
]

@app.route("/")
def Home():
    return "Welcome to the Sample To Do List Flask Application!"
## Get Retrieve all items
@app.route('/items', methods=['GET'])
def get_items():
    return jsonify(items)
## Get: Retrieve a specific item by ID
@app.route('/items/<int:item_id>', methods=['GET'])
def get_item(item_id):
    item = next((item for item in items if item['id']== item_id), None)
    if item:
        return jsonify(item)
    return jsonify({"message": "Item not found"}), 404

##Post: Create a new task - api
@app.route('/items', methods=['POST'])
def create_item():
    if not request.json or 'name' not in request.json:
        return jsonify({"message": "Invalid request"}), 400
    new_item = {
        "id" : items[-1]["id"] +1 if items else 1,
        "name": request.json["name"],
        "description": request.json["description"]
    }
    items.append(new_item)
    return jsonify(new_item), 201

##Put : Update an existing item
@app.route('/items/<int:item_id>', methods=['PUT'])
def update_item(item_id):
    item = next((item for item in items if item['id'] == item_id), None)
    if not item:
        return jsonify({"message": "Item not found"}), 404
    if not request.json:
        return jsonify({"message": "Invalid request"}), 400
    item['name'] = request.json.get('name', item['name'])
    item['description'] = request.json.get('description', item['description'])
    return jsonify(item)

##Delete : Delete an item
@app.route('/items/<int:item_id>', methods=['DELETE'])
def delete_item(item_id):
    global items
    items = [item for item in items if item['id'] != item_id]
    return jsonify({"message": "Item deleted"})

if __name__ == "__main__":
    app.run(debug = True)