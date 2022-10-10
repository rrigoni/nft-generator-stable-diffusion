from prompts import  generatePrompts
from generator import generate
import os
from dotenv import load_dotenv

load_dotenv()

if __name__ == '__main__':
    generatePrompts()
    generate(int(os.environ["AMOUNT_OF_IMAGES_TO_GENERATE"]))