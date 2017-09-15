import sys
from LedIndicatorWidget import *
import DemoAppUi


class DemoApp(QMainWindow, DemoAppUi.Ui_DemoApp):
    def __init__(self):
        super(self.__class__, self).__init__()

        self.setupUi(self)

        self.led = LedIndicator(self)
        self.led.setDisabled(True)  # Make the led non clickable
        self.horizontalLayout.addWidget(self.led)

        # Make the led red
        # self.led.on_color_1 = QColor(255, 0, 0)
        # self.led.on_color_2 = QColor(176, 0, 0)
        # self.led.off_color_1 = QColor(28, 0, 0)
        # self.led.off_color_2 = QColor(156, 0, 0)

        self.pushButton.clicked.connect(lambda: self.onPressButton())

    def onPressButton(self):
        self.led.setChecked(not self.led.isChecked())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = DemoApp()
    form.show()
    sys.exit(app.exec_())
