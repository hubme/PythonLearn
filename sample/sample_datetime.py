from datetime import datetime, timedelta, timezone

# 获取当前时间 2020-05-12 09:45:24.885220
now = datetime.now()
print("当前时间：", now)
print('type(now) =', type(now))
print("获取各字段时间：", now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond)
myTimeStamp = now.timestamp()
print("datetime 转时间戳：", myTimeStamp)
convertDateTime = datetime.fromtimestamp(myTimeStamp)
print("时间戳转 datetime：", convertDateTime)
print('timestamp -> datetime as UTC+0:', datetime.utcfromtimestamp(myTimeStamp))
print("\n")

mytime = datetime(2019, 6, 2, 12, 31)
print("自定义时间：", mytime)
print("\n")

# 字符串转日期
strDate = datetime.strptime('2019-6-2 12:33:09', '%Y-%m-%d %H:%M:%S')
print(strDate)
print("\n")

# 日期对象格式化
print('格式化日期:', strDate.strftime('%a, %b %d %H:%M'))
print("\n")

# 对日期进行操作
print('current datetime =', now)
print('current + 10 hours =', now + timedelta(hours=10))
print('current - 1 day =', now - timedelta(days=1))
print('current + 2.5 days =', now + timedelta(days=2, hours=12))
print("\n")

# 把时间从UTC+0时区转换为UTC+8:
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
utc8_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print('UTC+0:00 now =', utc_dt)
print('UTC+8:00 now =', utc8_dt)
print("\n")