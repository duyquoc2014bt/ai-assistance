import time

# --- PHẦN GIẢ LẬP ---
# Trong môi trường thực tế, bạn sẽ import thư viện `whisper` và `pyaudio` ở đây.
# import whisper
# import pyaudio
# import wave

def listen_for_command():
    """
    Mô phỏng việc lắng nghe lệnh từ micro.

    Trong phiên bản thực tế, hàm này sẽ:
    1. Ghi âm từ micro.
    2. Lưu tệp âm thanh tạm thời.
    3. Sử dụng Whisper để chuyển đổi âm thanh thành văn bản.
    4. Trả về văn bản đó.
    """
    print("\n[Giả lập] Đang lắng nghe trong 3 giây...")
    time.sleep(3)

    # Giả lập kết quả nhận dạng giọng nói.
    # Bạn có thể thay đổi các lệnh ở đây để kiểm tra các kịch bản khác nhau.
    mock_commands = [
        "mở nhạc giáng sinh",
        "kết nối loa bluetooth",
        "phát nhạc của sơn tùng mtp"
    ]
    import random
    command = random.choice(mock_commands)

    print(f"[Giả lập] Đã nhận diện lệnh: '{command}'")
    return command

# --- PHẦN MÃ THỰC TẾ (ĐÃ ĐƯỢC CHÚ THÍCH) ---
# Dưới đây là ví dụ về cách bạn sẽ triển khai hàm này với Whisper thật.
# Bạn cần bỏ chú thích và cài đặt các thư viện cần thiết để sử dụng.
"""
def record_audio(filename="temp_audio.wav", duration=5, sample_rate=16000, chunk=1024, channels=1):
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16,
                    channels=channels,
                    rate=sample_rate,
                    input=True,
                    frames_per_buffer=chunk)

    print("Bắt đầu ghi âm...")
    frames = []
    for _ in range(0, int(sample_rate / chunk * duration)):
        data = stream.read(chunk)
        frames.append(data)

    print("Kết thúc ghi âm.")
    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(pyaudio.paInt16))
    wf.setframerate(sample_rate)
    wf.writeframes(b''.join(frames))
    wf.close()
    return filename

def transcribe_with_whisper(filename="temp_audio.wav"):
    model = whisper.load_model("base") # "base" là một model nhỏ và nhanh
    result = model.transcribe(filename)
    return result["text"]

def listen_for_command_real():
    audio_file = record_audio()
    transcribed_text = transcribe_with_whisper(audio_file)
    print(f"Whisper đã nhận diện: {transcribed_text}")
    return transcribed_text
"""
