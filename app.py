from flask import Flask, jsonify

app = Flask(__name__)

posts = [{"id": 1, "title": "Post 1"}, {"id": 2, "title": "Post 2"}]
comments = [{"id": 1, "post_id": 1, "text": "Nice!"}, {"id": 2, "post_id": 2, "text": "Cool!"}]
albums = [{"id": 1, "name": "Album 1"}, {"id": 2, "name": "Album 2"}]

@app.route('/')
def home():
    return jsonify({"message": "Simple API"})

@app.route('/posts')
def get_posts():
    return jsonify(posts)

@app.route('/comments')
def get_comments():
    return jsonify(comments)

@app.route('/albums')
def get_albums():
    return jsonify(albums)

if __name__ == '__main__':
    app.run(debug=True)