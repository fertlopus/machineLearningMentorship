from numpy import argmax


def one_hot_encode_text(text: str = None):
    """
    Function to one hot encode the text sequence.
    :param text: Any string representation of the text.
    :return: Numpy ndarray feature tensor of encoded text.
    """
    # define the alphanumerical possible values
    alpha_nums = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 '

    # define the mappings char to int
    char_to_int = dict((char, i) for i, char in enumerate(alpha_nums))

    # encode the input sequence
    encoded_sequence = [char_to_int[char] for char in text]

    #
    one_hot_encoded = list()
    for val in encoded_sequence:
        letter = [0 for _ in range(len(alpha_nums))]
        letter[val] = 1
        one_hot_encoded.append(letter)
    return one_hot_encoded


def one_hot_decode(encoded_sequence = None):
    # define the alphanumerical possible values
    alpha_nums = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789 '

    # define the mappings char to int
    int_to_char = dict((i, char) for i, char in enumerate(alpha_nums))
    string_decoded = ""
    for i in encoded_sequence:
        string_decoded += int_to_char[argmax(i)]
    return string_decoded
