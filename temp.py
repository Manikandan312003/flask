from flask import Flask, jsonify, request
import json

app = Flask(__name__, static_folder='static')

with open('books.json') as f:
	books_data = json.load(f)
print(books_data)

@app.route('/')
def index():
	return app.send_static_file('index.html')

@app.route('/books_db/books')
def get_books():
	search_term = request.args.get('search')
	print(search_term)
	if search_term:
		filtered_books = [book for book in books_data if search_term.lower() in book['title'].lower()]
		return jsonify(filtered_books)
	else:
		return jsonify(books_data)

if __name__ == '__main__':
	app.run(port=8000, debug=True)
