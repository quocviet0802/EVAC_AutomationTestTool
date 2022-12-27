import AutoTestSlddService as service
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QAction
from PyQt5.QtGui import QPalette, QColor, QFont, QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt, QCoreApplication, QMetaObject, QRect
from PyQt5.QtWidgets import (
    QLabel,
    QGridLayout,
    QHBoxLayout,
    QFormLayout,
    QTabWidget,
    QWidget,
    QLineEdit,
    QFileDialog,
    QFrame,
    QGroupBox,
    QVBoxLayout,
    QMenu,
    QMenuBar,
    QStatusBar,
    QTextBrowser,
    QListView,
    QPushButton,
    QToolButton,
    QTableView
)


common_font = QFont()
common_font.setPointSize(10)


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Auto Test SLDD Application")
        self.setGeometry(300, 200, 900, 600)
        self.setFixedWidth(900)
        self.setFixedHeight(600)
        
        self.central_main_widget = QWidget(self)
        self.central_main_widget.setLayoutDirection(Qt.LeftToRight)
        
        # self.addMenu()
        self.add_content()
        
        self.setCentralWidget(self.central_main_widget)
        
    def addMenu(self):
        self.menubar = QMenuBar(self)
        
        self.menufile = QMenu(self.menubar)
        self.menufile.setTitle(QCoreApplication.translate("MainWindow", u"file", None))
        
        self.menuedit = QMenu(self.menubar)
        self.menuedit.setTitle(QCoreApplication.translate("MainWindow", u"edit", None))
        
        self.menuview = QMenu(self.menubar)
        self.menuview.setTitle(QCoreApplication.translate("MainWindow", u"view", None))
        
        self.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(self)
        self.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menufile.menuAction())
        self.menubar.addAction(self.menuedit.menuAction())
        self.menubar.addAction(self.menuview.menuAction())
    
    def add_content(self):
        self.tabWidget = QTabWidget(self.central_main_widget)
        self.tabWidget.setGeometry(QRect(0, 0, 900, 600))
        self.tabWidget.setLayoutDirection(Qt.LeftToRight)
        self.tabWidget.setTabPosition(QTabWidget.North) 
        self.tabWidget.setAutoFillBackground(True)        

        self.add_test_sldd_tab()
        self.create_test_case_tab()
        self.tabWidget.setCurrentIndex(0)

    def add_test_sldd_tab(self):
        self.test_sldd_tab = QWidget()
        
        # Input
        self.InputTestCaseGroup = QGroupBox(self.test_sldd_tab)
        self.InputTestCaseGroup.setGeometry(QRect(15, 15, 400, 80))
        # self.InputGroup.setTitle("Input")
        
        self.InputTestCasePathLabel = QLabel(self.InputTestCaseGroup)
        self.InputTestCasePathLabel.setGeometry(QRect(15, 20, 100, 30))
        self.InputTestCasePathLabel.setFont(common_font)
        self.InputTestCasePathLabel.setText("Input Path")
        
        self.TextTestCasePathBrowser = QLineEdit(self.InputTestCaseGroup)
        self.TextTestCasePathBrowser.setGeometry(QRect(80, 25, 270, 25))
        self.TextTestCasePathBrowser.setReadOnly(True)
        
        self.FileDialog = QFileDialog(self.InputTestCaseGroup)
        self.FileDialog.setFileMode(QFileDialog.AnyFile)

        self.OpenTestCaseFolderButton = QToolButton(self.InputTestCaseGroup)
        self.OpenTestCaseFolderButton.setText("...")
        self.OpenTestCaseFolderButton.setGeometry(QRect(360, 25, 25, 25))
        self.OpenTestCaseFolderButton.clicked.connect(self.event_tool_button)

        # TestCase
        self.TestCaseGroup_TabTest = QGroupBox(self.test_sldd_tab)
        self.TestCaseGroup_TabTest.setGeometry(QRect(15, 110, 825, 460))
        # self.TestCaseGroup_TabTest.setTitle("TestCaseGroup")
        
        self.TestCaseNameLabel_TabTest = QLabel(self.TestCaseGroup_TabTest)
        self.TestCaseNameLabel_TabTest.setText("Test Case")
        self.TestCaseNameLabel_TabTest.setFont(common_font)
        self.TestCaseNameLabel_TabTest.setGeometry(QRect(15, 15, 100, 30))
        
        self.TextTestCaseName_TabTest = QLineEdit(self.TestCaseGroup_TabTest)
        self.TextTestCaseName_TabTest.setReadOnly(True)
        self.TextTestCaseName_TabTest.setGeometry(QRect(80, 20, 720, 25))
        
        self.TestStepsLabel_TabTest = QLabel(self.TestCaseGroup_TabTest)
        self.TestStepsLabel_TabTest.setText("Test Steps")
        self.TestStepsLabel_TabTest.setFont(common_font)
        self.TestStepsLabel_TabTest.setGeometry(QRect(15, 50, 100, 30))
        
        self.TestSteplistView_TabTest = QListView(self.TestCaseGroup_TabTest)
        self.TestSteplistView_TabTest.setGeometry(QRect(80, 60, 720, 300))
        
        self.ExceptionLabel_TabTest = QLabel(self.TestCaseGroup_TabTest)
        self.ExceptionLabel_TabTest.setText("Exception")
        self.ExceptionLabel_TabTest.setFont(common_font)
        self.ExceptionLabel_TabTest.setGeometry(QRect(15, 365, 100, 30))
        
        self.ExceptionListView = QListView(self.TestCaseGroup_TabTest)
        self.ExceptionListView.setGeometry(QRect(80, 375, 720, 70))
        
        self.RunButton = QPushButton(self.test_sldd_tab)
        self.RunButton.setText("Run")
        self.RunButton.setGeometry(QRect(460, 40, 100, 25))
        self.RunButton.clicked.connect(self.event_run_test_case)
        
        self.SaveLogButton = QPushButton(self.test_sldd_tab)
        self.SaveLogButton.setText("Save Log")
        self.SaveLogButton.setGeometry(QRect(600, 40, 100, 25))
        
        self.ClearLogButton = QPushButton(self.test_sldd_tab)
        self.ClearLogButton.setText("Clear Log")
        self.ClearLogButton.setGeometry(QRect(740, 40, 100, 25))
        
        self.tabWidget.addTab(self.test_sldd_tab, "Auto Test")
    
    def create_test_case_tab(self):
        self.create_test_tab = QWidget()
    
        # Input
        self.InputGroup = QGroupBox(self.create_test_tab)
        self.InputGroup.setGeometry(QRect(15, 15, 400, 80))
        # self.InputGroup.setTitle("Input")

        self.InputPathLabel = QLabel(self.InputGroup)
        self.InputPathLabel.setGeometry(QRect(15, 20, 100, 30))
        self.InputPathLabel.setFont(common_font)
        self.InputPathLabel.setText("Input Path")
        
        self.TextPathBrowser = QTextBrowser(self.InputGroup)
        self.TextPathBrowser.setGeometry(QRect(80, 25, 270, 25))
        
        self.OpenFolderButton = QToolButton(self.InputGroup)
        self.OpenFolderButton.setText("...")
        self.OpenFolderButton.setGeometry(QRect(360, 25, 25, 25))
        
        # TestCase
        self.TestCaseGroup = QGroupBox(self.create_test_tab)
        self.TestCaseGroup.setGeometry(QRect(15, 110, 400, 400))
        # self.TestCaseGroup.setTitle("TestCaseGroup")
        
        self.TestCaseNameLabel = QLabel(self.TestCaseGroup)
        self.TestCaseNameLabel.setText("Test Case")
        self.TestCaseNameLabel.setFont(common_font)
        self.TestCaseNameLabel.setGeometry(QRect(15, 15, 100, 30))
        
        self.TextTestCaseName = QTextBrowser(self.TestCaseGroup)
        self.TextTestCaseName.setGeometry(QRect(80, 20, 270, 25))
        
        self.TestStepsLabel = QLabel(self.TestCaseGroup)
        self.TestStepsLabel.setText("Test Steps")
        self.TestStepsLabel.setFont(common_font)
        self.TestStepsLabel.setGeometry(QRect(15, 50, 100, 30))
        
        self.TestSteplistView = QListView(self.TestCaseGroup)
        self.TestSteplistView.setGeometry(QRect(80, 60, 270, 200))
        
        self.ExceptionLabel = QLabel(self.TestCaseGroup)
        self.ExceptionLabel.setText("Exception")
        self.ExceptionLabel.setFont(common_font)
        self.ExceptionLabel.setGeometry(QRect(15, 265, 100, 30))
        
        self.ExceptionListView = QListView(self.TestCaseGroup)
        self.ExceptionListView.setGeometry(QRect(80, 275, 270, 70))
        
        self.SaveTestCaseButton = QPushButton(self.TestCaseGroup)
        self.SaveTestCaseButton.setText("Save Test Case")
        self.SaveTestCaseButton.setGeometry(QRect(260, 355, 90, 25))
        
        # self.EditTestCaseButton = QPushButton(self.TestCaseGroup)
        # self.EditTestCaseButton.setText(QCoreApplication.translate("MainWindow", u"Edit Test Case", None))
        # self.EditTestCaseButton.setGeometry(QRect(240, 360, 91, 21))
        
        self.tabWidget.addTab(self.create_test_tab, "Create Test Case")


    def event_tool_button(self):
        # self.FileDialog.open
        file_path = self.FileDialog.getOpenFileName(self, "", "", "Json (*.json)")[0]
        if file_path:
            self.TextTestCasePathBrowser.setText(f"{file_path}")
            test_case = service.load_test_case(file_path)
            self.TextTestCaseName_TabTest.setText(test_case.test_case_name)
            model = QStandardItemModel()
            self.TestSteplistView_TabTest.setModel(model)
            for item in test_case.test_steps:
                print(test_case.test_steps[item].test_step_type)
                row = QStandardItem(test_case.test_steps[item].test_step_type)
                model.appendRow(row)
            

            # for item in test_case:
            #     print(item)

    def event_run_test_case(self):
        service.run()


def run_gui():
    application = QApplication([])
    mainWindow = MainWindow()
    mainWindow.show()
    application.exec()
