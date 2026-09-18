from transformers import pipeline


classifier = pipeline(
    "image-classification",
    model="google/vit-base-patch16-224"
)


def classify_image(image):
    results = classifier(image)
    return results