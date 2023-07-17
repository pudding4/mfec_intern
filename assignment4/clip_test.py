import os
import torch
import clip
from PIL import Image
from torchvision.datasets import CIFAR100
from scipy import spatial

# load the model
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

# phrases, text
text = clip.tokenize(["an airplane with a clear sky", "many books on a book shelf", "buildings with clear sky", "a black car", "a yellow fish underwater", 
                      "food on a table", "bright orange frog", "a panda", "many people in one location", "person texting on a phone"]).to(device)

# preprocess functions
def preprocess_image_func(image_path):
    image = Image.open(image_path)
    resized_image = image.resize((100, 100))
    preprocess_image = preprocess(resized_image).unsqueeze(0).to(device)
    return preprocess_image

# path to the images
folder_path = "/mnt/c/Users/Mon/Desktop/mfec_intern/assignment4/images"

# get a list of all image files in the folder
image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

preprocessed_images = []
# preprocess each images in a folder and store into preprocessed_images arr
for image_file in image_files:
    image_path = os.path.join(folder_path, image_file)
    # print(image_path)
    done = preprocess_image_func(image_path)
    # print(done.shape)
    preprocessed_images.append(done)

image_dog = preprocess_image_func("dog.jpg")
image_airplane = preprocess_image_func("airplane.jpg")

# print(preprocessed_images)

# convert to vectors
with torch.no_grad():
    image_features = []
    times = len(preprocessed_images)
    for i in range(times):
        image_features.append(model.encode_image(preprocessed_images[i]))
    text_features = model.encode_text(text)

    for i in range(times):
        logits_per_image, logits_per_text = model(preprocessed_images[i], text)
        probs = logits_per_image.softmax(dim=-1).cpu().numpy()

        #result = 1 - spatial.distance.cosine(text, preprocessed_images)
        probs = probs.tolist()  # Convert the numpy array to a Python list
        probs = [[round(p, 6) for p in prob] for prob in probs]  # Round each probability to 6 decimal places
        image_name = os.path.basename(image_files[i])
        print("Label probs:", image_name, probs)

# text that we use to describe each images
# text = clip.tokenize(["an airplane with a clear sky", "many books on a book shelf", "buildings with clear sky", "a black car", "a yellow fish underwater", 
# "food on a table", "bright orange frog", "a panda", "many people in one location", "person texting on a phone"]).to(device)