def look_and_say(num):
    repeat = num[0]
    times = 1
    num = num[1:] + " "

    result = ""
    for next in num:
        if next!=repeat:
            result+=str(times)+repeat
            repeat = next
            times =1
        else:
            times+=1

    return result

num = "1"
print num
for i in range(5):
    num = look_and_say(num)
    print num
