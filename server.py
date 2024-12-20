from flask import Flask, jsonify, request, render_template
from config import db
app = Flask(__name__)

# Sample product data with categories
products = [
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 999.99},
    {"id": 2, "name": "Smartphone", "category": "Electronics", "price": 699.99},
    {"id": 3, "name": "Running Shoes", "category": "Sports", "price": 89.99},
    {"id": 4, "name": "Tennis Racket", "category": "Sports", "price": 199.99},
    {"id": 5, "name": "Coffee Maker", "category": "Home", "price": 79.99}
]

# Route for welcome page
@app.route('/')
def home():
    return """
    <h1>Welcome to the Product API</h1>
    <p>Available endpoints:</p>
    <ul>
        <li>/api/product - Get all products</li>
        <li>/api/product/count - Get product count</li>
        <li>/api/catalog/[category] - Get products by category</li>
        <li>/api/categories - Get all categories</li>
        <li>/about - About page</li>
    </ul>
    """

# Route for about page
@app.route('/about')
def about():
    return """
    <h1>About</h1>
    <p>This is a REST API built with Flask that manages product catalog information.</p>
    """

# Get all products
@app.route('/api/product')
def get_products():
    return jsonify(products)
db.products.insert_one(product)

# Get product count
@app.route('/api/product/count')
def get_product_count():
    return jsonify({"count": len(products)})

# Get products by category
@app.route('/api/catalog/<category>')
def get_products_by_category(category):
    category_products = [product for product in products if product['category'].lower() == category.lower()]
    if not category_products:
        return jsonify({"error": "Category not found"}), 404
    return jsonify(category_products)
def fix_id(obj):
    obj["id"] = str(obj)["id"])
    return obj


# Get unique categories
@app.route('/api/categories')
def get_categories():
    unique_categories = list(set(product['category'] for product in products))
    return jsonify(unique_categories)

if __name__ == '__main__':
    app.run(debug=True)