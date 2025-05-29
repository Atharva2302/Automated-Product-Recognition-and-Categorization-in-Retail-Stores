import tensorflow as tf

def load_main_category_model_scratch():
    return tf.keras.models.load_model('/content/drive/MyDrive/Product_Recognition_Categorisation/Models/main_category_model.h5')

def load_fruits_subcategory_model_scratch():
    return tf.keras.models.load_model('/content/drive/MyDrive/Product_Recognition_Categorisation/Models/fruits_subcategory_model.h5')

def load_vegetables_subcategory_model_scratch():
    return tf.keras.models.load_model('/content/drive/MyDrive/Product_Recognition_Categorisation/Models/vegetables_subcategory_model.h5')

def load_packages_subcategory_model_scratch():
    return tf.keras.models.load_model('/content/drive/MyDrive/Product_Recognition_Categorisation/Models/packages_subcategory_model.h5')

def load_main_category_model_vgg16():
    return tf.keras.models.load_model('/content/drive/MyDrive/Product_Recognition_Categorisation/Models/main_category_scratch.h5')

def load_fruits_subcategory_model_vgg16():
    return tf.keras.models.load_model('/content/drive/MyDrive/Product_Recognition_Categorisation/Models/fruits_subcategory_scratch.h5')

def load_vegetables_subcategory_model_vgg16():
    return tf.keras.models.load_model('/content/drive/MyDrive/Product_Recognition_Categorisation/Models/Vegetables_subcategory_scratch.h5')

def load_packages_subcategory_model_vgg16():
    return tf.keras.models.load_model('/content/drive/MyDrive/Product_Recognition_Categorisation/Models/Packages_subcategory_scratch.h5')