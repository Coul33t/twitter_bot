# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!

# TODO: add an " edit sentence " button

from PyQt5 import QtCore, QtGui, QtWidgets

from gui_funcs import *

class Ui_Dialog(object):
    def __init__(self):
        self.tweeter_bot = TwitterBot()
        self.must_re_gather = False

    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(790, 310)
        self.at_label = QtWidgets.QLabel(Dialog)
        self.at_label.setGeometry(QtCore.QRect(10, 10, 16, 16))
        self.at_label.setObjectName("at_label")
        self.at_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.at_lineEdit.setGeometry(QtCore.QRect(30, 10, 113, 20))
        self.at_lineEdit.setObjectName("at_lineEdit")
        self.nb_pages_spinBox = QtWidgets.QSpinBox(Dialog)
        self.nb_pages_spinBox.setGeometry(QtCore.QRect(100, 70, 42, 22))
        self.nb_pages_spinBox.setMinimum(1)
        self.nb_pages_spinBox.setObjectName("nb_pages_spinBox")
        self.nb_pages_label = QtWidgets.QLabel(Dialog)
        self.nb_pages_label.setGeometry(QtCore.QRect(10, 70, 91, 16))
        self.nb_pages_label.setObjectName("nb_pages_label")
        self.replies_checkBox = QtWidgets.QCheckBox(Dialog)
        self.replies_checkBox.setGeometry(QtCore.QRect(50, 40, 91, 17))
        self.replies_checkBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.replies_checkBox.setChecked(False)
        self.replies_checkBox.setObjectName("replies_checkBox")
        self.markov_label = QtWidgets.QLabel(Dialog)
        self.markov_label.setGeometry(QtCore.QRect(10, 100, 47, 13))
        self.markov_label.setObjectName("markov_label")
        self.markov_spinBox = QtWidgets.QSpinBox(Dialog)
        self.markov_spinBox.setGeometry(QtCore.QRect(100, 100, 42, 22))
        self.markov_spinBox.setMinimum(1)
        self.markov_spinBox.setObjectName("markov_spinBox")
        self.output_checkBox = QtWidgets.QCheckBox(Dialog)
        self.output_checkBox.setGeometry(QtCore.QRect(49, 180, 91, 20))
        self.output_checkBox.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.output_checkBox.setObjectName("output_checkBox")
        self.output_filename_label = QtWidgets.QLabel(Dialog)
        self.output_filename_label.setGeometry(QtCore.QRect(10, 210, 131, 16))
        self.output_filename_label.setObjectName("output_filename_label")
        self.output_filename_lineEdit = QtWidgets.QLineEdit(Dialog)
        self.output_filename_lineEdit.setGeometry(QtCore.QRect(10, 230, 113, 20))
        self.output_filename_lineEdit.setObjectName("output_filename_lineEdit")
        self.output_extension_label = QtWidgets.QLabel(Dialog)
        self.output_extension_label.setGeometry(QtCore.QRect(130, 230, 47, 13))
        self.output_extension_label.setObjectName("output_extension_label")
        self.final_sentences_listView = QtWidgets.QListView(Dialog)
        self.final_sentences_listView.setGeometry(QtCore.QRect(170, 10, 611, 291))
        self.final_sentences_listView.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.final_sentences_listView.setProperty("isWrapping", True)
        self.final_sentences_listView.setResizeMode(QtWidgets.QListView.Adjust)
        self.final_sentences_listView.setWordWrap(True)
        self.final_sentences_listView.setObjectName("final_sentences_listView")
        self.nb_sentences_spinBox = QtWidgets.QSpinBox(Dialog)
        self.nb_sentences_spinBox.setGeometry(QtCore.QRect(100, 130, 42, 22))
        self.nb_sentences_spinBox.setMinimum(1)
        self.nb_sentences_spinBox.setObjectName("nb_sentences_spinBox")
        self.nb_sentences_label = QtWidgets.QLabel(Dialog)
        self.nb_sentences_label.setGeometry(QtCore.QRect(10, 120, 71, 41))
        self.nb_sentences_label.setWordWrap(True)
        self.nb_sentences_label.setObjectName("nb_sentences_label")
        self.tweet_pushButton = QtWidgets.QPushButton(Dialog)
        self.tweet_pushButton.setGeometry(QtCore.QRect(90, 270, 75, 23))
        self.tweet_pushButton.setObjectName("tweet_pushButton")
        self.generate_pushButton = QtWidgets.QPushButton(Dialog)
        self.generate_pushButton.setGeometry(QtCore.QRect(10, 270, 75, 23))
        self.generate_pushButton.setObjectName("generate_pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        self.initialise()
        self.link()

    def initialise(self):
        self.model_listView_final_sentences = QtGui.QStandardItemModel(self.final_sentences_listView)
        self.final_sentences_listView.setModel(self.model_listView_final_sentences)
        self.tweeter_bot.pages_to_retrieve = self.nb_pages_spinBox.value()
        self.tweeter_bot.forward_words = self.markov_spinBox.value()
        self.tweeter_bot.nb_tweets_to_generate = self.nb_sentences_spinBox.value()

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.at_label.setText(_translate("Dialog", "@"))
        self.nb_pages_label.setText(_translate("Dialog", "Number of pages"))
        self.replies_checkBox.setText(_translate("Dialog", "Ignore replies"))
        self.markov_label.setText(_translate("Dialog", "Markov"))
        self.output_checkBox.setText(_translate("Dialog", "To output file"))
        self.output_filename_label.setText(_translate("Dialog", "Output file name"))
        self.output_extension_label.setText(_translate("Dialog", ".txt"))
        self.nb_sentences_label.setText(_translate("Dialog", "Number of sentences to generate"))
        self.tweet_pushButton.setText(_translate("Dialog", "Tweet"))
        self.generate_pushButton.setText(_translate("Dialog", "Generate"))

    def link(self):
        self.nb_pages_spinBox.valueChanged.connect(self.change_number_of_pages)
        self.markov_spinBox.valueChanged.connect(self.change_markov_value)
        self.nb_sentences_spinBox.valueChanged.connect(self.change_nb_sentences_to_generate)
        self.replies_checkBox.stateChanged.connect(self.set_ignore_replies)
        self.output_checkBox.stateChanged.connect(self.set_output_file)
        self.generate_pushButton.clicked.connect(self.generate)
        self.tweet_pushButton.clicked.connect(self.tweet)

    def change_number_of_pages(self):
        self.tweeter_bot.pages_to_retrieve = self.nb_pages_spinBox.value()
        self.must_re_gather = True

    def change_markov_value(self):
        self.tweeter_bot.forward_words = self.markov_spinBox.value()

    def change_nb_sentences_to_generate(self):
        self.tweeter_bot.nb_tweets_to_generate = self.nb_sentences_spinBox.value()

    def set_ignore_replies(self):
        self.tweeter_bot.no_answers = self.replies_checkBox.isChecked()
        self.must_re_gather = True

    def set_output_file(self):
        self.tweeter_bot.output_to_file = self.output_checkBox.isChecked()

    def generate(self):
        # TODO: add window to tell what's happening
        self.tweeter_bot.initialise()

        if self.tweeter_bot.name != self.at_lineEdit.text():
            self.tweeter_bot.name = self.at_lineEdit.text()
            self.must_re_gather = True

        if self.must_re_gather:
            self.must_re_gather = False
            self.tweeter_bot.gather_tweets()

        self.tweeter_bot.create_new_sentences()

        self.model_listView_final_sentences.clear()

        for i in range(self.tweeter_bot.nb_tweets_to_generate):
            item = QtGui.QStandardItem(self.tweeter_bot.generated_tweets[i][0])
            self.model_listView_final_sentences.appendRow(item)

    def tweet(self):
        pass

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())