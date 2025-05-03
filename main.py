import sys
import os
import PySide6
from PySide6.QtWidgets import QApplication, QMainWindow

# Наш сгенеренный файл!
from mainwindow import Ui_MainWindow

  
# Это просто надо
dirname = os.path.dirname(PySide6.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path


class MainWindow(QMainWindow):
	def __init__(self):
		# Это нужно для доступа к объектам, которые создаются в дизайнере
		super(MainWindow, self).__init__()

		# В качестве дизайна указвыаем наш	
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)


if __name__ == "__main__":
	# Создаем объект графического приложения в памяти
	app = QApplication(sys.argv)

	# Создаем объект окна в памяти
	window = MainWindow()
	
	# Показываем
	window.show()
	
	# Работаем, пока пользователь не закроет окно
	sys.exit(app.exec())