import asyncio
from playwright.sync_api import sync_playwright, Page
import sys

def play_youtube_video(search_query: str):
    """
    Mở trình duyệt, tìm kiếm trên YouTube và phát video đầu tiên.
    """
    with sync_playwright() as p:
        # Khởi chạy trình duyệt. Thay `headless=False` để thấy cửa sổ trình duyệt.
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        try:
            print(f"Đang điều hướng đến YouTube...")
            page.goto("https://www.youtube.com", timeout=60000)

            # Chờ trang tải và tìm ô tìm kiếm
            print(f"Đang tìm kiếm '{search_query}'...")
            search_box = page.locator('input[name="search_query"]')
            search_box.fill(search_query)
            search_box.press("Enter")

            # Chờ kết quả tìm kiếm xuất hiện
            print("Đang chờ kết quả tìm kiếm...")
            # Selector cho tiêu đề video trong kết quả tìm kiếm
            first_video_selector = "ytd-video-renderer a#video-title"
            page.wait_for_selector(first_video_selector, timeout=30000)

            # Nhấp vào video đầu tiên
            print("Đã tìm thấy video. Đang nhấp vào kết quả đầu tiên...")
            page.locator(first_video_selector).first.click()

            # Chờ một chút để video bắt đầu phát trước khi đóng
            print(f"Đang phát video cho '{search_query}'. Tác vụ sẽ kết thúc sau 10 giây.")
            page.wait_for_timeout(10000) # Giữ trình duyệt mở trong 10 giây

        except Exception as e:
            print(f"Đã xảy ra lỗi: {e}", file=sys.stderr)
        finally:
            print("Đóng trình duyệt.")
            browser.close()

# Khối mã để chạy thử nghiệm module một cách độc lập
if __name__ == "__main__":
    query = "Sơn Tùng MTP"
    print(f"Bắt đầu tác vụ tự động hóa trình duyệt cho: '{query}'")
    play_youtube_video(query)
    print("Tác vụ tự động hóa trình duyệt đã hoàn tất.")
