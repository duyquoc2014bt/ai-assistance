import sys
from PyQt6.QtWidgets import QApplication
from ui.overlay import OverlayWindow
from services.browser_automation import play_youtube_video
# from services.command_parser import parse_command # Đã lỗi thời
from services.bluetooth_manager import connect_to_nearest_speaker
from services.voice_module import listen_for_command
from services.ai_core import get_ai_response
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
        print("\nTrợ lý ảo đã sẵn sàng để lắng nghe...")
        while True:
            try:
                # Thay thế input() bằng module lắng nghe giọng nói
                command = listen_for_command()

                # Thoát nếu lệnh là exit/quit (chỉ để an toàn, vì listen_for_command hiện không trả về lệnh này)
                if command.lower() in ["exit", "quit", "thoát"]:
                    print("Đang đóng trợ lý ảo...")
                    app.quit()
                    break

                # Phân tích lệnh bằng AI
                print(f"Đang gửi lệnh '{command}' đến AI để phân tích...")
                ai_result = get_ai_response(command)
                intent = ai_result.get("intent")
                entities = ai_result.get("entities", {})

                if intent == "play_music":
                    # Xây dựng truy vấn tìm kiếm từ các thực thể AI trích xuất được
                    search_query = " ".join(entities.values())
                    if search_query:
                        print(f"AI đã hiểu ý định: Phát nhạc. Truy vấn: '{search_query}'")
                        play_youtube_video(search_query)
                    else:
                        print("AI không thể xác định bạn muốn nghe gì. Vui lòng thử lại.")

                elif intent == "connect_bluetooth":
                    print(f"AI đã hiểu ý định: Kết nối Bluetooth.")
                    connect_to_nearest_speaker()

                elif intent == "error":
                    print(f"Lỗi từ Lõi AI: {ai_result.get('details')}")

                else: # intent == "unknown"
                    print(f"AI không thể xác định ý định cho lệnh: '{command}'")

            except Exception as e:
                print(f"Đã xảy ra lỗi trong vòng lặp lệnh: {e}")
                break

        print("Luồng backend đã kết thúc.")

    # Tạo và bắt đầu luồng cho vòng lặp lệnh
    print("Chuẩn bị khởi động luồng backend...")
    backend_thread = threading.Thread(target=command_loop)
    backend_thread.daemon = True  # Đặt làm daemon thread
    backend_thread.start()
    print("Luồng backend đã được khởi động.")

    # Bắt đầu vòng lặp sự kiện của ứng dụng GUI
    print("Bắt đầu vòng lặp sự kiện của GUI... (Nhấn Ctrl+C trong terminal để thoát)")
    try:
        sys.exit(app.exec())
    except KeyboardInterrupt:
        print("\nĐã nhận tín hiệu Ctrl+C. Đang đóng ứng dụng...")
        # Không cần làm gì thêm vì daemon thread sẽ tự động tắt

if __name__ == "__main__":
    main()
