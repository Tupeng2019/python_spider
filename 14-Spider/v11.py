from urllib import request

if __name__ == '__main__':

    url = "http://www.renren.com/965187997/profile"

    rsp = request.urlopen(url)
    # 这就是保存文件的操作
    html = rsp.read().decode()

    with open("rsp.html", "w") as f:
        f.write(html)