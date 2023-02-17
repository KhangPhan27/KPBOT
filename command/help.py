from action.sendMessage import sendMessage
from action.seen import seen
def help(sender_id, message):
    seen(sender_id)
    covid = "\n\n/covid  Để xem tình hình covid hôm nay."
    wiki = "\n\n/wiki [từ khóa]  Để tìm định nghĩa trên Wikipedia. Ví dụ: /wiki ChatGPT."
    diche = "\n\n/diche [từ cần dịch]  Trả về văn bản được dịch sang tiếng Việt. Ví dụ: /diche Hello."
    dichv = "\n\n/dichv [từ cần dịch]  Trả về văn bản được dịch sang tiếng Anh. Ví dụ: /dichv Xin chào."
    fact = "\n\n/fact  Random 1 fact."
    sim = "\n\nHoặc nhắn bất kì, Simsimi sẽ rep bạn 😉"
    gpt = "\n\n/gpt [câu hỏi]   Trả lời 1 câu hỏi ngắn. Ví dụ: /gpt xin chào"
    img =  "\n\n/img [từ khóa]   Tìm ảnh thông qua từ khóa banj cung cấp. Ví dụ: /img mèo"
    tik = "\n\n/tik [url video tiktok]  Tải xuống video Tiktok. Ví dụ: /tik https://www.tiktok.com/@example/video/110110101"
    help = f"Chào bạn, bạn có thể sử dụng các câu lệnh sau: {covid}{wiki}{diche}{dichv}{gpt}{img}{fact}{tik}{sim}"
    sendMessage(sender_id,help)
