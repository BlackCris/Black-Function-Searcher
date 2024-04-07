from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QTextEdit, QPushButton, QLabel, QScrollArea, QVBoxLayout
from PyQt5.QtCore import Qt
import sys
import json
import webbrowser
import os

if getattr(sys, 'frozen', False):
    application_path = os.path.dirname(sys.executable)
else:
    application_path = os.path.dirname(os.path.abspath(__file__))

functions_json_path = os.path.join(application_path, 'functions.json')

class CodeFunctionSearcher(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Black Python Function Searcher')
        self.setGeometry(100, 100, 600, 400)
        self.functions = self.load_functions("functions.json")
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.search_box = QLineEdit()
        self.search_box.setPlaceholderText("输入搜索词...")
        layout.addWidget(self.search_box)

        # 使用QScrollArea显示搜索结果
        self.scroll_area = QScrollArea()
        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout()
        self.scroll_widget.setLayout(self.scroll_layout)

        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.scroll_widget)
        layout.addWidget(self.scroll_area)

        self.setLayout(layout)
        self.search_box.textChanged.connect(self.on_search)

    def load_functions(self, filename):
        with open(functions_json_path, "r", encoding="utf-8") as file:  # 注意这里使用了变量functions_json_path
         functions = json.load(file)
        return functions


    def on_search(self):
        search_term = self.search_box.text().lower()
        # 清空旧的搜索结果
        for i in reversed(range(self.scroll_layout.count())): 
            self.scroll_layout.itemAt(i).widget().setParent(None)
        
        # 显示新的搜索结果
        for name, info in self.functions.items():
            if search_term in name.lower() or search_term in info['description'].lower():
                func_label = QLabel(f"Function: {name}\nDescription: {info['description']}\nExample: {info['example']}\n")
                self.scroll_layout.addWidget(func_label)
                
                doc_button = QPushButton("打开文档")
                doc_button.clicked.connect(lambda _, url=info['url']: webbrowser.open(url))
                self.scroll_layout.addWidget(doc_button)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = CodeFunctionSearcher()
    ex.show()
    sys.exit(app.exec_())
