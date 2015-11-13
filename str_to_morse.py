morse_dict = {
    'a': '.-',
    'b': '-...',
    'c': '-.-.',
    'd': '-..',
    'e': '.',
    'f': '..-.',
    'g': '--.',
    'h': '....',
}


def convert_string_to_morse(uni_string):
    """
    function for converting a string to morse code.

    uni_string, any string, may only contain a-z.

    return a list of dots and hyphens.

    """
    return [morse_dict[char] for char in uni_string]


def main():
    print(' '.join(convert_string_to_morse('abc')))


if __name__ == '__main__':
    main()
