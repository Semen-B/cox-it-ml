import torch
from torchvision import models
from torchvision import transforms
from src.utils.utilities import *
import os

SAVE_LOCATION = os.getcwd() + "/resources/"


def torch_preprocess(img):
    try:
        transform = transforms.Compose([
            transforms.Resize(256),
            transforms.CenterCrop(224),
            transforms.ToTensor(),
            transforms.Normalize(
                mean=[0.485, 0.456, 0.406],
                std=[0.229, 0.224, 0.225]
            )])
        input_tensor = transform(img)
        input_batch = torch.unsqueeze(input_tensor, 0)
        return input_batch
    except Exception as e:
        print(e)


model = None


def get_model():
    global model
    if model is None:
        model = models.alexnet(pretrained=True)
    return model


def get_labels():
    if not os.path.exists(SAVE_LOCATION + 'imagenet_classes.txt'):
        dir_check(SAVE_LOCATION)
        print("downloading imgnet classes in: ", SAVE_LOCATION)
        url = "https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt"
        r = requests.get(url, allow_redirects=True)
        open(SAVE_LOCATION + 'imagenet_classes.txt', 'wb').write(r.content)
    with open(SAVE_LOCATION + 'imagenet_classes.txt') as f:
        labels = [line.strip() for line in f.readlines()]
    return labels


def torch_predict(input_batch, model=None):
    if model is None:
        model = get_model()
    model.eval()
    with torch.no_grad():
        output = model(input_batch)

    labels = get_labels()
    _, index = torch.max(output, 1)

    percentage = torch.nn.functional.softmax(output, dim=1)[0] * 100
    # print(labels[index[0]], percentage[index[0]].item())

    _, indices = torch.sort(output, descending=True)
    return [(labels[idx], percentage[idx].item()) for idx in indices[0][:5]]


def torch_run_classifier(image: str):
    img = load_image(image)  # loading image
    if img is None:
        return None
    input_batch = torch_preprocess(img)  # preprocessing image
    top_labels = torch_predict(input_batch, model=None)  # prediction
    return top_labels[0]
