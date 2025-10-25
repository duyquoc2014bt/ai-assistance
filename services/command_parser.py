def parse_command(command: str) -> dict:
    """
    Phân tích lệnh văn bản đơn giản để xác định ý định và chi tiết.
    """
    command_lower = command.lower()

    # Từ khóa cho việc phát nhạc
    music_keywords = ["phát nhạc", "mở nhạc", "play music"]
    for keyword in music_keywords:
        if keyword in command_lower:
            # Lấy phần văn bản sau từ khóa làm truy vấn tìm kiếm
            query = command_lower.replace(keyword, "").strip()
            return {"intent": "play_music", "details": query}

    # Từ khóa cho việc kết nối Bluetooth
    bluetooth_keywords = ["kết nối loa", "connect speaker", "kết nối bluetooth"]
    for keyword in bluetooth_keywords:
        if keyword in command_lower:
            # Lệnh này không cần chi tiết thêm
            return {"intent": "connect_bluetooth", "details": None}

    # Nếu không có từ khóa nào khớp
    return {"intent": "unknown", "details": command}
