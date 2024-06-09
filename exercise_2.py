import time
time_stamp=time.strftime('%H:%M:%S')
print(time_stamp)
time_stamp_h=int(time.strftime('%H'))
print(time_stamp_h)
time_stamp_m=int(time.strftime('%M'))
print(time_stamp_m)
time_stamp_s=int(time.strftime("%S"))
print(time_stamp_s)
if(time_stamp_h>=4 and time_stamp_h<12):
    print("good morning")
elif(time_stamp_h>=12 and time_stamp_h <=16):
    print("good afternoon")
else:
    print("good evening")        