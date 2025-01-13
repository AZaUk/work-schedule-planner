work_time = int(input("What time do you need to be at work? \n Enter time in 24h format (05, 08, 14): \n"))
while True:
    if 24 < work_time < 0:
        print("Please enter time in 24h format (05, 08, 14): \n")
        work_time = int(input("What time do you need to be at work? \n Enter time in 24h format (05, 08, 14): \n"))

    else:
        break
transit_time = int(input("How many minutes does it take you to get to work? \n"))
while True:
    if transit_time > (work_time * 60):
        transit_time = int(input("How many minutes does it take you to get to work? \n"))
    else:
        break
early_choice = input("Would you like to arrive at your workplace early? \n y or n: ")
while True:
    if early_choice == "y":
        print("How early would you like to arrive to your workplace?")
        early_time = int(input("In minutes: "))
        break
    elif early_choice == "n":
        early_time = 0
        break
    else:
        print("Please enter y or n!")
        early_choice = input("Would you like to arrive at your workplace early? \n y or n: ")

wake_time = int(input("How much time do you need to wake up and prepare for work? (In minutes): \n"))
while True:
    if wake_time > (work_time * 60):
        wake_time = int(input("How much time do you need to wake up and prepare for work? (In minutes): \n"))
    else:
        break
sleep_time = int(input("Lastly, how many hours of sleep do you desire? (In hours): \n"))

bed_time = (work_time * 60) - (transit_time + early_time + wake_time) - (sleep_time * 60)
wake_up = (work_time * 60) - (transit_time + early_time + wake_time)
leave_by = (work_time * 60) - (transit_time + early_time)
work_arrival = (work_time * 60) - early_time

print("You should arrive at " + str(work_arrival // 60) + ":" + str(work_arrival % 60) + " o'clock")
print("You need to leave house at " + str(leave_by // 60) + ":" + str(leave_by % 60) + " o'clock")
print("You need to wake up at " + str(wake_up // 60) + ":" + str(wake_up % 60) + " o'clock")
if work_time >= 12:
    print("You need to go to bed at " + str(int(bed_time) // 60) + ":" + str(int(bed_time) % 60) + " o'clock")
else:
    bed_time = str(bed_time).replace("-", "")
    import math

    bed_time_hrs = math.floor(24 - int(bed_time) / 60)
    if bed_time_hrs == 24:
        bed_time_hrs = 0
    bed_time = 60 - int(bed_time) % 60
    if bed_time == 60:
        bed_time = 0
    print("You need to go to bed at " + str(bed_time_hrs) + ":" + str(bed_time) + " o'clock")

input("")
