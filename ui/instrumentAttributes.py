# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'instrumentAttributes.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_InstrumentAttributesDialog(object):
    def setupUi(self, InstrumentAttributesDialog):
        InstrumentAttributesDialog.setObjectName("InstrumentAttributesDialog")
        InstrumentAttributesDialog.resize(526, 416)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(InstrumentAttributesDialog.sizePolicy().hasHeightForWidth())
        InstrumentAttributesDialog.setSizePolicy(sizePolicy)
        InstrumentAttributesDialog.setMinimumSize(QtCore.QSize(526, 400))
        InstrumentAttributesDialog.setMaximumSize(QtCore.QSize(1000, 600))
        self.gridLayout_3 = QtWidgets.QGridLayout(InstrumentAttributesDialog)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox = QtWidgets.QGroupBox(InstrumentAttributesDialog)
        self.groupBox.setStyleSheet("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.Chan3LabelEdit = QtWidgets.QLineEdit(self.groupBox)
        self.Chan3LabelEdit.setMinimumSize(QtCore.QSize(120, 22))
        self.Chan3LabelEdit.setMaximumSize(QtCore.QSize(160, 16777215))
        self.Chan3LabelEdit.setMaxLength(12)
        self.Chan3LabelEdit.setObjectName("Chan3LabelEdit")
        self.gridLayout.addWidget(self.Chan3LabelEdit, 6, 1, 1, 1)
        self.Chan0LabelEdit = QtWidgets.QLineEdit(self.groupBox)
        self.Chan0LabelEdit.setMinimumSize(QtCore.QSize(120, 22))
        self.Chan0LabelEdit.setMaximumSize(QtCore.QSize(160, 16777215))
        self.Chan0LabelEdit.setMaxLength(12)
        self.Chan0LabelEdit.setObjectName("Chan0LabelEdit")
        self.gridLayout.addWidget(self.Chan0LabelEdit, 3, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setMinimumSize(QtCore.QSize(0, 0))
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 3, 2, 1, 1)
        self.Chan0ColourLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.Chan0ColourLineEdit.setMinimumSize(QtCore.QSize(120, 22))
        self.Chan0ColourLineEdit.setMaximumSize(QtCore.QSize(120, 16777215))
        self.Chan0ColourLineEdit.setMaxLength(7)
        self.Chan0ColourLineEdit.setObjectName("Chan0ColourLineEdit")
        self.gridLayout.addWidget(self.Chan0ColourLineEdit, 3, 3, 1, 1)
        self.PickerButton0 = QtWidgets.QPushButton(self.groupBox)
        self.PickerButton0.setMinimumSize(QtCore.QSize(107, 22))
        self.PickerButton0.setMaximumSize(QtCore.QSize(100, 16777215))
        self.PickerButton0.setObjectName("PickerButton0")
        self.gridLayout.addWidget(self.PickerButton0, 3, 4, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setMinimumSize(QtCore.QSize(30, 0))
        self.label_5.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(self.groupBox)
        self.label_18.setMinimumSize(QtCore.QSize(0, 0))
        self.label_18.setObjectName("label_18")
        self.gridLayout.addWidget(self.label_18, 4, 2, 1, 1)
        self.Chan1ColourLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.Chan1ColourLineEdit.setMinimumSize(QtCore.QSize(120, 22))
        self.Chan1ColourLineEdit.setMaximumSize(QtCore.QSize(120, 16777215))
        self.Chan1ColourLineEdit.setMaxLength(7)
        self.Chan1ColourLineEdit.setObjectName("Chan1ColourLineEdit")
        self.gridLayout.addWidget(self.Chan1ColourLineEdit, 4, 3, 1, 1)
        self.Chan5LabelEdit = QtWidgets.QLineEdit(self.groupBox)
        self.Chan5LabelEdit.setMinimumSize(QtCore.QSize(120, 22))
        self.Chan5LabelEdit.setMaximumSize(QtCore.QSize(160, 16777215))
        self.Chan5LabelEdit.setMaxLength(12)
        self.Chan5LabelEdit.setObjectName("Chan5LabelEdit")
        self.gridLayout.addWidget(self.Chan5LabelEdit, 8, 1, 1, 1)
        self.PickerButton1 = QtWidgets.QPushButton(self.groupBox)
        self.PickerButton1.setMinimumSize(QtCore.QSize(107, 22))
        self.PickerButton1.setMaximumSize(QtCore.QSize(100, 16777215))
        self.PickerButton1.setObjectName("PickerButton1")
        self.gridLayout.addWidget(self.PickerButton1, 4, 4, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setMinimumSize(QtCore.QSize(30, 20))
        self.label_6.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 0, 1, 1)
        self.Chan2LabelEdit = QtWidgets.QLineEdit(self.groupBox)
        self.Chan2LabelEdit.setMinimumSize(QtCore.QSize(120, 22))
        self.Chan2LabelEdit.setMaximumSize(QtCore.QSize(160, 16777215))
        self.Chan2LabelEdit.setMaxLength(12)
        self.Chan2LabelEdit.setObjectName("Chan2LabelEdit")
        self.gridLayout.addWidget(self.Chan2LabelEdit, 5, 1, 1, 1)
        self.label_19 = QtWidgets.QLabel(self.groupBox)
        self.label_19.setMinimumSize(QtCore.QSize(0, 20))
        self.label_19.setObjectName("label_19")
        self.gridLayout.addWidget(self.label_19, 5, 2, 1, 1)
        self.Chan2ColourLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.Chan2ColourLineEdit.setMinimumSize(QtCore.QSize(120, 20))
        self.Chan2ColourLineEdit.setMaximumSize(QtCore.QSize(120, 16777215))
        self.Chan2ColourLineEdit.setMaxLength(7)
        self.Chan2ColourLineEdit.setObjectName("Chan2ColourLineEdit")
        self.gridLayout.addWidget(self.Chan2ColourLineEdit, 5, 3, 1, 1)
        self.PickerButton2 = QtWidgets.QPushButton(self.groupBox)
        self.PickerButton2.setMinimumSize(QtCore.QSize(107, 22))
        self.PickerButton2.setMaximumSize(QtCore.QSize(100, 16777215))
        self.PickerButton2.setObjectName("PickerButton2")
        self.gridLayout.addWidget(self.PickerButton2, 5, 4, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setMinimumSize(QtCore.QSize(30, 0))
        self.label_7.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 0, 1, 1)
        self.label_20 = QtWidgets.QLabel(self.groupBox)
        self.label_20.setObjectName("label_20")
        self.gridLayout.addWidget(self.label_20, 6, 2, 1, 1)
        self.Chan3ColourLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.Chan3ColourLineEdit.setMinimumSize(QtCore.QSize(120, 22))
        self.Chan3ColourLineEdit.setMaximumSize(QtCore.QSize(120, 16777215))
        self.Chan3ColourLineEdit.setMaxLength(7)
        self.Chan3ColourLineEdit.setObjectName("Chan3ColourLineEdit")
        self.gridLayout.addWidget(self.Chan3ColourLineEdit, 6, 3, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setObjectName("label_15")
        self.horizontalLayout.addWidget(self.label_15)
        self.StaribusPortLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.StaribusPortLineEdit.setMinimumSize(QtCore.QSize(0, 22))
        self.StaribusPortLineEdit.setObjectName("StaribusPortLineEdit")
        self.horizontalLayout.addWidget(self.StaribusPortLineEdit)
        self.RS485checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.RS485checkBox.setObjectName("RS485checkBox")
        self.horizontalLayout.addWidget(self.RS485checkBox)
        self.StaribusAutodetectCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.StaribusAutodetectCheckBox.setObjectName("StaribusAutodetectCheckBox")
        self.horizontalLayout.addWidget(self.StaribusAutodetectCheckBox)
        self.Staribus2StarinetCheckBox = QtWidgets.QCheckBox(self.groupBox)
        self.Staribus2StarinetCheckBox.setObjectName("Staribus2StarinetCheckBox")
        self.horizontalLayout.addWidget(self.Staribus2StarinetCheckBox)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 5)
        self.PickerButton3 = QtWidgets.QPushButton(self.groupBox)
        self.PickerButton3.setMinimumSize(QtCore.QSize(107, 22))
        self.PickerButton3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.PickerButton3.setObjectName("PickerButton3")
        self.gridLayout.addWidget(self.PickerButton3, 6, 4, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setMinimumSize(QtCore.QSize(30, 0))
        self.label_8.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 7, 0, 1, 1)
        self.Chan4LabelEdit = QtWidgets.QLineEdit(self.groupBox)
        self.Chan4LabelEdit.setMinimumSize(QtCore.QSize(120, 22))
        self.Chan4LabelEdit.setMaximumSize(QtCore.QSize(160, 16777215))
        self.Chan4LabelEdit.setMaxLength(12)
        self.Chan4LabelEdit.setObjectName("Chan4LabelEdit")
        self.gridLayout.addWidget(self.Chan4LabelEdit, 7, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.groupBox)
        self.label_21.setObjectName("label_21")
        self.gridLayout.addWidget(self.label_21, 7, 2, 1, 1)
        self.Chan4ColourLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.Chan4ColourLineEdit.setMinimumSize(QtCore.QSize(120, 22))
        self.Chan4ColourLineEdit.setMaximumSize(QtCore.QSize(120, 16777215))
        self.Chan4ColourLineEdit.setMaxLength(7)
        self.Chan4ColourLineEdit.setObjectName("Chan4ColourLineEdit")
        self.gridLayout.addWidget(self.Chan4ColourLineEdit, 7, 3, 1, 1)
        self.PickerButton4 = QtWidgets.QPushButton(self.groupBox)
        self.PickerButton4.setMinimumSize(QtCore.QSize(107, 22))
        self.PickerButton4.setMaximumSize(QtCore.QSize(100, 16777215))
        self.PickerButton4.setObjectName("PickerButton4")
        self.gridLayout.addWidget(self.PickerButton4, 7, 4, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setMinimumSize(QtCore.QSize(30, 0))
        self.label_9.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 8, 0, 1, 1)
        self.label_22 = QtWidgets.QLabel(self.groupBox)
        self.label_22.setObjectName("label_22")
        self.gridLayout.addWidget(self.label_22, 8, 2, 1, 1)
        self.Chan5ColourLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.Chan5ColourLineEdit.setMinimumSize(QtCore.QSize(120, 22))
        self.Chan5ColourLineEdit.setMaximumSize(QtCore.QSize(120, 16777215))
        self.Chan5ColourLineEdit.setMaxLength(7)
        self.Chan5ColourLineEdit.setObjectName("Chan5ColourLineEdit")
        self.gridLayout.addWidget(self.Chan5ColourLineEdit, 8, 3, 1, 1)
        self.PickerButton5 = QtWidgets.QPushButton(self.groupBox)
        self.PickerButton5.setMinimumSize(QtCore.QSize(107, 22))
        self.PickerButton5.setMaximumSize(QtCore.QSize(100, 16777215))
        self.PickerButton5.setObjectName("PickerButton5")
        self.gridLayout.addWidget(self.PickerButton5, 8, 4, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setMinimumSize(QtCore.QSize(30, 0))
        self.label_10.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 9, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setMinimumSize(QtCore.QSize(102, 0))
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setMaxCount(253)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        self.label_16.setMinimumSize(QtCore.QSize(56, 0))
        self.label_16.setObjectName("label_16")
        self.horizontalLayout_2.addWidget(self.label_16)
        self.BaudrateCombobox = QtWidgets.QComboBox(self.groupBox)
        self.BaudrateCombobox.setObjectName("BaudrateCombobox")
        self.horizontalLayout_2.addWidget(self.BaudrateCombobox)
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setMinimumSize(QtCore.QSize(53, 0))
        self.label_17.setMaximumSize(QtCore.QSize(53, 16777215))
        self.label_17.setObjectName("label_17")
        self.horizontalLayout_2.addWidget(self.label_17)
        self.TimeoutCombobox = QtWidgets.QComboBox(self.groupBox)
        self.TimeoutCombobox.setObjectName("TimeoutCombobox")
        self.horizontalLayout_2.addWidget(self.TimeoutCombobox)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.StarinetAddressLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.StarinetAddressLineEdit.setMinimumSize(QtCore.QSize(129, 22))
        self.StarinetAddressLineEdit.setMaxLength(15)
        self.StarinetAddressLineEdit.setObjectName("StarinetAddressLineEdit")
        self.horizontalLayout_3.addWidget(self.StarinetAddressLineEdit)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.StarinetPortLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.StarinetPortLineEdit.setMinimumSize(QtCore.QSize(50, 22))
        self.StarinetPortLineEdit.setMaxLength(5)
        self.StarinetPortLineEdit.setObjectName("StarinetPortLineEdit")
        self.horizontalLayout_3.addWidget(self.StarinetPortLineEdit)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 5)
        self.Chan1LabelEdit = QtWidgets.QLineEdit(self.groupBox)
        self.Chan1LabelEdit.setMinimumSize(QtCore.QSize(120, 22))
        self.Chan1LabelEdit.setMaximumSize(QtCore.QSize(160, 16777215))
        self.Chan1LabelEdit.setMaxLength(12)
        self.Chan1LabelEdit.setObjectName("Chan1LabelEdit")
        self.gridLayout.addWidget(self.Chan1LabelEdit, 4, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setMinimumSize(QtCore.QSize(45, 0))
        self.label_4.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 0, 1, 1)
        self.Chan6LabelEdit = QtWidgets.QLineEdit(self.groupBox)
        self.Chan6LabelEdit.setMinimumSize(QtCore.QSize(120, 22))
        self.Chan6LabelEdit.setMaximumSize(QtCore.QSize(160, 16777215))
        self.Chan6LabelEdit.setMaxLength(12)
        self.Chan6LabelEdit.setObjectName("Chan6LabelEdit")
        self.gridLayout.addWidget(self.Chan6LabelEdit, 9, 1, 1, 1)
        self.label_23 = QtWidgets.QLabel(self.groupBox)
        self.label_23.setObjectName("label_23")
        self.gridLayout.addWidget(self.label_23, 9, 2, 1, 1)
        self.Chan6ColourLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.Chan6ColourLineEdit.setMinimumSize(QtCore.QSize(120, 22))
        self.Chan6ColourLineEdit.setMaximumSize(QtCore.QSize(120, 16777215))
        self.Chan6ColourLineEdit.setMaxLength(7)
        self.Chan6ColourLineEdit.setObjectName("Chan6ColourLineEdit")
        self.gridLayout.addWidget(self.Chan6ColourLineEdit, 9, 3, 1, 1)
        self.PickerButton6 = QtWidgets.QPushButton(self.groupBox)
        self.PickerButton6.setMinimumSize(QtCore.QSize(107, 22))
        self.PickerButton6.setMaximumSize(QtCore.QSize(100, 16777215))
        self.PickerButton6.setObjectName("PickerButton6")
        self.gridLayout.addWidget(self.PickerButton6, 9, 4, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setMinimumSize(QtCore.QSize(30, 0))
        self.label_11.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 10, 0, 1, 1)
        self.Chan7LabelEdit = QtWidgets.QLineEdit(self.groupBox)
        self.Chan7LabelEdit.setMinimumSize(QtCore.QSize(120, 22))
        self.Chan7LabelEdit.setMaximumSize(QtCore.QSize(160, 16777215))
        self.Chan7LabelEdit.setMaxLength(12)
        self.Chan7LabelEdit.setObjectName("Chan7LabelEdit")
        self.gridLayout.addWidget(self.Chan7LabelEdit, 10, 1, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.groupBox)
        self.label_24.setObjectName("label_24")
        self.gridLayout.addWidget(self.label_24, 10, 2, 1, 1)
        self.Chan7ColourLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.Chan7ColourLineEdit.setMinimumSize(QtCore.QSize(120, 22))
        self.Chan7ColourLineEdit.setMaximumSize(QtCore.QSize(120, 16777215))
        self.Chan7ColourLineEdit.setMaxLength(7)
        self.Chan7ColourLineEdit.setObjectName("Chan7ColourLineEdit")
        self.gridLayout.addWidget(self.Chan7ColourLineEdit, 10, 3, 1, 1)
        self.PickerButton7 = QtWidgets.QPushButton(self.groupBox)
        self.PickerButton7.setMinimumSize(QtCore.QSize(107, 22))
        self.PickerButton7.setMaximumSize(QtCore.QSize(100, 16777215))
        self.PickerButton7.setObjectName("PickerButton7")
        self.gridLayout.addWidget(self.PickerButton7, 10, 4, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setMinimumSize(QtCore.QSize(30, 0))
        self.label_12.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 11, 0, 1, 1)
        self.Chan8LabelEdit = QtWidgets.QLineEdit(self.groupBox)
        self.Chan8LabelEdit.setMinimumSize(QtCore.QSize(120, 22))
        self.Chan8LabelEdit.setMaximumSize(QtCore.QSize(160, 16777215))
        self.Chan8LabelEdit.setMaxLength(12)
        self.Chan8LabelEdit.setObjectName("Chan8LabelEdit")
        self.gridLayout.addWidget(self.Chan8LabelEdit, 11, 1, 1, 1)
        self.label_25 = QtWidgets.QLabel(self.groupBox)
        self.label_25.setObjectName("label_25")
        self.gridLayout.addWidget(self.label_25, 11, 2, 1, 1)
        self.Chan8ColourLineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.Chan8ColourLineEdit.setMinimumSize(QtCore.QSize(120, 22))
        self.Chan8ColourLineEdit.setMaximumSize(QtCore.QSize(120, 16777215))
        self.Chan8ColourLineEdit.setMaxLength(7)
        self.Chan8ColourLineEdit.setObjectName("Chan8ColourLineEdit")
        self.gridLayout.addWidget(self.Chan8ColourLineEdit, 11, 3, 1, 1)
        self.PickerButton8 = QtWidgets.QPushButton(self.groupBox)
        self.PickerButton8.setMinimumSize(QtCore.QSize(107, 22))
        self.PickerButton8.setMaximumSize(QtCore.QSize(100, 16777215))
        self.PickerButton8.setObjectName("PickerButton8")
        self.gridLayout.addWidget(self.PickerButton8, 11, 4, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(InstrumentAttributesDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok|QtWidgets.QDialogButtonBox.RestoreDefaults)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_3.addWidget(self.buttonBox, 1, 0, 1, 1)

        self.retranslateUi(InstrumentAttributesDialog)
        self.buttonBox.accepted.connect(InstrumentAttributesDialog.accept)
        self.buttonBox.rejected.connect(InstrumentAttributesDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(InstrumentAttributesDialog)

    def retranslateUi(self, InstrumentAttributesDialog):
        _translate = QtCore.QCoreApplication.translate
        InstrumentAttributesDialog.setWindowTitle(_translate("InstrumentAttributesDialog", "Instrument Attributes"))
        self.groupBox.setTitle(_translate("InstrumentAttributesDialog", "Instrument Attributes"))
        self.label_13.setText(_translate("InstrumentAttributesDialog", "Colour"))
        self.PickerButton0.setText(_translate("InstrumentAttributesDialog", "Colour Picker"))
        self.label_5.setText(_translate("InstrumentAttributesDialog", "Label 1"))
        self.label_18.setText(_translate("InstrumentAttributesDialog", "Colour"))
        self.PickerButton1.setText(_translate("InstrumentAttributesDialog", "Colour Picker"))
        self.label_6.setText(_translate("InstrumentAttributesDialog", "Label 2"))
        self.label_19.setText(_translate("InstrumentAttributesDialog", "Colour"))
        self.PickerButton2.setText(_translate("InstrumentAttributesDialog", "Colour Picker"))
        self.label_7.setText(_translate("InstrumentAttributesDialog", "Label 3"))
        self.label_20.setText(_translate("InstrumentAttributesDialog", "Colour"))
        self.label_15.setText(_translate("InstrumentAttributesDialog", "Staribus Port"))
        self.RS485checkBox.setText(_translate("InstrumentAttributesDialog", "RS485"))
        self.StaribusAutodetectCheckBox.setText(_translate("InstrumentAttributesDialog", "Autodetect"))
        self.Staribus2StarinetCheckBox.setText(_translate("InstrumentAttributesDialog", "Staribus2Starinet"))
        self.PickerButton3.setText(_translate("InstrumentAttributesDialog", "Colour Picker"))
        self.label_8.setText(_translate("InstrumentAttributesDialog", "Label 4"))
        self.label_21.setText(_translate("InstrumentAttributesDialog", "Colour"))
        self.PickerButton4.setText(_translate("InstrumentAttributesDialog", "Colour Picker"))
        self.label_9.setText(_translate("InstrumentAttributesDialog", "Label 5"))
        self.label_22.setText(_translate("InstrumentAttributesDialog", "Colour"))
        self.PickerButton5.setText(_translate("InstrumentAttributesDialog", "Colour Picker"))
        self.label_10.setText(_translate("InstrumentAttributesDialog", "Label 6"))
        self.label.setText(_translate("InstrumentAttributesDialog", "Staribus Address"))
        self.label_16.setText(_translate("InstrumentAttributesDialog", "Baudrate"))
        self.label_17.setText(_translate("InstrumentAttributesDialog", "Timeout"))
        self.label_2.setText(_translate("InstrumentAttributesDialog", "Starinet IP Address"))
        self.label_3.setText(_translate("InstrumentAttributesDialog", "Starinet Port"))
        self.label_4.setText(_translate("InstrumentAttributesDialog", "Label 0"))
        self.label_23.setText(_translate("InstrumentAttributesDialog", "Colour"))
        self.PickerButton6.setText(_translate("InstrumentAttributesDialog", "Colour Picker"))
        self.label_11.setText(_translate("InstrumentAttributesDialog", "Label 7"))
        self.label_24.setText(_translate("InstrumentAttributesDialog", "Colour"))
        self.PickerButton7.setText(_translate("InstrumentAttributesDialog", "Colour Picker"))
        self.label_12.setText(_translate("InstrumentAttributesDialog", "Label 8"))
        self.label_25.setText(_translate("InstrumentAttributesDialog", "Colour"))
        self.PickerButton8.setText(_translate("InstrumentAttributesDialog", "Colour Picker"))

