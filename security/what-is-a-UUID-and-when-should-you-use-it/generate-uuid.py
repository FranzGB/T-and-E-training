import uuid
import os


def save_file(file_data):
    # generate a UUID to use as the file name
    file_name = str(uuid.uuid4())

    # get the file extension from the original file name
    _, extension = os.path.splitext(file_data.name)

    # create a new file with the UUID as the name
    file_path = f"./{file_name}{extension}"
    with open(file_path, "wb") as f:
        f.write(file_data.read())

    return file_path


myfile = open("test.txt", "rb")
print(save_file(myfile))
