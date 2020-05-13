from urllib import request, parse


with request.urlopen("https://docs.python.org/zh-cn/3/library/urllib.request.html?highlight=urllib") as f:
    data = f.read()
    print("status: ", f.status, f.reason)
    for k, v in f.getheaders():
        print("%s : %s" % (k, v))
    print("result: ", data.decode("utf-8"))
print("\n")


req = request.Request('http://www.baidu.com/')
req.add_header('User-Agent', 'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
values = {'name': 'Michael Foord',
          'location': 'Northampton', 'language': 'Python'}
with request.urlopen(req, parse.urlencode(values).encode("utf-8")) as f:
    print('Status:', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))
