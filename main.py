import os
import sys
import cv2
import pytesseract

# Path to tesseract executable
pytesseract.pytesseract.tesseract_cmd = "C:/Program Files/Tesseract-OCR/tesseract.exe"

READ_PATH = "Files"
SAVE_PATH = "Processed"

if not os.path.exists(SAVE_PATH):
    os.makedirs(SAVE_PATH)


def breaker(num: int=50, char: str="*") -> None:
    print("\n" + num*char + "\n")


def main():

    args_1: tuple = ("--file", "-f")
    args_2: tuple = ("--timeout", "-t")
    args_3: tuple = ("--save", "-s")
    
    filename: str = None
    timeout: float = 5.0
    save: bool = False

    if args_1[0] in sys.argv: filename = sys.argv[sys.argv.index(args_1[0]) + 1]
    if args_1[1] in sys.argv: filename = sys.argv[sys.argv.index(args_1[1]) + 1]

    if args_2[0] in sys.argv: timeout = float(sys.argv[sys.argv.index(args_2[0]) + 1])
    if args_2[1] in sys.argv: timeout = float(sys.argv[sys.argv.index(args_2[1]) + 1])

    if args_3[0] in sys.argv or args_3[1] in sys.argv: save = True

    assert filename is not None, "No file specified"

    image = cv2.cvtColor(src=cv2.imread(os.path.join(READ_PATH, filename), cv2.IMREAD_COLOR), code=cv2.COLOR_BGR2RGB)

    try:
        data = pytesseract.image_to_string(image, timeout=timeout)
    except:
        breaker()
        print("Timeout Error")
        breaker()
    
    if save:
        with open(os.path.join(SAVE_PATH, "output.txt"), "w+") as fp:
            fp.write(data)
    else:
        breaker()
        print(data)
        breaker()


if __name__ == "__main__":
    sys.exit(main() or 0)
