import random
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Token của bot Telegram
TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"

# Hàm xử lý lệnh /roll
def roll(update: Update, context: CallbackContext) -> None:
    # Lặp 3 lần để ném xúc xắc
    for i in range(3):
        # Tạo một con xúc xắc ngẫu nhiên từ 1 đến 6
        dice_result = random.randint(1, 6)
        # Gửi kết quả về cho người dùng
        update.message.reply_text(f"Phiên {i+1}: Bạn được {dice_result}!")

def main() -> None:
    # Khởi tạo updater với token của bot Telegram
    updater = Updater(TOKEN)
    # Lấy dispatcher để xử lý các lệnh và thông điệp
    dispatcher = updater.dispatcher
    # Đăng ký xử lý lệnh /roll
    dispatcher.add_handler(CommandHandler("roll", roll))
    # Bắt đầu chạy bot
    updater.start_polling()
    # Dừng lại khi nhấn Ctrl+C
    updater.idle()

if __name__ == '__main__':
    main()
