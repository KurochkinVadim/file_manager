import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QFileSystemModel,
    QTreeView, QVBoxLayout, QWidget, QLabel
)

class FileManager(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Простой файловый менеджер")
        self.setGeometry(100, 100, 800, 600)

        # Модель файловой системы
        self.model = QFileSystemModel()
        self.model.setRootPath("")  # Корневая директория

        # Виджет для отображения файлов
        self.tree_view = QTreeView()
        self.tree_view.setModel(self.model)
        self.tree_view.setRootIndex(self.model.index(""))  # Показываем корень

        # Статус-бар (показывает путь к файлу)
        self.status_label = QLabel("Готово")
        self.statusBar().addWidget(self.status_label)

        # Основной layout
        layout = QVBoxLayout()
        layout.addWidget(self.tree_view)

        # Центральный виджет
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Сигналы
        self.tree_view.clicked.connect(self.on_file_clicked)

    def on_file_clicked(self, index):
        """Обработка клика по файлу/папке"""
        file_path = self.model.filePath(index)
        self.status_label.setText(f"Выбрано: {file_path}")
        print(f"Переход на {file_path}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FileManager()
    window.show()
    sys.exit(app.exec_())