import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input
from tensorflow.keras.applications.mobilenet_v2 import decode_predictions
from PIL import Image

# 加载 MobileNetV2 预训练模型
model = MobileNetV2(weights='imagenet')

def is_duck(image_path):
    # 加载图像并调整大小为 224x224
    img = Image.open(image_path)
    img = img.resize((224, 224))
    
    # 转换为 numpy 数组，并扩展维度以适应模型输入
    img_array = np.array(img)
    img_array = np.expand_dims(img_array, axis=0)
    
    # 预处理图像（适用于 MobileNetV2）
    img_array = preprocess_input(img_array)
    
    # 使用模型进行预测
    predictions = model.predict(img_array)
    
    # 解码预测结果，返回图片最可能的标签
    decoded_predictions = decode_predictions(predictions, top=3)[0]
    
    # 打印预测结果
    for i, (imagenet_id, label, score) in enumerate(decoded_predictions):
        print(f"{i+1}: {label} ({score:.2f})")
    
    # 判断是否包含 "duck" 类别
    for _, label, _ in decoded_predictions:
        if 'duck' in label.lower():  # 判断是否是鸭子
            return True
    return False

# 测试代码
image_path = 'pic/1.png'  # 替换成你自己图片的路径
if is_duck(image_path):
    print("This is a duck!")
else:
    print("This is not a duck.")
