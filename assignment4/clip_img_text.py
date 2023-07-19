import torch
import clip
from PIL import Image
import numpy as np

# load the model
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

# text prompt
text = clip.tokenize(["image with text", "image with NO text"])

# preprocess functions
def preprocess_image_func(image_path):
    image = Image.open(image_path)
    preprocess_image = preprocess(image).unsqueeze(0).to(device)
    return preprocess_image

# path to images
path = "/mnt/c/Users/Mon/Desktop/mfec_intern/assignment4/text_inside_image"

# images for testing
image_with_text = preprocess_image_func(path + "/image_with_text4.jpg") # should print --> "This image most likely contain text!"
image_without_text = preprocess_image_func(path + "/no_text4.jpg") # should print --> "This image most likely does NOT contain text!"

with torch.no_grad():
    image_features = model.encode_image(image_with_text)
    text_features = model.encode_text(text)
    
    logits_per_image, logits_per_text = model(image_with_text, text)
    probs = logits_per_image.softmax(dim=-1).cpu().numpy()

# with torch.no_grad():
#     image_features = model.encode_image(image_without_text)
#     text_features = model.encode_text(text)
    
#     logits_per_image, logits_per_text = model(image_without_text, text)
#     probs = logits_per_image.softmax(dim=-1).cpu().numpy()

# convert numpy array into string
probs = np.array2string(probs[0], precision=8, separator=' ')

# create an array of string to extract
probs_strings = probs[1:-1].split()

prob_yes_text= float(probs_strings[0])
prob_no_text = float(probs_strings[1])

print("Probability of containing text: ", prob_yes_text)
print("Probability of containing NO text: ", prob_no_text)

# checking
if (prob_yes_text > prob_no_text):
    print("This image most likely contain text!")
elif (prob_yes_text < prob_no_text):
    print("This image most likely does NOT contain text!")
else:
    print("Cannot Tell")