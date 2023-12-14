import openai
import sys
from window_script import Window,bolb
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore
import threading
from PyQt5.QtCore import pyqtSignal


class GPT(Window):
    signal = pyqtSignal(object)
    def __init__(self):
        super().__init__()
        self.returnText = None
        self.message = None
        self.returnFlag=True
        self.signal.connect(self.show_dialog)
        # 接口
        self.apikey= "sk-dn8q1bmjrhaQVkrw1583Db7f6aF648Ac8994Ea297c3bBfCe"
        self.url="https://one.apifaucet.com/v1/"
        openai.api_key = self.apikey
        openai.base_url = self.url
        self.page_init()
        self.message = [{"role": "system", "content": "你好！"}]
    def page_init(self):
        self.apibox.setText(self.apikey)
        self.baserurlbox.setText(self.url)


    def apply_api(self):
        self.apikey=self.apibox.text()
        self.url=self.baserurlbox.text()
        openai.api_key = self.apikey
        openai.base_url = self.url
    def show_dialog(self):#展示最新的一条
        for item in self.message[-1:]:
            if item["role"] == "system":
                bolb.chat_generate(self,item["content"],"GPT","left")
            elif item["role"] == "user":
                bolb.chat_generate(self,item["content"],"user","right")
            QApplication.processEvents()

    def message_add(self, returnMessage):
        self.message.append({"role": "system", "content": "%s" % returnMessage})

    def post(self):
        if self.returnFlag==True:
            self.returnFlag = False
            inputs = self.textEdit.toPlainText()
            self.textEdit.setText("")
            self.message.append({"role": "user", "content": "%s" % inputs})
            self.show_dialog()
            t=threading.Thread(target=self.req,name="s")
            t.start()

    def clean_message_list(self):
        if self.returnFlag == True :
            self.message = [{"role": "system", "content": "你好！"}]
            self.clear_scroll_bar()
            self.show_dialog()

    def clear_scroll_bar(self):
        for i in range(self.verticalLayout_2.count()):
            self.verticalLayout_2.itemAt(i).widget().deleteLater()

    def req(self):
            completion = openai.chat.completions.create(model="gpt-3.5-turbo", messages=self.message)
            if completion.choices:
                self.returnText = completion.choices[0].message.content
                self.message_add(completion.choices[0].message.content)
                self.signal.emit("")
                self.returnFlag = True
            else:
                self.returnText = None
                print("error")
                self.returnFlag = True
def main():
    app = QApplication(sys.argv)
    mywindow = GPT()
    mywindow.show_dialog()
    mywindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

    a = GPT()
    a.run_gpt()
