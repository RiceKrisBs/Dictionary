import json


def get_user_input() -> str:
    while True:
        user_word = input("Enter a word: ")
        user_word = user_word.strip().lower()
        if user_word:
            return user_word
        print("Your word must contain letters.")

def get_word_definition(word: str, dictionary: dict) -> list:
    return dictionary.get(word, [])

def print_definitions(definitions: list) -> None:
    if definitions:
        for definition in definitions:
            print(definition)
    else:
        print("No definition found.")


if __name__ == '__main__':
    with open('data.json', 'r') as f:
        dictionary_data = json.load(f)

    word = get_user_input()
    definitions = get_word_definition(word, dictionary_data)
    print_definitions(definitions)