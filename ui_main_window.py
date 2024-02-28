from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QCheckBox, QFrame,
    QLabel, QLineEdit, QMainWindow, QMenuBar, QHBoxLayout,
    QProgressBar, QPushButton, QRadioButton, QSizePolicy,
    QStackedWidget, QTabWidget, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(640, 480)
        MainWindow.setMinimumSize(QSize(640, 480))
        MainWindow.setMaximumSize(QSize(640, 480))
        MainWindow.setWindowOpacity(0.92)
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        gradient = QLinearGradient(0, 0, 1, 0)
        gradient.setSpread(QGradient.PadSpread)
        gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient.setColorAt(0, QColor(10, 25, 47, 200))
        gradient.setColorAt(1, QColor(25, 50, 70, 200))
        brush1 = QBrush(gradient)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(255, 255, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(244, 244, 244, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(117, 117, 117, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(156, 156, 156, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        gradient1 = QLinearGradient(0, 0, 1, 0)
        gradient1.setSpread(QGradient.PadSpread)
        gradient1.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient1.setColorAt(0, QColor(10, 25, 47, 200))
        gradient1.setColorAt(1, QColor(25, 50, 70, 200))
        brush6 = QBrush(gradient1)
        palette.setBrush(QPalette.Active, QPalette.Base, brush6)
        gradient2 = QLinearGradient(0, 0, 1, 0)
        gradient2.setSpread(QGradient.PadSpread)
        gradient2.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient2.setColorAt(0, QColor(10, 25, 47, 200))
        gradient2.setColorAt(1, QColor(25, 50, 70, 200))
        brush7 = QBrush(gradient2)
        palette.setBrush(QPalette.Active, QPalette.Window, brush7)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush3)
        brush8 = QBrush(QColor(255, 255, 220, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush9 = QBrush(QColor(0, 0, 0, 127))
        brush9.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette.setBrush(QPalette.Active, QPalette.Accent, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        gradient3 = QLinearGradient(0, 0, 1, 0)
        gradient3.setSpread(QGradient.PadSpread)
        gradient3.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient3.setColorAt(0, QColor(10, 25, 47, 200))
        gradient3.setColorAt(1, QColor(25, 50, 70, 200))
        brush10 = QBrush(gradient3)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush10)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        gradient4 = QLinearGradient(0, 0, 1, 0)
        gradient4.setSpread(QGradient.PadSpread)
        gradient4.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient4.setColorAt(0, QColor(10, 25, 47, 200))
        gradient4.setColorAt(1, QColor(25, 50, 70, 200))
        brush11 = QBrush(gradient4)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush11)
        gradient5 = QLinearGradient(0, 0, 1, 0)
        gradient5.setSpread(QGradient.PadSpread)
        gradient5.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient5.setColorAt(0, QColor(10, 25, 47, 200))
        gradient5.setColorAt(1, QColor(25, 50, 70, 200))
        brush12 = QBrush(gradient5)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush12)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.Accent, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        gradient6 = QLinearGradient(0, 0, 1, 0)
        gradient6.setSpread(QGradient.PadSpread)
        gradient6.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient6.setColorAt(0, QColor(10, 25, 47, 200))
        gradient6.setColorAt(1, QColor(25, 50, 70, 200))
        brush13 = QBrush(gradient6)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush13)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        gradient7 = QLinearGradient(0, 0, 1, 0)
        gradient7.setSpread(QGradient.PadSpread)
        gradient7.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient7.setColorAt(0, QColor(10, 25, 47, 200))
        gradient7.setColorAt(1, QColor(25, 50, 70, 200))
        brush14 = QBrush(gradient7)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush14)
        gradient8 = QLinearGradient(0, 0, 1, 0)
        gradient8.setSpread(QGradient.PadSpread)
        gradient8.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient8.setColorAt(0, QColor(10, 25, 47, 200))
        gradient8.setColorAt(1, QColor(25, 50, 70, 200))
        brush15 = QBrush(gradient8)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        brush16 = QBrush(QColor(234, 234, 234, 255))
        brush16.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush16)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        brush17 = QBrush(QColor(117, 117, 117, 127))
        brush17.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush17)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.Accent, brush2)
        MainWindow.setPalette(palette)
        MainWindow.setStyleSheet(u"""
        QWidget#MainWindow {
            background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(10, 25, 47, 200), stop:1 rgba(25, 50, 70, 200));
        }
        
        QDialog#AboutDialogWindow {
            background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(10, 25, 47, 200), stop:1 rgba(25, 50, 70, 200));
        }

        QWidget#verticalLayoutWidget { /* Assuming you have a widget that holds the QVBoxLayout */
            background-color: rgba(0, 0, 0, 0); /* Fully transparent */
        }

        QStackedWidget#stackedWidget {
            background-color: rgba(0, 0, 0, 0); /* Fully transparent */
        }

        QLabel, QPushButton, QRadioButton, QCheckBox, QProgressBar {
            color: rgba(225, 245, 254, 255); /* Slightly blue-tinted white for better readability */
            font: 11pt "Segoe UI"; /* More modern and professional font */
        }

        QPushButton {
            background-color: rgba(70, 130, 180, 255); /* Softer blue for buttons */
            border: 1px solid rgba(60, 120, 170, 255); /* Slightly darker border for depth */
            border-radius: 4px; /* Rounded corners for a modern look */
        }

        QPushButton:hover {
            background-color: rgba(85, 145, 195, 255); /* Lighter on hover for interactive effect */
        }

        QPushButton:pressed {
            background-color: rgba(60, 110, 160, 255); /* Darker when pressed to simulate depth */
        }

        QProgressBar {
            background-color: rgba(35, 35, 70, 240); /* Dark background for contrast */
            border: 1px solid #2E2E5E; /* Slightly lighter border for subtle contrast */
            border-radius: 4px; /* Consistent rounded corners */
            padding: 2px; /* Adjust as necessary */
            margin: 0px; /* Adjust based on your layout needs */
            text-align: center; /* Ensure text is centered, might not affect all styles */
        }

        QProgressBar::chunk {
            background-color: rgba(95, 185, 234, 255); /* Brighter, more vibrant progress color */
            border-radius: 3px; /* Rounded corners inside the progress bar */
        }

        QLineEdit, QTextEdit {
            color: rgba(173, 216, 230, 255); /* Light blue color for text */
            /* Other properties like background-color, border, etc., can be added here as needed */
        }

        QLineEdit {
            background-color: rgba(40, 40, 40, 240); /* Dark background for contrast */
            border: 1px solid rgba(60, 60, 60, 240); /* Slightly lighter border for visibility */
            border-radius: 4px; /* Rounded corners for a modern look */
        }

        QTextEdit {
            background-color: rgba(40, 40, 40, 240); /* Dark background for contrast */
            border: 1px solid rgba(60, 60, 60, 240); /* Slightly lighter border for visibility */
            border-radius: 4px; /* Consistent with QLineEdit for a unified look */
        }

        QTabWidget::pane { /* The tab widget frame */
            border-top: 2px solid rgba(10, 25, 47, 180); /* Dark blue, slightly transparent border */
        }

        QTabWidget::tab-bar {
            alignment: center; /* Adjust the alignment of tabs as needed */
        }

        QTabBar::tab {
            background: rgba(10, 25, 47, 180); /* Dark blue, slightly transparent background for tabs */
            color: rgba(225, 245, 254, 255); /* Light text color for contrast */
            padding: 5px; /* Adjust padding as needed */
            border: 1px solid rgba(25, 50, 70, 180); /* Slightly lighter blue for the border, slightly transparent */
            border-bottom-color: transparent; /* Make the bottom border transparent for a seamless look */
            min-width: 80px; /* Adjust the minimum width as needed */
            min-height: 20px; /* Adjust the minimum height as needed */
        }

        QTabBar::tab:selected, QTabBar::tab:hover {
            background: rgba(25, 50, 70, 200); /* Slightly lighter and less transparent for the active or hovered tab */
            border-bottom-color: none; /* Can remove the bottom border for the selected tab if desired */
        }

        QTabBar::tab:!selected {
            margin-top: 2px; /* Slightly raise the unselected tabs to make the selected tab stand out */
        }

        QLabel {
            font: 11pt "Segoe UI"; /* Match the font size and family with QPushButton */
            color: rgba(225, 245, 254, 255); /* Adjust color as needed, here using a light color for contrast */
        }

        QPushButton, QRadioButton, QCheckBox {
            font: 11pt "Segoe UI"; /* Set a common font size and family for consistency */
            color: rgba(225, 245, 254, 255); /* Adjust color as needed */
        }

        QRadioButton, QCheckBox {
            font-size: 10pt; /* Set a smaller font size than QPushButton */
        }

        QTextEdit#AboutDialogText {
            font: 12pt "Courier";
        }

        QLabel#AboutDialogLabel {
            font: 10pt;
        }
        """)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushAboutButton = QPushButton(self.centralwidget)
        self.pushAboutButton.setObjectName(u"pushAboutButton")
        self.pushAboutButton.setGeometry(QRect(1, 420, 109, 24))
        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(110, 0, 16, 480))
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(120, 0, 511, 451))
        self.TextStackedWidget = QWidget()
        self.TextStackedWidget.setObjectName(u"TextStackedWidget")
        self.TextTabWidget = QTabWidget(self.TextStackedWidget)
        self.TextTabWidget.setObjectName(u"TextTabWidget")
        self.TextTabWidget.setGeometry(QRect(0, 0, 511, 441))
        self.TextTabWidget.setDocumentMode(False)
        self.EncryptTextTab = QWidget()
        self.EncryptTextTab.setObjectName(u"EncryptTextTab")
        self.InputEncryptionTextBox = QTextEdit(self.EncryptTextTab)
        self.InputEncryptionTextBox.setObjectName(u"InputEncryptionTextBox")
        self.InputEncryptionTextBox.setGeometry(QRect(30, 50, 451, 71))
        self.InputEncryptionPasswordLine = QLineEdit(self.EncryptTextTab)
        self.InputEncryptionPasswordLine.setObjectName(u"InputEncryptionPasswordLine")
        self.InputEncryptionPasswordLine.setGeometry(QRect(30, 150, 191, 22))
        self.EncryptTextButton = QPushButton(self.EncryptTextTab)
        self.EncryptTextButton.setObjectName(u"EncryptTextButton")
        self.EncryptTextButton.setGeometry(QRect(400, 380, 75, 24))
        self.OutputEncryptionTextBox = QTextEdit(self.EncryptTextTab)
        self.OutputEncryptionTextBox.setObjectName(u"OutputEncryptionTextBox")
        self.OutputEncryptionTextBox.setGeometry(QRect(30, 270, 451, 71))
        self.OutputEncryptionTextBox.setReadOnly(True)
        self.labelText_1 = QLabel(self.EncryptTextTab)
        self.labelText_1.setObjectName(u"labelText_1")
        self.labelText_1.setGeometry(QRect(40, 20, 71, 21))
        self.labelText_2 = QLabel(self.EncryptTextTab)
        self.labelText_2.setObjectName(u"labelText_2")
        self.labelText_2.setGeometry(QRect(40, 130, 61, 16))
        self.labelText_3 = QLabel(self.EncryptTextTab)
        self.labelText_3.setObjectName(u"labelText_3")
        self.labelText_3.setGeometry(QRect(40, 240, 151, 21))
        self.checkTextPasswordEncrBox = QCheckBox(self.EncryptTextTab)
        self.checkTextPasswordEncrBox.setObjectName(u"checkTextPasswordEncrBox")
        self.checkTextPasswordEncrBox.setGeometry(QRect(30, 180, 111, 20))
        self.TextTabWidget.addTab(self.EncryptTextTab, "")
        self.DecryptTextTab = QWidget()
        self.DecryptTextTab.setObjectName(u"DecryptTextTab")
        self.OutputDecryptionTextBox = QTextEdit(self.DecryptTextTab)
        self.OutputDecryptionTextBox.setObjectName(u"OutputDecryptionTextBox")
        self.OutputDecryptionTextBox.setGeometry(QRect(30, 270, 451, 71))
        self.OutputDecryptionTextBox.setReadOnly(True)
        self.DecryptTextButton = QPushButton(self.DecryptTextTab)
        self.DecryptTextButton.setObjectName(u"DecryptTextButton")
        self.DecryptTextButton.setGeometry(QRect(400, 380, 75, 24))
        self.InputDecryptionTextBox = QTextEdit(self.DecryptTextTab)
        self.InputDecryptionTextBox.setObjectName(u"InputDecryptionTextBox")
        self.InputDecryptionTextBox.setGeometry(QRect(30, 50, 451, 71))
        self.InputDecryptionPasswordLine = QLineEdit(self.DecryptTextTab)
        self.InputDecryptionPasswordLine.setObjectName(u"InputDecryptionPasswordLine")
        self.InputDecryptionPasswordLine.setGeometry(QRect(30, 150, 191, 22))
        self.labelText_4 = QLabel(self.DecryptTextTab)
        self.labelText_4.setObjectName(u"labelText_4")
        self.labelText_4.setGeometry(QRect(40, 20, 141, 21))
        self.labelText_5 = QLabel(self.DecryptTextTab)
        self.labelText_5.setObjectName(u"labelText_5")
        self.labelText_5.setGeometry(QRect(40, 130, 61, 16))
        self.labelText_6 = QLabel(self.DecryptTextTab)
        self.labelText_6.setObjectName(u"labelText_6")
        self.labelText_6.setGeometry(QRect(40, 240, 151, 21))
        self.checkTextPasswordDecrBox = QCheckBox(self.DecryptTextTab)
        self.checkTextPasswordDecrBox.setObjectName(u"checkTextPasswordDecrBox")
        self.checkTextPasswordDecrBox.setGeometry(QRect(30, 180, 111, 20))
        self.TextTabWidget.addTab(self.DecryptTextTab, "")
        self.stackedWidget.addWidget(self.TextStackedWidget)
        self.FileStackedWidget = QWidget()
        self.FileStackedWidget.setObjectName(u"FileStackedWidget")
        self.progressFileBar = QProgressBar(self.FileStackedWidget)
        self.progressFileBar.setObjectName(u"progressFileBar")
        self.progressFileBar.setGeometry(QRect(40, 50, 471, 61))
        self.progressFileBar.setValue(0)
        self.pushOpenFileButton = QPushButton(self.FileStackedWidget)
        self.pushOpenFileButton.setObjectName(u"pushOpenFileButton")
        self.pushOpenFileButton.setGeometry(QRect(410, 170, 101, 41))
        self.pushFileActionButton = QPushButton(self.FileStackedWidget)
        self.pushFileActionButton.setObjectName(u"pushFileActionButton")
        self.pushFileActionButton.setGeometry(QRect(40, 400, 451, 51))
        self.radioDecryptionButton = QRadioButton(self.FileStackedWidget)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.radioDecryptionButton)
        self.radioDecryptionButton.setObjectName(u"radioDecryptionButton")
        self.radioDecryptionButton.setGeometry(QRect(300, 280, 89, 20))
        self.radioEncryptionButton = QRadioButton(self.FileStackedWidget)
        self.buttonGroup.addButton(self.radioEncryptionButton)
        self.radioEncryptionButton.setObjectName(u"radioEncryptionButton")
        self.radioEncryptionButton.setGeometry(QRect(300, 250, 89, 20))
        self.radioEncryptionButton.setChecked(True)
        self.lineFilePath = QLineEdit(self.FileStackedWidget)
        self.lineFilePath.setObjectName(u"lineFilePath")
        self.lineFilePath.setGeometry(QRect(120, 180, 281, 22))
        self.lineFilePath.setReadOnly(True)
        self.labelFile_1 = QLabel(self.FileStackedWidget)
        self.labelFile_1.setObjectName(u"labelFile_1")
        self.labelFile_1.setGeometry(QRect(60, 180, 51, 21))
        self.labelFile_3 = QLabel(self.FileStackedWidget)
        self.labelFile_3.setObjectName(u"labelFile_3")
        self.labelFile_3.setGeometry(QRect(50, 260, 61, 21))
        self.lineFilePassword = QLineEdit(self.FileStackedWidget)
        self.lineFilePassword.setObjectName(u"lineFilePassword")
        self.lineFilePassword.setGeometry(QRect(120, 260, 141, 22))
        self.checkFilePasswordBox = QCheckBox(self.FileStackedWidget)
        self.checkFilePasswordBox.setObjectName(u"checkFilePasswordBox")
        self.checkFilePasswordBox.setGeometry(QRect(120, 290, 121, 20))
        self.lineNewFileName = QLineEdit(self.FileStackedWidget)
        self.lineNewFileName.setObjectName(u"lineNewFileName")
        self.lineNewFileName.setGeometry(QRect(120, 220, 141, 22))
        self.labelFile_2 = QLabel(self.FileStackedWidget)
        self.labelFile_2.setObjectName(u"labelFile_2")
        self.labelFile_2.setGeometry(QRect(20, 220, 91, 21))
        self.stackedWidget.addWidget(self.FileStackedWidget)
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 60, 111, 161))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushTextButton = QPushButton(self.layoutWidget)
        self.sidePanelButtonGroup = QButtonGroup(MainWindow)
        self.sidePanelButtonGroup.setObjectName(u"sidePanelButtonGroup")
        self.sidePanelButtonGroup.addButton(self.pushTextButton)
        self.pushTextButton.setObjectName(u"pushTextButton")
        self.pushTextButton.setMinimumSize(QSize(0, 40))
        self.pushTextButton.setCheckable(True)
        self.pushTextButton.setChecked(True)

        self.verticalLayout.addWidget(self.pushTextButton)

        self.pushFileButton = QPushButton(self.layoutWidget)
        self.sidePanelButtonGroup.addButton(self.pushFileButton)
        self.pushFileButton.setObjectName(u"pushFileButton")
        self.pushFileButton.setMinimumSize(QSize(0, 40))
        self.pushFileButton.setCheckable(True)

        self.verticalLayout.addWidget(self.pushFileButton)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 23))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)
        self.TextTabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AES PyEncryptor", None))
        self.pushAboutButton.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.EncryptTextButton.setText(QCoreApplication.translate("MainWindow", u"Encrypt", None))
        self.labelText_1.setText(QCoreApplication.translate("MainWindow", u"Input Text", None))
        self.labelText_2.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.labelText_3.setText(QCoreApplication.translate("MainWindow", u"Output Encrypted Text", None))
        self.checkTextPasswordEncrBox.setText(QCoreApplication.translate("MainWindow", u"Show password", None))
        self.TextTabWidget.setTabText(self.TextTabWidget.indexOf(self.EncryptTextTab), QCoreApplication.translate("MainWindow", u"Encryption", None))
        self.DecryptTextButton.setText(QCoreApplication.translate("MainWindow", u"Decrypt", None))
        self.labelText_4.setText(QCoreApplication.translate("MainWindow", u"Input Encrypted Text", None))
        self.labelText_5.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.labelText_6.setText(QCoreApplication.translate("MainWindow", u"Output Decrypted Text", None))
        self.checkTextPasswordDecrBox.setText(QCoreApplication.translate("MainWindow", u"Show password", None))
        self.TextTabWidget.setTabText(self.TextTabWidget.indexOf(self.DecryptTextTab), QCoreApplication.translate("MainWindow", u"Decryption", None))
        self.pushOpenFileButton.setText(QCoreApplication.translate("MainWindow", u"OpenFile", None))
        self.pushFileActionButton.setText(QCoreApplication.translate("MainWindow", u"Encrypt", None))
        self.radioDecryptionButton.setText(QCoreApplication.translate("MainWindow", u"Decryption", None))
        self.radioEncryptionButton.setText(QCoreApplication.translate("MainWindow", u"Encryption", None))
        self.labelFile_1.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">File Path</span></p></body></html>", None))
        self.labelFile_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Password</span></p></body></html>", None))
        self.checkFilePasswordBox.setText(QCoreApplication.translate("MainWindow", u"Show password", None))
        self.labelFile_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">New File Name</span></p></body></html>", None))
        self.pushTextButton.setText(QCoreApplication.translate("MainWindow", u"Text", None))
        self.pushFileButton.setText(QCoreApplication.translate("MainWindow", u"File", None))
    # retranslateUi