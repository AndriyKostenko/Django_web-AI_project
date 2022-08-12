import os
import cv2
import tensorflow as tf
from django.core.exceptions import ObjectDoesNotExist



from persik.models import Photo


def recognize_cat():
    # CATEGORIES = ["Probably not a Cat 😊", "Probably that's a Cat 😊"]
    CATEGORIES = ["0", "1"]
    model_path = os.path.abspath("persik/cat_&_others.model")

    try:
        last_photo = Photo.objects.latest('id')
        photo_path = last_photo.file.path

        IMG_SIZE = 50
        img_array = cv2.imread(photo_path, cv2.IMREAD_GRAYSCALE)
        new_array = cv2.resize(img_array, (IMG_SIZE, IMG_SIZE))

        model = tf.keras.models.load_model(model_path)
        prediction = model.predict([new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)])
        result = str(CATEGORIES[int(prediction[0][0])])
    except (ObjectDoesNotExist, cv2.error):
        return None
    return result
