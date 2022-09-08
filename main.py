import os
import sys
import cv2
import argparse
import pytesseract

# Path to tesseract executable
pytesseract.pytesseract.tesseract_cmd = os.path.join(os.environ.get("TESSERACT_PATH"), "tesseract.exe")

INPUT_PATH: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), "input")
OUTPUT_PATH: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")

def breaker(num: int=50, char: str="*") -> None: print("\n" + num*char + "\n")

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("--filename", "-f", default="Test_1.png", help="Filename of the image file")
    parser.add_argument("--timeout", "-t", type=float, default=10.0, help="Max time after which to quit the OCR process")
    parser.add_argument("--save", "-s", action="store_true", help="Flag to save the detected text")
    args = parser.parse_args()

    assert args.filename in os.listdir(INPUT_PATH), "File not found in input directory"

    image = cv2.cvtColor(src=cv2.imread(os.path.join(INPUT_PATH, args.filename), cv2.IMREAD_COLOR), code=cv2.COLOR_BGR2RGB)

    try:
        data = pytesseract.image_to_string(image, timeout=args.timeout)
    except:
        breaker()
        print("Timeout Error")
        breaker()
    

    if args.save:
        with open(os.path.join(OUTPUT_PATH, "output.txt"), "w+") as fp: fp.write(data)
    else:
        breaker()
        print(data)
        breaker()


if __name__ == "__main__":
    sys.exit(main() or 0)
