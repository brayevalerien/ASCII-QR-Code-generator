import argparse
from random import randint

import qrcode


def parse_arguments():
    parser = argparse.ArgumentParser("ASCII QR Code generator",
                                     description="A QR Code generator that outputs ASCII art, using specified characters.")
    parser.add_argument("--content", required=True, type=str,
                        help="Content to include in the generated QR code (usually an URL).")
    parser.add_argument("--characters", required=False, default="#", type=str,
                        help="String containing the characters to use in the output.")
    parser.add_argument("--filepath", required=False, default=None, type=str,
                        help="If not None, will print the output to a file at the path (creating the file if not already existent). Otherwise, prints the output to stdout.")
    parser.add_argument("--random", required=False, default=None, type=str,
                        help="If set to True, characters will be picked at random in the given string.")
    parser.add_argument("--correction", required=False, default="medium", type=str,
                        help="Error correction level of the generated QR code.")
    return parser.parse_args()


def generate_qrcode_data(content: str, correction: str = "medium") -> list[list[bool]]:
    """
    Create the QR code data (bits) 

    Args:
        content (str): content to include in the generated QR code.
        correction (str): error correction level of the generated QR code, can be of "low" (7%), "medium" (15%), "quality" (25%), "high" (30%). Defaults to "medium".

    Returns:
        list[list[bool]]: a matrix of booleans, True represents a black cell and False a white one.
    """
    correction_levels = {
        "low": qrcode.constants.ERROR_CORRECT_L,
        "medium": qrcode.constants.ERROR_CORRECT_M,
        "quality": qrcode.constants.ERROR_CORRECT_Q,
        "high": qrcode.constants.ERROR_CORRECT_H
    }
    qr = qrcode.QRCode(
        border=0, error_correction=correction_levels[correction.lower()])
    qr.add_data(content)
    qr.make()
    return qr.modules


def qrcode_data_to_ascii(qr_data: list[list[bool]], characters: str = "#", random: bool = False) -> list[str]:
    """
    Converts a QR data (bits representing each cell in the QR code) to a matrix of characters (a list of strings) included in the characters arguments, that represent the QR code.

    Args:
        qr_data (list[list[bool]]): bits representing each cell in the QR code.
        characters (str): string containing the characters to use in the output. Defaults to "#".
        random (bool): if kept to False, the characters will be used in the order they are given. If set to True, characters will be picked at random in the given string.

    Returns:
        list[str]: the ASCII representation of the QR code, ready to be printed to the stdout or into a text file.
    """
    if not characters:
        raise ValueError(
            "Character list is empty, please provide at least one character to use.")
    qr_ascii = []
    char_count = len(characters)
    # Quick and dirty nested for loops. Works well enough with qr codes for the moment.
    for line in qr_data:
        i = 0  # pointer to the character to use in the character string
        ascii_line = ""
        for bit in line:
            if bit:
                # Do it twice since characters are approx. 2 times taller than they are wide
                ascii_line += characters[randint(0,
                                                 char_count-1) if random else i]
                if not random:
                    i = (i+1) % char_count
                ascii_line += characters[randint(0,
                                                 char_count-1) if random else i]
                if not random:
                    i = (i+1) % char_count
            else:
                ascii_line += "  "
        qr_ascii.append(ascii_line)
    return qr_ascii


def print_output(qr_ascii: list[str], filepath: str = None) -> None:
    """
    Outputs a list of lines (strings) either to the stdout or to a file.

    Args:
        qr_ascii (list[str]): content to print.
        filepath (str, optional): If not None, will print the output to a file at the path (creating the file if not already existent). Otherwise, prints the output to stdout. Defaults to None.
    """
    output = "\n".join(qr_ascii)
    if filepath is None:
        print(output)
    else:
        with open(filepath, "w+", encoding="utf-8") as f:
            f.write(output)


if __name__ == "__main__":
    args = parse_arguments()

    qr_data = generate_qrcode_data(args.content)

    qr_ascii = qrcode_data_to_ascii(qr_data, args.characters, args.random)

    print_output(qr_ascii, args.filepath)
