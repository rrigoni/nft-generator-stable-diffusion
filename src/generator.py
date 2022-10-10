from dotenv import load_dotenv
import io
import warnings
from PIL import Image
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation
import os

load_dotenv()




def generate(amount):
    prompts = []
    counter = 1;
    with open("outputs/prompts.txt") as my_file:
        prompts = my_file.readlines()
    for prompt in prompts:
        generateImage(prompt, counter)
        counter = counter + 1
        if counter == amount:
            break;


def generateImage(prompt, imageNumber):
    print("Generating image " + str(imageNumber) + " for prompt " + prompt)
    stability_api = client.StabilityInference(key=os.environ['STABLE_DIFFUSION_API_KEY'],verbose=True)
    answers = stability_api.generate(prompt=prompt, width=512, height=512)
    for resp in answers:
        for artifact in resp.artifacts:
            if artifact.finish_reason == generation.FILTER:
                warnings.warn("Your request activated the API's safety filters and could not be processed. Please modify the prompt and try again.")
            if artifact.type == generation.ARTIFACT_IMAGE:
                img = Image.open(io.BytesIO(artifact.binary))
                img.save("outputs/img/" + str(imageNumber) + ".png")



