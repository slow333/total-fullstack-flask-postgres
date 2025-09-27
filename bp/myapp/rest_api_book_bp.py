from flask import Blueprint, request, jsonify
from db import get_mydb as get_db # type: ignore

book_bp = Blueprint('book_bp_psycopg2', __name__, url_prefix='/apps/books')

@book_bp.route('/', methods=['GET'])
def get_books():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM book;')
    books = cursor.fetchall()
    return jsonify(books)

@book_bp.route('/', methods=['POST'])
def create_book():
    data = request.get_json()
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        'INSERT INTO book (title, author, language, published_date) VALUES (%s, %s, %s, %s) RETURNING id;',
        (data.get("title"), data.get("author"), data.get("language"), data.get("published_date"))
    )
    new_id = cursor.fetchone()[0]
    db.commit()

    new_book = {
        "id": new_id,
        "title": data.get("title"),
        "author": data.get("author"),
        "language": data.get("language"),
        "published_date": data.get("published_date")
    }
    return jsonify(new_book), 201
@book_bp.route('/<int:book_id>', methods=['GET'])
def get_book(book_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM book WHERE id = %s;', (book_id,))
    book = cursor.fetchone()

    if book is None:
        return jsonify({"error": "Book not found"}), 404
    book_dict = {
        "id": book[0],
        "title": book[1],
        "author": book[2],
        "language": book[3],
        "published_date": book[4]
    }
    return jsonify(book_dict)
@book_bp.route('/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    db = get_db()
    cursor = db.cursor()
    cursor.execute(
        'UPDATE book SET title = %s, author = %s, language = %s, published_date = %s WHERE id = %s;',
        (data.get("title"), data.get("author"), data.get("language"), data.get("published_date"), book_id)
    )
    db.commit()

    return jsonify({"message": "Book updated successfully"})

@book_bp.route('/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute('DELETE FROM book WHERE id = %s;', (book_id,))

    db.close()
    return jsonify({"message": f"Book deleted successfully: {book_id}"})