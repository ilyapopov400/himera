import json

if __name__ == "__main__":
    with open("credit", "r") as my_file:
        result = json.loads(my_file.read())
        print(result)
