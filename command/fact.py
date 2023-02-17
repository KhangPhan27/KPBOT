from action.sendMessage import sendMessage
import random
from action.seen import seen
def fact(sender_id, message):
    seen(sender_id)
    facts = [
                "Châu Phi là lục địa duy nhất nằm trên cả 4 bán cầu và cũng là lục địa duy nhất có cả Xích đạo và Kinh tuyến gốc chạy qua.",
                "Canada là nhà của hơn một nửa số hồ tự nhiên trên thế giới, với tổng cộng 31.752 hồ, Ngoài ra 9% diện tích Canada được che phủ bởi nguồn nước ngọt.",
                "Trung Quốc có chung đường biên giới với 14 nước: Ấn Độ, Pakistan, Afghanistan, Myanmar, Nepal, Bhutan, Lào, Kyrgyzstan, Kazakhstan, Tajikistan, Nga, Việt Nam, Mông Cổ và Triều Tiên.",
                "Alaska là bang cực bắc, cực đông và cực tây của nước Mỹ.",
                "Về mặt kỹ thuật, ngọn núi cao nhất thế giới là Mauna Kea ở Hawaii, chứ không phải Đỉnh Everest. Điều này là bởi Everest cao 8.850 mét so với mặt nước biển, trong khi đỉnh cao nhất của Mauna Kea chỉ cao 4.205 mét so với mặt nước biển. Tuy nhiên, Mauna Kea còn khoảng 6.000 mét chìm bên dưới mặt nước biển và tổng chiều cao của nó là 10.210 mét.",
                "Vatican là đất nước nhỏ nhất thế giới với diện tích chỉ 0,44 km vuông.",
                "Hòn đảo Nauru ở Thái Bình Dương là quốc gia duy nhất không có thủ đô chính thức. Quốc kỳ Nauru thể hiện vị trí của hòn đảo này. Đường ngang màu vàng tượng trưng cho Xích đạo và ngôi sao màu trắng bên dưới là Nauru.",
                "Saudi Arabia không có bất cứ con sông, hồ nước hay thác nước nào. Quốc gia này phụ thuộc vào nguồn nước ngầm và các loại cây khử muối để lấy nước sinh hoạt.",
                "Quốc gia Trung Đông duy nhất không có sa mạc là Lebanon.",
                "Quốc gia có đường bờ biển lớn nhất thế giới là Canada, với đường bờ biển trải dài 202.080km.",
                "Thành phố Istanbul của Thổ Nhĩ Kỳ nằm trên 2 lục địa: châu Âu và châu Á.",
                "Australia rộng hơn cả Mặt Trăng. Mặt trăng có bán kính 3.476,28km, trong khi Australia từ đông sang Tây trải dài 4,000km.",
                "Ngọn núi gần không gian vũ trụ nhất không phải đỉnh Everest mà là đỉnh Chimbozaro ở Ecuador. Dù Chimbozaro chỉ cao 6.263m, còn Everest cao 8.850m, nhưng Chimbozaro vươn xa hơn vào vũ trụ do nằm ở vị trí Xích Đạo.",
                "Biển Sargasso là biển duy nhất trên thế giới không có bờ. Thay vào đó, nó được xác định bởi 4 dòng chảy đại dương nằm trong dòng Hoàn lưu Cận nhiệt đới: Dòng Vịnh Gulf Stream, dòng Bắc Đại Tây Dương, dòng Canary và dòng xích đạo Bắc Đại Tây Dương.",
                "Sa mạc lớn nhất thế giới không phải Sahara mà là Sa mạc Nam cực với diện tích 14.244.934,6 km vuông.",
                "Khoảng 99% băng nước ngọt trên Trái Đất nằm ở các phiến băng Nam Cực và Greenland.",
                'Theo Sách Kỷ lục Guinness Thế giới, nhiệt độ cao nhất khi nhận được trên Trái Đất là 56,7 độ C. Mức nhiệt này ghi nhận được ở Greenland Ranch, Thung lũng Chết, California vào ngày 10/7/1913.',
                "Khi chúng ta nhìn lên những ngôi sao trên trời, chúng ta thực ra đang nhìn về quá khứ bởi chúng ở cách Trái Đất hàng triệu năm ánh sáng.",
                "Kính thiên văn Hubble có khả năng quan sát chi tiết tới nỗi nó thể chụp được một con ruồi đang bay ở khoảng cách hơn 20.000 km.",
                "Khác với vẻ đẹp tròn trịa mà mọi người thường lầm tưởng khi quan sát Mặt TTrăng từ Trái Đất, vệ tinh này thực chất có hình dạng không đối xứng và trông giống như một quả chanh (hoặc quả trứng).",
                'Vi khuẩn lam (Cyanobacteria) là những sinh vật "thở" bằng sự quang hợp, chúng hít khí carbon dioxide và thải ra khí oxy, giống như loài thực vật. Cyanobacteria được xem là loài sinh vật đầu tiên tạo ra oxy trên Trái Đất. Điều này được xem như một Sự kiện Oxy hóa vĩ đại trong lịch sử.',
                "Quá ít oxy cũng nguy hiểm mà quá nhiều oxy cũng nguy hiểm. Nếu chúng ta hít thở 80% oxy trong hơn 12 giờ sẽ gây kích thích đường hô hấp, và cuối cùng là có thể bị tràn dịch, hoặc phù nề.",
                "Chúng ta phải cám ơn vì bầu khí quyền có nồng độ 21% oxy. Khoảng 300 triệu năm trước, nồng độ oxy đạt 35%, các loài côn trùng có thể phát triển siêu lớn: hãy tưởng tượng thế giới sẽ ra sao nếu loài chuồn chuồn có sải cánh rộng bằng diều hâu!",
                'Nghĩ đến nguồn cung cấp oxi hầu hết mọi người sẽ nghĩ ngay đến khu rừng mưa nhiệt đới Amazon với hệ thực vật phong phú -, Nhưng thực tế là rừng Amazon chỉ là nguồn cung cấp của khoảng 20% lượng oxy trên Trái Đất. Ồ khoan! Chỉ 20% thôi ư, vậy số còn lại đến từ đâu???\nNGUỒN OXY DỒI DÀO NHẤT ĐÓ LÀ ĐẠI DƯƠNG!\nChính xác hơn là từ các thực vật phù du (phytoplankton/algea) ở khắp các đại dương. Chúng cung cấp khoảng 50 - 85% oxy cho hệ khí quyển trên Trái Đất (khoảng 330 tỷ tấn oxy/năm). Thực vật phù du sống nhờ vào quá trình quang hợp: Chúng sử dụng năng lượng từ mặt trời và các dưỡng chất từ nước (được hấp thụ qua thành tế bào) để thực hiện quá trình quang hợp - cung cấp năng lượng cho chính chúng, đồng thời tạo ra oxy.',
                "Nếu Mặt Trời có kích thước của một tế bào bạch cầu trong máu, thì dải Ngân hà của chúng ta có kích thước tương đương với cả nước Mỹ.",
                "Có nhiều ngôi sao trong vũ trụ hơn số hạt cát có trên tất cả các bãi biển của thế giới.",
                "Một con bạch tuộc có tới 3 quả tim",
                "Số lượng vi khuẩn trong cơ thể của chúng ta nhiều gấp 10 lần số lượng các tế bào",
            ]
    sendMessage(sender_id, random.choice(facts))