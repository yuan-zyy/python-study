import time

# max()
#
#
# reversed()

# a = 10
# print(type(a))
#
# print(type(type))
#
# a = int('a', base=16)
# print(a)
#
# import time

for i in range(11):
    # \r 让光标回到行首，end="" 阻止换行
    print(f"\r进度: {i*10}%", end="", flush=True)
    time.sleep(0.5)