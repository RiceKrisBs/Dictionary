import json
from spellchecker import SpellChecker
from typing import Optional, NoReturn


def get_user_word() -> str:
    while True:
        user_word = input("Enter a word: ")
        user_word = user_word.strip().lower()
        if user_word:
            return user_word
        print("Your word must contain letters.\n")


def get_word_definitions(word: str) -> list:
    return dictionary_data.get(word)


def print_definitions(definitions: list) -> NoReturn:
    for definition in definitions:
        print(definition)


def get_possible_correction(word: str) -> Optional[dict]:
    spell = SpellChecker()
    possible_correction = spell.correction(word)
    correction_definitions = get_word_definitions(possible_correction)
    if word != possible_correction and correction_definitions:
        return {'word': possible_correction,
                'definitions': correction_definitions}


def confirm_correction(correction: str) -> bool:
    confirmation = input(f"Did you mean {correction}? Enter y/n: ")
    return confirmation.strip().lower() in ('y', 'yes')


if __name__ == '__main__':
    with open('data.json', 'r') as f:
        dictionary_data = json.load(f)
    user_word = get_user_word()
    definitions = get_word_definitions(user_word)

    if definitions:
        print_definitions(definitions)

    else:
        correction = get_possible_correction(user_word)
        if correction:
            user_confirmation = confirm_correction(correction['word'])

            if user_confirmation:
                print_definitions(correction['definitions'])

            else:
                print("Please check your spelling.")

        else:
            print(f"Sorry, {user_word} is not in this dictionary.")
