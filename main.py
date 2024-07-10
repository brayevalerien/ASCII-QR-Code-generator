import qrcode
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser("ASCII QR Code generator",
                                     description="A QR Code generator that outputs ASCII art, using specified characters.")
    parser.add_argument("--content", required=True, type=str)
    parser.add_argument("--characters", required=False, default="#", type=str)
    parser.add_argument("--filepath", required=False, default=None, type=str)
    return parser.parse_args()

def generate_qrcode_data(content: str) -> list[list[bool]]:
    """
    Create the QR code data (bits) 

    Args:
        content (str): content to include in the generated QR code.

    Returns:
        list[list[bool]]: a matrix of booleans, True represents a black cell and False a white one.
    """
    qr = qrcode.QRCode(border=0)
    qr.add_data(content)
    qr.make()
    return qr.modules

def qrcode_data_to_ascii(qr_data: list[list[bool]], characters: str="#"):
    """
    Converts a QR data (bits representing each cell in the QR code) to a matrix of characters (a list of strings) included in the characters arguments, that represent the QR code.

    Args:
        qr_data (list[list[bool]]): bits representing each cell in the QR code.
        characters (str): string containing the characters to use in the output. Defaults to "#".

    Returns:
        _type_: _description_
    """
    qr_ascii = ["".join(["██" if bit else "  " for bit in line]) for line in qr_data]
    return qr_ascii

def print_output(qr_ascii: list[str], filepath: str=None) -> None:
    """
    Outputs a list of lines (strings) either to the stdout or to a file.

    Args:
        qr_ascii (list[str]): content to print.
        filepath (str, optional): ignored if None. If not None, will print the output to a file at the path (creating the file if not already existent). Defaults to None.
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
    
    qr_ascii = qrcode_data_to_ascii(qr_data, args.characters)
    
    print_output(qr_ascii, args.filepath)