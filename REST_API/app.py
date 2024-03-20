from flask import Flask, request, jsonify

app = Flask(__name__)

book_list = [
{
            'id': 1,
            'author': "Gentle",
            'language': "English",
            'title': "EnGentech, the pride of time"
        },
{
            'id': 2,
            'author': "Chime",
            'language': "Spanish",
            'title': "Talu Escasor"
        }
]

@app.route("/books", methods=["GET", "POST"])
def books():
    if request.method == "GET":
        if len(book_list) > 0:
            return jsonify(book_list)
        else:
            return "Nothing in list", 404

    if request.method == 'POST':
        new_author = request.form['author']
        new_language = request.form['language']
        new_title = request.form['title']
        iD = book_list[-1]['id']+1 # this is the id of the previous book list

        new_obj = {
            'id': iD,
            'author': new_author,
            'language': new_language,
            'title': new_title
        }
        # Lets append the list to the previous

        book_list.append(new_obj)
        #then return the file in json
        return jsonify(book_list), 201

    # Note tha we are using an in-memory list which will only be available only on runtime,
    # This is to say that the storage ability is not permanent as we are not populating
    # the list in a database where the information can later be retrived

@app.route("/books/<int:id>", methods=['GET', 'PUT', 'DELETE'])
def book_id(id):
    if request.method == "GET":
        for x in book_list:
            if x['id'] == id:
                return jsonify(x)
            else:
                return "Id: {} is not available".format(id)

    elif request.method == "PUT":
        for x in book_list:
            if x['id'] == id:
                x['author'] = request.form['author']
                x['language'] = request.form['language']
                x['title'] = request.form['title']
                new_update = {
                    'id': id,
                    'author': x['author'],
                    'language': x['language'],
                    'title': x['title']
                }
                return jsonify(new_update)

    elif request.method == "DELETE":
        for key, value in enumerate(book_list):
            if key == id - 1:
                book_list.pop(key)
                return jsonify(book_list)


if __name__ == "__main__":
    app.run(debug=True)