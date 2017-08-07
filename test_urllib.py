from urllib import request
import http.cookiejar

url = "http://www.baidu.com"
print("第一种方法：最简洁的方法")
# 直接请求
response1 = request.urlopen(url)
# 获取状态码
print(response1.getcode())
# 读取内容
print(len(response1.read()))

print("第二种方法：添加data、http header")
# 创建Request对象
req = request.Request(url)
# 添加http的header
req.add_header('user-agent', 'Mozilla/5.0')
# 发送请求获取结果
response2 = request.urlopen(req)
print(response2.getcode())
print(len(response2.read()))

print("第三种方法：添加特殊情景的处理器")
# 创建cookie容器
cj = http.cookiejar.CookieJar()
# 创建一个opener
opener = request.build_opener(request.HTTPCookieProcessor(cj))
# 给request安装opener
request.install_opener(opener)
# 使用带有cookie的request访问网页
response3 = request.urlopen(url)
print(response3.getcode())
print(cj)
print(len(response3.read()))