import os
import google.generativeai as genai
import json

# --- HƯỚNG DẪN CÀI ĐẶT ---
# 1. Lấy API Key của bạn từ Google AI Studio: https://aistudio.google.com/app/apikey
# 2. Thiết lập biến môi trường trong terminal của bạn TRƯỚC KHI chạy ứng dụng:
#    export GOOGLE_API_KEY='YOUR_API_KEY_HERE'
#    (Thay 'YOUR_API_KEY_HERE' bằng key thật của bạn)

def get_ai_response(user_command: str) -> dict:
    """
    Sử dụng mô hình ngôn ngữ lớn để phân tích lệnh của người dùng và
    trích xuất ý định (intent) cũng như các thực thể (entities).
    """
    try:
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            print("LỖI: Biến môi trường GOOGLE_API_KEY chưa được thiết lập.")
            return {"intent": "error", "details": "API key not configured."}

        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')

        # Đây là "prompt" - hướng dẫn cho AI biết phải làm gì.
        # Chúng ta yêu cầu nó hoạt động như một bộ phân tích lệnh và trả về JSON.
        prompt = f"""
            Analyze the user's command for a virtual assistant and return a JSON object.
            The JSON object must have two keys: "intent" and "entities".
            - "intent" can be one of: "play_music", "connect_bluetooth", "unknown".
            - "entities" is a dictionary containing extracted information. For "play_music", it should include "song_description" or "artist".

            User command: "{user_command}"

            JSON response:
        """

        response = model.generate_content(prompt)

        # Trích xuất và làm sạch phần JSON từ phản hồi của AI
        response_text = response.text.strip()
        # Đôi khi model có thể trả về ```json ... ```, chúng ta cần loại bỏ nó
        if response_text.startswith("```json"):
            response_text = response_text[7:-3].strip()

        parsed_json = json.loads(response_text)
        return parsed_json

    except Exception as e:
        print(f"Đã xảy ra lỗi khi gọi AI model: {e}")
        return {"intent": "error", "details": str(e)}

# Ví dụ để kiểm tra
if __name__ == '__main__':
    # Nhớ thiết lập GOOGLE_API_KEY trước khi chạy tệp này
    test_command = "Bật cho tôi bài hát hay nhất của Sơn Tùng MTP đi"
    ai_result = get_ai_response(test_command)
    print(f"Lệnh: '{test_command}'")
    print(f"Kết quả phân tích AI: {ai_result}")

    test_command_2 = "kết nối loa gần đây"
    ai_result_2 = get_ai_response(test_command_2)
    print(f"\nLệnh: '{test_command_2}'")
    print(f"Kết quả phân tích AI: {ai_result_2}")
