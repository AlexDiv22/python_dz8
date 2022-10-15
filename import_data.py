import json

def import_data(data, sep=None):
    with open('list_students.json', 'a+') as file:
        if sep == None:
            for i in data:
                file.write(f"{i}\n")
            file.write(f"\n")
        else:
            json.dump(data, file,)
            file.write(f"\n")