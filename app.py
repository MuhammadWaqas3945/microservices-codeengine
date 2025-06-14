from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/book')
def get_book():
    return jsonify({
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald"
    })

if __name__ == '__main__':
    app.run(port=5001)
