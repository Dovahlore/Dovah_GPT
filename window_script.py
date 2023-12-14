from PyQt5.QtWidgets import QMainWindow,QFileDialog
from PyQt5 import QtWidgets,QtCore,QtGui
from window import Ui_MainWindow

class Window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.setupUi(self) # 渲染页面控件
        self.connect_signals() # 设置信号槽

    def connect_signals(self):
        self.pushButton.clicked.connect(self.post) # 绑定确定按钮事件
        self.pushButton_2.clicked.connect(self.clean_message_list)
        self.apply.clicked.connect(self.apply_api)
        self.toolButton.clicked.connect(self.bg_choose)
    def bg_choose(self):
        file=QFileDialog.getOpenFileName(self,filter="Images (*.png *.xpm *.jpg)")   # 设置文件扩展名过滤,用双分号间隔
        print(file)

        self.centralwidget.setStyleSheet("#centralwidget {background-image: url(%s);}"%file[0])





class bolb():
        def chat_generate(self,text,who,dir):
            self.message_3 = QtWidgets.QFrame(self.scrollAreaWidgetContents)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.message_3.sizePolicy().hasHeightForWidth())
            self.message_3.setSizePolicy(sizePolicy)
            self.message_3.setMinimumSize(QtCore.QSize(0, 0))
            if dir=="left":
                self.message_3.setLayoutDirection(QtCore.Qt.LeftToRight)
            elif dir=="right":
                self.message_3.setLayoutDirection(QtCore.Qt.RightToLeft)
            self.message_3.setAutoFillBackground(False)
            self.message_3.setFrameShape(QtWidgets.QFrame.NoFrame)
            self.message_3.setFrameShadow(QtWidgets.QFrame.Plain)
            self.message_3.setLineWidth(0)
            self.message_3.setObjectName("message_3")
            self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.message_3)
            self.horizontalLayout_6.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
            self.horizontalLayout_6.setContentsMargins(9, 9, 9, 0)
            self.horizontalLayout_6.setObjectName("horizontalLayout_6")
            self.groupBox_5 = QtWidgets.QGroupBox(self.message_3)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.groupBox_5.sizePolicy().hasHeightForWidth())
            self.groupBox_5.setSizePolicy(sizePolicy)
            self.groupBox_5.setMinimumSize(QtCore.QSize(80, 100))
            self.groupBox_5.setTitle("")
            self.groupBox_5.setObjectName("groupBox_5")
            self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.groupBox_5)
            self.verticalLayout_7.setObjectName("verticalLayout_7")
            self.pic_5 = QtWidgets.QLabel(self.groupBox_5)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.pic_5.sizePolicy().hasHeightForWidth())
            self.pic_5.setSizePolicy(sizePolicy)
            self.pic_5.setText("")
            self.pic_5.setMinimumSize(QtCore.QSize(60, 60))
            self.pic_5.setMaximumSize(QtCore.QSize(60, 60))
            self.pic_5.setScaledContents(True)
            if dir == "left":
                self.pic_5.setPixmap(QtGui.QPixmap(":/chat/chat.png"))
            elif dir =="right":
                self.pic_5.setPixmap(QtGui.QPixmap(":/chat/user.png"))

            self.pic_5.setObjectName("pic_5")
            self.verticalLayout_7.addWidget(self.pic_5, 0, QtCore.Qt.AlignHCenter)
            self.system_5 = QtWidgets.QLabel(self.groupBox_5)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.system_5.sizePolicy().hasHeightForWidth())
            self.system_5.setSizePolicy(sizePolicy)
            self.system_5.setObjectName("system_5")
            self.verticalLayout_7.addWidget(self.system_5, 0, QtCore.Qt.AlignHCenter | QtCore.Qt.AlignVCenter)
            self.horizontalLayout_6.addWidget(self.groupBox_5, 0, QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
            self.label_5 = QtWidgets.QLabel(self.message_3)
            sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
            sizePolicy.setHorizontalStretch(0)
            sizePolicy.setVerticalStretch(0)
            sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
            self.label_5.setSizePolicy(sizePolicy)
            self.label_5.setAutoFillBackground(False)
            if dir == "left":

                self.label_5.setStyleSheet(
                "color: rgb(0, 0, 0);font: 14pt \"黑体\";background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:0.54, y2:1, stop:0.25 rgba(93, 224, 255, 255), stop:1 rgba(152, 255, 255, 255));border-radius: 10px; border: 2px groove gray;")
            elif dir=="right":
                self.label_5.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(198, 64, 255, 255), stop:1 rgba(197, 175, 255, 255));color: rgb(255, 255, 255);font: 14pt \"华文宋体\";border-radius: 10px; border: 2px groove gray;")

            self.label_5.setScaledContents(True)
            self.label_5.setAlignment(QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
            self.label_5.setWordWrap(True)
            self.label_5.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
            self.label_5.setObjectName("label_5")
            self.horizontalLayout_6.addWidget(self.label_5, 0, QtCore.Qt.AlignTop)
            spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
            self.horizontalLayout_6.addItem(spacerItem1)
            self.horizontalLayout_6.setStretch(1, 100)
            self.horizontalLayout_6.setStretch(2, 30)
            self.verticalLayout_2.addWidget(self.message_3)
            _translate = QtCore.QCoreApplication.translate
            self.system_5.setText(_translate("MainWindow", who))
            self.label_5.setText(_translate("MainWindow", text))
            self.label_5.setTextFormat(QtCore.Qt.TextFormat.MarkdownText)
            print(text)