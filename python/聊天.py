import random
import time

class ChatBot:
    def __init__(self):
        self.responses = {
            "你好": ["你好!", "你好啊!", "很高兴见到你!"],
            "再见": ["再见!", "下次见!", "期待下次聊天!"],
            "天气": ["今天天气不错呢!", "是个出门的好日子!", "记得带伞哦!"],
            "名字": ["我叫小智，是你的AI助手!", "你可以叫我小智!", "我是小智~"],
            "心情": ["我今天心情不错!", "和你聊天让我很开心!", "希望你也开心!"],
            "吃饭": ["吃饭对身体很重要哦!", "记得按时吃饭!", "想吃什么好吃的呢?"],
        }
        
        self.default_responses = [
            "抱歉,我不太明白...",
            "这个问题有点难,换个话题吧!",
            "让我想想怎么回答...",
            "你说得很有趣呢!",
        ]

    def format_response(self, text):
        """格式化输出的文本"""
        return f"\n🤖 AI助手: {text}\n"

    def format_user_input(self, text):
        """格式化用户输入的文本"""
        return f"\n👤 你: {text}\n"

    def get_response(self, user_input):
        """获取回复内容"""
        # 模拟思考时间
        time.sleep(0.5)
        
        # 检查是否匹配预设问答
        for key in self.responses:
            if key in user_input:
                return random.choice(self.responses[key])
        
        # 如果没有匹配的回答,返回默认回复
        return random.choice(self.default_responses)

    def start_chat(self):
        """开始聊天"""
        print("\n" + "="*50)
        print("欢迎使用AI聊天助手! 输入'退出'结束对话。")
        print("="*50 + "\n")

        while True:
            # 获取用户输入
            user_input = input("请输入: ").strip()
            
            # 打印格式化的用户输入
            print(self.format_user_input(user_input))
            
            # 检查是否退出
            if user_input in ['退出', '再见']:
                print(self.format_response("再见!期待下次聊天~"))
                break
            
            # 获取并打印回复
            response = self.get_response(user_input)
            print(self.format_response(response))

def main():
    chatbot = ChatBot()
    chatbot.start_chat()

if __name__ == "__main__":
    main()
