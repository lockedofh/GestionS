# Form implementation generated from reading ui file 'edit_vendor.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_EditVendor(object):
    def setupUi(self, EditVendor):
        EditVendor.setObjectName("EditVendor")
        EditVendor.resize(411, 472)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(EditVendor)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelTitle = QtWidgets.QLabel(parent=EditVendor)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelTitle.sizePolicy().hasHeightForWidth())
        self.labelTitle.setSizePolicy(sizePolicy)
        self.labelTitle.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.labelTitle.setFont(font)
        self.labelTitle.setObjectName("labelTitle")
        self.verticalLayout.addWidget(self.labelTitle)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.labelNIF = QtWidgets.QLabel(parent=EditVendor)
        self.labelNIF.setObjectName("labelNIF")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelNIF)
        self.inputNIF = QtWidgets.QLineEdit(parent=EditVendor)
        self.inputNIF.setObjectName("inputNIF")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.inputNIF)
        self.labelName = QtWidgets.QLabel(parent=EditVendor)
        self.labelName.setObjectName("labelName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelName)
        self.inputName = QtWidgets.QLineEdit(parent=EditVendor)
        self.inputName.setObjectName("inputName")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.inputName)
        self.labelAddress = QtWidgets.QLabel(parent=EditVendor)
        self.labelAddress.setObjectName("labelAddress")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelAddress)
        self.inputAddress = QtWidgets.QLineEdit(parent=EditVendor)
        self.inputAddress.setObjectName("inputAddress")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.inputAddress)
        self.labelPhone = QtWidgets.QLabel(parent=EditVendor)
        self.labelPhone.setObjectName("labelPhone")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.labelPhone)
        self.inputPhone = QtWidgets.QLineEdit(parent=EditVendor)
        self.inputPhone.setObjectName("inputPhone")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.inputPhone)
        self.verticalLayout.addLayout(self.formLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.buttonBack = QtWidgets.QPushButton(parent=EditVendor)
        self.buttonBack.setObjectName("buttonBack")
        self.horizontalLayout.addWidget(self.buttonBack)
        self.buttonOK = QtWidgets.QPushButton(parent=EditVendor)
        self.buttonOK.setDefault(True)
        self.buttonOK.setObjectName("buttonOK")
        self.horizontalLayout.addWidget(self.buttonOK)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(EditVendor)
        QtCore.QMetaObject.connectSlotsByName(EditVendor)

    def retranslateUi(self, EditVendor):
        _translate = QtCore.QCoreApplication.translate
        EditVendor.setWindowTitle(_translate("EditVendor", "Edita proveïdor"))
        self.labelTitle.setWhatsThis(_translate("EditVendor", "<html><head/><body><p><span style=\" font-size:18pt; font-weight:700;\">Nou proveïdor</span></p></body></html>"))
        self.labelTitle.setText(_translate("EditVendor", "Edita proveïdor"))
        self.labelNIF.setText(_translate("EditVendor", "NIF"))
        self.labelName.setText(_translate("EditVendor", "Nom"))
        self.labelAddress.setText(_translate("EditVendor", "Direcció"))
        self.labelPhone.setText(_translate("EditVendor", "Telèfon"))
        self.buttonBack.setText(_translate("EditVendor", "Cancela"))
        self.buttonOK.setText(_translate("EditVendor", "Guarda"))
