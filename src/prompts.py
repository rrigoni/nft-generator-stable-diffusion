from dotenv import load_dotenv
import random
import os
load_dotenv()

numberOfObjects = int(os.environ["NUMBER_OF_OBJECTS"])
numberOfStyles = int(os.environ["NUMBER_OF_STYLES"])
numberOfActions = int(os.environ["NUMBER_OF_ACTIONS"])
numberOfBackgrounds = int(os.environ["NUMBER_OF_BACKGROUNDS"])
numberOfDetails = int(os.environ["NUMBER_OF_DETAILS"])

totalPromptSize = int(os.environ["AMOUNT_OF_IMAGES_TO_GENERATE"])

def readFile(file):
    with open(file) as my_file:
        return my_file.readlines();

def randItem(list):
    return random.choice(list)
    #return list[choice]

def buildItem(list, size):
    items = []
    for x in range(size):
        item = item = randItem(list)
        while item in items:
            item = randItem(list)
        items.append(item)
    return items


def generatePrompts():
    os.remove("outputs/prompts.txt")
    actions = readFile("resources/actions.txt")
    background = readFile("resources/background.txt")
    details = readFile("resources/details.txt")
    objects = readFile("resources/objects.txt")
    styles = readFile("resources/styles.txt")

    prompts = []

    f = open('outputs/prompts.txt', 'w')

    for n in range(totalPromptSize):
        _objects = buildItem(objects, numberOfObjects)
        _styles = buildItem(styles, numberOfStyles)
        _background = buildItem(background, numberOfBackgrounds)
        _details = buildItem(details, numberOfDetails)
        _actions = buildItem(actions, numberOfActions)
        prompt = [*_objects, *_styles, *_details, *_actions, *_background]
        newPrompt = []
        for y in prompt:
            newPrompt.append(y.replace("\n", ""))
        f.write(",".join(newPrompt) + "\n")
    f.close()
