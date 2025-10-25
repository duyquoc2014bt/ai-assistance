import sys
from PyQt6.QtWidgets import QApplication
from ui.overlay import OverlayWindow
from services.browser_automation import play_youtube_video
from services.command_parser import parse_command
from services.bluetooth_manager import connect_to_nearest_speaker
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
    # Vòng lặp chính để nhận và xử lý lệnh từ người dùng
    def command_loop():
        print("\nTrợ lý ảo đã sẵn sàng. Vui lòng nhập lệnh...")
        while True:
            try:
                command = input("Bạn muốn làm gì? > ")
                if command.lower() in ["exit", "quit", "thoát"]:
                    print("Đang đóng trợ lý ảo...")
                    app.quit()
                    break

                # Phân tích lệnh
                parsed_command = parse_command(command)
                intent = parsed_command.get("intent")
                details = parsed_command.get("details")

                if intent == "play_music":
                    if details:
                        print(f"Đã hiểu ý định: Phát nhạc. Chi tiết: '{details}'")
                        play_youtube_video(details)
                    else:
                        print("Bạn muốn nghe nhạc gì? Vui lòng nói rõ hơn.")
                elif intent == "connect_bluetooth":
                    print(f"Đã hiểu ý định: Kết nối Bluetooth.")
                    connect_to_nearest_speaker()
                else:
                    print(f"Xin lỗi, tôi chưa hiểu lệnh: '{command}'")

            except Exception as e:
                print(f"Đã xảy ra lỗi trong vòng lặp lệnh: {e}")
                break

        print("Luồng backend đã kết thúc.")

    # Tạo và bắt đầu luồng cho vòng lặp lệnh
    print("Chuẩn bị khởi động luồng backend...")
    backend_thread = threading.Thread(target=command_loop)
    backend_thread.start()
    print("Luồng backend đã được khởi động.")

    # Bắt đầu vòng lặp sự kiện của ứng dụng GUI
    print("Bắt đầu vòng lặp sự kiện của GUI...")
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
