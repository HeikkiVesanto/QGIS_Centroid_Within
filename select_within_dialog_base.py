# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select_within_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_SelectWithinDialogBase(object):
    def setupUi(self, SelectWithinDialogBase):
        SelectWithinDialogBase.setObjectName("SelectWithinDialogBase")
        SelectWithinDialogBase.resize(312, 367)
        self.horizontalLayout = QtWidgets.QHBoxLayout(SelectWithinDialogBase)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(SelectWithinDialogBase)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.selectFromCombo = QgsMapLayerComboBox(SelectWithinDialogBase)
        self.selectFromCombo.setObjectName("selectFromCombo")
        self.verticalLayout.addWidget(self.selectFromCombo)
        self.label_2 = QtWidgets.QLabel(SelectWithinDialogBase)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.centroidRadioButton = QtWidgets.QRadioButton(SelectWithinDialogBase)
        self.centroidRadioButton.setMinimumSize(QtCore.QSize(60, 0))
        self.centroidRadioButton.setChecked(True)
        self.centroidRadioButton.setObjectName("centroidRadioButton")
        self.Where_Group = QtWidgets.QButtonGroup(SelectWithinDialogBase)
        self.Where_Group.setObjectName("Where_Group")
        self.Where_Group.addButton(self.centroidRadioButton)
        self.horizontalLayout_2.addWidget(self.centroidRadioButton)
        self.pointonsurfaceRadioButton = QtWidgets.QRadioButton(SelectWithinDialogBase)
        self.pointonsurfaceRadioButton.setMinimumSize(QtCore.QSize(100, 0))
        self.pointonsurfaceRadioButton.setObjectName("pointonsurfaceRadioButton")
        self.Where_Group.addButton(self.pointonsurfaceRadioButton)
        self.horizontalLayout_2.addWidget(self.pointonsurfaceRadioButton)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.poleOfInaccessibilityRadioButton = QtWidgets.QRadioButton(SelectWithinDialogBase)
        self.poleOfInaccessibilityRadioButton.setMinimumSize(QtCore.QSize(130, 0))
        self.poleOfInaccessibilityRadioButton.setObjectName("poleOfInaccessibilityRadioButton")
        self.Where_Group.addButton(self.poleOfInaccessibilityRadioButton)
        self.horizontalLayout_4.addWidget(self.poleOfInaccessibilityRadioButton)
        self.poiTolSpin = QtWidgets.QDoubleSpinBox(SelectWithinDialogBase)
        self.poiTolSpin.setEnabled(False)
        self.poiTolSpin.setSuffix("")
        self.poiTolSpin.setMinimum(0.01)
        self.poiTolSpin.setMaximum(100000.0)
        self.poiTolSpin.setProperty("value", 1.0)
        self.poiTolSpin.setObjectName("poiTolSpin")
        self.horizontalLayout_4.addWidget(self.poiTolSpin)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.mostlyWithinRadioButton = QtWidgets.QRadioButton(SelectWithinDialogBase)
        self.mostlyWithinRadioButton.setObjectName("mostlyWithinRadioButton")
        self.Where_Group.addButton(self.mostlyWithinRadioButton)
        self.horizontalLayout_5.addWidget(self.mostlyWithinRadioButton)
        self.mostlySpin = QtWidgets.QDoubleSpinBox(SelectWithinDialogBase)
        self.mostlySpin.setEnabled(False)
        self.mostlySpin.setMinimum(0.01)
        self.mostlySpin.setMaximum(100.0)
        self.mostlySpin.setProperty("value", 50.0)
        self.mostlySpin.setObjectName("mostlySpin")
        self.horizontalLayout_5.addWidget(self.mostlySpin)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.label_3 = QtWidgets.QLabel(SelectWithinDialogBase)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.selectWithCombo = QgsMapLayerComboBox(SelectWithinDialogBase)
        self.selectWithCombo.setObjectName("selectWithCombo")
        self.verticalLayout.addWidget(self.selectWithCombo)
        self.selectedFeaturesCheckbox = QtWidgets.QCheckBox(SelectWithinDialogBase)
        self.selectedFeaturesCheckbox.setChecked(True)
        self.selectedFeaturesCheckbox.setObjectName("selectedFeaturesCheckbox")
        self.verticalLayout.addWidget(self.selectedFeaturesCheckbox)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.newSelectionRadioButton = QtWidgets.QRadioButton(SelectWithinDialogBase)
        self.newSelectionRadioButton.setChecked(True)
        self.newSelectionRadioButton.setObjectName("newSelectionRadioButton")
        self.Selection_Group = QtWidgets.QButtonGroup(SelectWithinDialogBase)
        self.Selection_Group.setObjectName("Selection_Group")
        self.Selection_Group.addButton(self.newSelectionRadioButton)
        self.horizontalLayout_3.addWidget(self.newSelectionRadioButton)
        self.currentSelectionRadioButton = QtWidgets.QRadioButton(SelectWithinDialogBase)
        self.currentSelectionRadioButton.setObjectName("currentSelectionRadioButton")
        self.Selection_Group.addButton(self.currentSelectionRadioButton)
        self.horizontalLayout_3.addWidget(self.currentSelectionRadioButton)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.Advanced = QtWidgets.QGroupBox(SelectWithinDialogBase)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.Advanced.sizePolicy().hasHeightForWidth())
        self.Advanced.setSizePolicy(sizePolicy)
        self.Advanced.setMinimumSize(QtCore.QSize(0, 80))
        self.Advanced.setObjectName("Advanced")
        self.noIndexSelectFrom = QtWidgets.QCheckBox(self.Advanced)
        self.noIndexSelectFrom.setGeometry(QtCore.QRect(10, 20, 281, 17))
        self.noIndexSelectFrom.setObjectName("noIndexSelectFrom")
        self.noIndexSelectWith = QtWidgets.QCheckBox(self.Advanced)
        self.noIndexSelectWith.setGeometry(QtCore.QRect(10, 40, 281, 17))
        self.noIndexSelectWith.setObjectName("noIndexSelectWith")
        self.noDissolveSelectWith = QtWidgets.QCheckBox(self.Advanced)
        self.noDissolveSelectWith.setEnabled(False)
        self.noDissolveSelectWith.setGeometry(QtCore.QRect(10, 60, 281, 17))
        self.noDissolveSelectWith.setToolTip("")
        self.noDissolveSelectWith.setObjectName("noDissolveSelectWith")
        self.verticalLayout.addWidget(self.Advanced)
        self.button_box = QtWidgets.QDialogButtonBox(SelectWithinDialogBase)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.verticalLayout.addWidget(self.button_box)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(SelectWithinDialogBase)
        self.button_box.rejected.connect(SelectWithinDialogBase.reject)
        self.button_box.accepted.connect(SelectWithinDialogBase.accept)
        QtCore.QMetaObject.connectSlotsByName(SelectWithinDialogBase)

    def retranslateUi(self, SelectWithinDialogBase):
        _translate = QtCore.QCoreApplication.translate
        SelectWithinDialogBase.setWindowTitle(_translate("SelectWithinDialogBase", "Select Within"))
        self.label.setText(_translate("SelectWithinDialogBase", "Select all features from:"))
        self.label_2.setText(_translate("SelectWithinDialogBase", "Where:"))
        self.centroidRadioButton.setText(_translate("SelectWithinDialogBase", "Centroid"))
        self.pointonsurfaceRadioButton.setText(_translate("SelectWithinDialogBase", "Point on Surface"))
        self.poleOfInaccessibilityRadioButton.setText(_translate("SelectWithinDialogBase", "Pole of Inaccessibility"))
        self.poiTolSpin.setToolTip(_translate("SelectWithinDialogBase", "Tolerance. Leave at 1.0 if unsure."))
        self.mostlyWithinRadioButton.setText(_translate("SelectWithinDialogBase", "Pecrcentage (slow)"))
        self.label_3.setText(_translate("SelectWithinDialogBase", "Is within:"))
        self.selectedFeaturesCheckbox.setText(_translate("SelectWithinDialogBase", "Using selected features"))
        self.newSelectionRadioButton.setText(_translate("SelectWithinDialogBase", "Creating new selection"))
        self.currentSelectionRadioButton.setText(_translate("SelectWithinDialogBase", "Adding to current selection"))
        self.Advanced.setTitle(_translate("SelectWithinDialogBase", "Advanced"))
        self.noIndexSelectFrom.setToolTip(_translate("SelectWithinDialogBase", "Slower, but might be useful if errors occur."))
        self.noIndexSelectFrom.setText(_translate("SelectWithinDialogBase", "Don\'t use index on select from layer"))
        self.noIndexSelectWith.setToolTip(_translate("SelectWithinDialogBase", "Slower, but might be useful if errors occur."))
        self.noIndexSelectWith.setText(_translate("SelectWithinDialogBase", "Don\'t use index on select with layer"))
        self.noDissolveSelectWith.setText(_translate("SelectWithinDialogBase", "Don\'t dissolve before percentage within selection"))

from qgis.gui import QgsMapLayerComboBox
