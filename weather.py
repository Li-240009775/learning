import requests
from bs4 import BeautifulSoup

# 以“天气网”为例（你也可以换成其他公开API）
url = "https://tianqi.2345.com/wea_fenlei/"

# 
头信息 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}

响应 = requests.get(url, headers=头信息)
if 响应.status_code == 200:
    soup = BeautifulSoup(响应.text, "html.parser")
    # 找到温度元素（需要根据实际网页调整选择器）
    温度标签 = soup.find("div", class_="temp")  # 示例class
    if 温度标签:
        print(f"当前温度：{温度标签.text}")
    else:
        print("未找到温度数据，需要调整选择器")
else:
    print("请求失败")
