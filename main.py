import sys
from PyQt6.QtWidgets import QApplication
from ui.overlay import OverlayWindow
from services.browser_automation import play_youtube_video
import threading

def main():
    """
    Điểm khởi đầu chính của ứng dụng.
    """
    # Khởi tạo ứng dụng GUI
    app = QApplication(sys.argv)

    # Tạo và hiển thị cửa sổ overlay
    overlay = OverlayWindow()
    overlay.show()

    # --- Tích hợp Backend ---
    # Chạy tác vụ tự động hóa trình duyệt trong một luồng riêng
    # để không làm treo giao diện người dùng.
    search_query = "Sơn Tùng MTP"

    def browser_task():
        print(f"Bắt đầu tác vụ backend: tìm kiếm '{search_query}'")
        play_youtube_video(search_query)
        print("Tác vụ backend đã hoàn tất.")
        # Sau khi hoàn thành, có thể thêm code để đóng ứng dụng hoặc cập nhật UI
        # Ví dụ: app.quit()

    # Tạo và bắt đầu luồng cho tác vụ backend
    print("Chuẩn bị khởi động luồng backend...")
    backend_thread = threading.Thread(target=browser_task)
    backend_thread.start()
    print("Luồng backend đã được khởi động.")

    # Bắt đầu vòng lặp sự kiện của ứng dụng GUI
    print("Bắt đầu vòng lặp sự kiện của GUI...")
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
