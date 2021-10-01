n = int(input())
sec = n % 60
minutes = (n // 60) % 60
hours = (n // 3600) % 24
if sec < 10:
    sec = "0" + str(sec)
if minutes < 10:
    minutes = "0" + str(minutes)
if hours < 10:
    hours = "0" + str(hours)
print(hours, minutes, sec, sep=":")