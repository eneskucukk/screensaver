import sys
import threading
import time

from PySide2.QtCore import *
from PySide2.QtGui import QMovie
from PySide2.QtWidgets import QApplication, QLabel, QMainWindow, QWidget


class Second(QMainWindow):
    def __init__(self, parent=None):
        super(Second, self).__init__(parent)

        self.flag = None
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setGeometry(QRect(0, 0, 1920, 1080))

        self.label.setObjectName("label")

        self.setCentralWidget(self.centralwidget)

        self.movie = QMovie("/home/enes/Desktop/projeler/ScreenSaver/gif-Backgrounds-Wallpaper-Cave.gif")
        self.label.setMovie(self.movie)
        self.movie.start()
        self.app = Application

    def screenSaverHide(self):
        dialog.hide()
        self.app.counter = 0
        self.flag = 1
        print(self.flag)

    def mousePressEvent(self, e):
        self.screenSaverHide()

    def wheelEvent(self, e):
        self.screenSaverHide()

    def mouseReleaseEvent(self, e):
        self.screenSaverHide()

    def mouseMoveEvent(self, e):
        self.screenSaverHide()


class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300, 450, 300)
        self.setWindowTitle('Event object')

        self.show()

        t1 = threading.Thread(target=self.time_counter)
        t1.setDaemon(True)
        t1.start()

        global dialog
        dialog = Second()
        dialog.close()
        self.flag = 1
        self.counter = 0

    def time_counter(self):
        screenSaver = Second()
        screenSaver.close()
        self.counter = 0
        while True:
            self.counter += 1
            time.sleep(5)
            print(self.counter)
            if screenSaver.flag == 1 and self.flag != 1:
                dialog.hide()
                self.counter = 0
            elif self.counter == 3 and self.flag == 1:
                dialog.showFullScreen()

            elif self.counter >= 3:
                self.counter = 0

    def mouse_event_active(self):
        dialog.hide()
        self.flag = 1
        self.event_timer = 0
        self.counter = 0

    def is_another_event_called(self):
        self.event_timer += 1
        print(self.event_timer)
        time.sleep(1)
        if self.event_timer == 10:
            self.flag = 0
            dialog.showFullScreen()

    def mousePressEvent(self, e):
        self.mouse_event_active()
        print("mousePressEvent")

        while not self.mouseReleaseEvent and not self.wheelEvent and not self.mouseMoveEvent:
            self.is_another_event_called()
            break

    def wheelEvent(self, e):
        self.mouse_event_active()
        print("wheelEvent")
        while not self.mouseReleaseEvent and not self.mouseMoveEvent and not self.mousePressEvent:
            self.is_another_event_called()
            break

    def mouseReleaseEvent(self, e):
        self.mouse_event_active()
        print("mouseReleaseEvent")
        while not self.mouseMoveEvent and not self.wheelEvent and not self.mousePressEvent:
            self.is_another_event_called()
            break

    def mouseMoveEvent(self, e):
        self.mouse_event_active()
        print("mouseMoveEvent")
        while not self.mouseReleaseEvent and not self.wheelEvent and not self.mousePressEvent:
            self.is_another_event_called()
            break


def main():
    app = QApplication(sys.argv)
    ex = Application()
    sys.exit(app.exec_())


if __name__ == '__main__':

    main()
