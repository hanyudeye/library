1. 添加到右键菜单

按 Win + R，输入 regedit，打开注册表编辑器。
找到以下路径：
HKEY_CLASSES_ROOT\Directory\Background\shell\
右击 shell，选择 新建 -> 项，命名为 Open with Cursor（这是你在右键菜单中看到的选项名称）。
在刚刚创建的 Open with Cursor 项下，右击 新建 -> 项，命名为 command。

选择 command 项，在右侧窗口中双击 默认 键值，将其值设置为批处理文件的路径。例如：
C:\path\to\exefile "%V"
注意：%V 是当前文件夹路径的占位符。