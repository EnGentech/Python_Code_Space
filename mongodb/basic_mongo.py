from pymongo import MongoClient

client = MongoClient()

db = client.school


def list_all(data_collection):
    return data_collection.find()


def insert_school(mongo_collection, **kwargs):
    """function to insert key value: data in mongo_collection"""
    for key, values in kwargs.items():
        save = mongo_collection.insert_one({key: values})
        print(save.inserted_id)


def update_topics(mongo_collection, name, topics):
    """function to insert key value: data in mongo_collection"""
    mongo_collection.update_many({'name': name}, {'$set': {'age': topics}})


def schools_by_topic(mongo_collection, topic):
    '''A function to return an array containing a certain topic of interest'''
    return mongo_collection.find({'age': topic})


def top_students(mongo_collection):

    myList = []
    values = mongo_collection.find()
    for x in values:
        treated = x.get('topics')
        all_scores = []
        try:
            for val in treated:
                all_scores.append(val.get('scores'))
                '''all_scores.append(val.get('score'))
            myList.append(sum(all_scores))'''

        except TypeError:
            pass
        myList.append(sum(all_scores))
    return myList


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    students_collection = client.my_db.students

    top_students = top_students(students_collection)
    for student in top_students:
        print(student)
        # print("[{}] {} => {}".format(student.get('_id'), student.get('name'), student.get('averageScore')))
