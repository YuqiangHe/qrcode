# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 14:36:56 2019

@author: Administrator
"""

from PyQt5 import QtCore, QtWidgets
  
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
     def _fromUtf8(s):
         return s
 
try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
         return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
     def _translate(context, text, disambig):
         return QtWidgets.QApplication.translate(context, text, disambig)
 
class Ui_qrcode(object):
     def setupUi(self, qrcode):
         qrcode.setObjectName(_fromUtf8("qrcode"))
         qrcode.setEnabled(True)
         qrcode.resize(515, 424)
         self.groupBoxshow = QtWidgets.QGroupBox(qrcode)
         self.groupBoxshow.setGeometry(QtCore.QRect(50, 120, 431, 281))
         sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
         sizePolicy.setHorizontalStretch(0)
         sizePolicy.setVerticalStretch(0)
         sizePolicy.setHeightForWidth(self.groupBoxshow.sizePolicy().hasHeightForWidth())
         self.groupBoxshow.setSizePolicy(sizePolicy)
         self.groupBoxshow.setMinimumSize(QtCore.QSize(0, 0))
         self.groupBoxshow.setAutoFillBackground(True)
         self.groupBoxshow.setCheckable(False)
         self.groupBoxshow.setObjectName(_fromUtf8("groupBoxshow"))
         self.label = QtWidgets.QLabel(self.groupBoxshow)
         self.label.setGeometry(QtCore.QRect(10, 20, 401, 241))
         self.label.setText(_fromUtf8(""))
         self.label.setObjectName(_fromUtf8("label"))
         self.groupBox = QtWidgets.QGroupBox(qrcode)
         self.groupBox.setGeometry(QtCore.QRect(50, 20, 431, 91))
         self.groupBox.setObjectName(_fromUtf8("groupBox"))
         self.horizontalLayoutWidget = QtWidgets.QWidget(self.groupBox)
         self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 401, 80))
         self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
         self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
         self.horizontalLayout.setMargin(0)
         self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
         self.label_url = QtWidgets.QLabel(self.horizontalLayoutWidget)
         self.label_url.setObjectName(_fromUtf8("label_url"))
         self.horizontalLayout.addWidget(self.label_url)
         self.lineEditInput = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
         self.lineEditInput.setObjectName(_fromUtf8("lineEditInput"))
         self.horizontalLayout.addWidget(self.lineEditInput)
         self.pushButtonOk = QtWidgets.QPushButton(self.horizontalLayoutWidget)
         self.pushButtonOk.setObjectName(_fromUtf8("pushButtonOk"))
         self.horizontalLayout.addWidget(self.pushButtonOk)
 
         self.retranslateUi(qrcode)
         QtCore.QMetaObject.connectSlotsByName(qrcode)
 
     def retranslateUi(self, qrcode):
         qrcode.setWindowTitle(_translate("qrcode", "Pyqt Qrcode", None))
         self.groupBoxshow.setTitle(_translate("qrcode", "二维码显示", None))
         self.groupBox.setTitle(_translate("qrcode", "填写二维码内容", None))
         self.label_url.setText(_translate("qrcode", "URL地址：", None))
         self.pushButtonOk.setText(_translate("qrcode", "生成二维码", None))
 
 
import qrcode
class showQr(QtWidgets.QMainWindow):
     def __init__(self):
         super(showQr, self).__init__()
         self.ui_qr = Ui_qrcode()
         self.ui_qr.setupUi(self)
        # PyQT禁止窗口最大化按钮：
         self.setWindowFlags(QtCore.Qt.WindowMinimizeButtonHint)
         # PyQT禁止调整窗口大小:
         self.setFixedSize(self.width(), self.height())
 
         # 触发信号槽
         QtWidgets.QWidget.connect(self.ui_qr.pushButtonOk, QtCore.SIGNAL('clicked()'), self.generateQr) 
         # self.ui_qr.pushButtonOk.clicked.connect(self.generateQr)
 
     def generateQr(self):
         textcontent=self.ui_qr.lineEditInput.text()
         if textcontent=='':
             QtWidgets.QMessageBox.information(self, (u'提示'),(u'请填写URL地址'),QtWidgets.QMessageBox.Yes)
         else:
             filename='Qrcode.png'
             qr = qrcode.QRCode(
                 version=None,
                 error_correction=qrcode.constants.ERROR_CORRECT_L,
                 box_size=5,
                 border=4,
             )
             qr.add_data(textcontent)
             qr.make(fit=True)
             img = qr.make_image()
             img.save(filename)
             # img = qrcode.make(textcontent)
             # img.save(filename)
             self.ui_qr.label.setPixmap(QtWidgets.QPixmap(filename))
 
 
 
      # 重载keyPressEvent ，  当按下Esc退出
     def keyPressEvent(self, event):
         if event.key() ==QtCore.Qt.Key_Escape:
             self.close()
             
if __name__ == "__main__":
     import sys
     app = QtWidgets.QApplication(sys.argv)
     qr = showQr()
     qr.show()
     sys.exit(app.exec_())