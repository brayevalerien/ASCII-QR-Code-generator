# ASCII-QR-Code-generator
Generate ASCII art of QR codes and choose the characters to use in the output.

## Installation
> This code is written in Python. To download the code and run it, make sure [Git](https://git-scm.com/) and [Python](https://www.python.org/) are installed on your machine before installing this project.

Start by clonning this repo and `cd` into it:
```bash
git clone https://github.com/brayevalerien/ascii-qr-code-generator
cd ASCII-QR-Code-generator
```

Then install the `qrcode` library:
```bash
pip install qrcode
```

## Usage
Run the `main.py` script with Python. Here is the usage string:
```
ASCII QR Code generator [-h] --content CONTENT [--characters CHARACTERS] [--filepath FILEPATH] [--random RANDOM] [--correction CORRECTION]

A QR Code generator that outputs ASCII art, using specified characters.

options:
  -h, --help            show this help message and exit
  --content CONTENT     Content to include in the generated QR code (usually an URL).
  --characters CHARACTERS
                        String containing the characters to use in the output.
  --filepath FILEPATH   If not None, will print the output to a file at the path (creating the file if not already existent). Otherwise, prints the output to stdout.
  --random RANDOM       If set to True, characters will be picked at random in the given string.
  --correction CORRECTION
                        Error correction level of the generated QR code.
```

> [!TIP]
> Use characters that are dark enough (e.g. `#` is dark, `.` is light) to ensure the resulting QR code is scannable.
