FILEPATH = "works.txt"

def get_works(filepath=FILEPATH):
    """ Read a text file and return the list of works items """

    with open(filepath, 'r') as file_local:
        works_local = file_local.readlines()
    return works_local

def write_works(works_arg, filepath=FILEPATH):
    """ Write the works items list in the text file """
    with open(filepath, 'w') as file:
        file.writelines(works_arg)


if __name__ == "__main__":
    print("Hello")
    print(get_works())

