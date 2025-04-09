## 1. **自动化重命名文件**
# 有时需要批量重命名文件，可以使用 Python 脚本来自动化此过程。

import os

directory="./"

for filename in os.listdir(directory):
    if filename.endswith("md") or filename.endswith("txt"):
        new_name="prefix_"+filename
        # os.rename(os.path.join(directory,filename) ,os.path.join(directory,new_name))
        print(f"重命名：{filename}->{new_name}")

