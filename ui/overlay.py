import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt

class OverlayWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Thiết lập các thuộc tính cho cửa sổ overlay
        self.setWindowFlags(
            Qt.WindowType.FramelessWindowHint |        # Không có khung viền
            Qt.WindowType.WindowStaysOnTopHint |       # Luôn hiển thị trên cùng
            Qt.WindowType.Tool                         # Không hiển thị trên taskbar
        )
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground) # Nền trong suốt

        # Tạo một widget trung tâm và layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Placeholder cho Avatar
        self.avatar_label = QLabel("Avatar Placeholder")
        self.avatar_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.avatar_label.setStyleSheet("color: white; font-size: 24px; background-color: rgba(0, 0, 0, 128);")
        layout.addWidget(self.avatar_label)

        # Placeholder cho Sóng âm
        self.waveform_label = QLabel("Voice Waveform")
        self.waveform_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.waveform_label.setStyleSheet("color: white; font-size: 16px; background-color: rgba(0, 0, 0, 128);")
        layout.addWidget(self.waveform_label)

        # Thiết lập kích thước và vị trí ban đầu
        self.setGeometry(100, 100, 300, 200)

# Khối mã để chạy thử nghiệm giao diện một cách độc lập
if __name__ == "__main__":
    app = QApplication(sys.argv)
    overlay = OverlayWindow()
    overlay.show()
    sys.exit(app.exec())
