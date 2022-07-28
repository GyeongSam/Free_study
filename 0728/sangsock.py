participants =  [3, 7, 100, 21, 13, 6, 5, 7, 5, 6, 3, 13, 21]
rast=0
while True:
    rast=participants.pop(0)
    if rast not in participants:
        print(rast)
        break
    else:
        participants.pop(participants.index(rast))

    


    