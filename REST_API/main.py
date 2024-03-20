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
a = 2
for key, value in enumerate(book_list):
    if key == a - 1:
        book_list.pop(key)
        print(value)