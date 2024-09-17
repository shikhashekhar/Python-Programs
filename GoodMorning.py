from datetime import datetime
a=datetime.now()
print(a.hour)

# 5am - 12pm : Morning
#12am - 5pm : Afternoon
#5pm - 9pm : Evening
#9pm - 4am : Night

if(a.hour>5 and a.hour<12):
    print("Good Morning")
elif(a.hour>=12 and a.hour<17):
    print("Good Afternoon")
elif(a.hour>=17 and a.hour<21):
    print("Good Evening")
elif(a.hour>=21 and a.hour<4):
    print("Good Night")
else:
    print("Not a correct time format")
