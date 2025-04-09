import tensorflow as tf
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np
import os

def is_duck(image_path):
    """
    判断传入的图片是否是鸭子
    :param image_path: 图片路径
    :return: True 如果是鸭子，否则 False
    """
    # 加载预训练的 MobileNetV2 模型
    model = MobileNetV2(weights='imagenet')

    # 加载图片并调整大小为模型输入所需的尺寸
    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    # 使用模型预测
    predictions = model.predict(img_array)
    decoded_predictions = decode_predictions(predictions, top=3)[0]

    # 打印预测结果
    for _, label, confidence in decoded_predictions:
        print(f"预测类别: {label}, 置信度: {confidence:.2f}")

    # 检查预测结果中是否包含鸭子
    for _, label, confidence in decoded_predictions:
        if 'duck' in label.lower():
            return True
    return False

# 测试程序
if __name__ == "__main__":
    image_path = "pic/4.png"  # 替换为你的图片路径
    # print(os.getcwd())
    if is_duck(image_path):
        print("这是一只鸭子!")
    else:
        print("这不是鸭子!")