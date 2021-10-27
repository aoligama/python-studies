monday = int(input('Votes for Monday: '))
tuesday = int(input('Votes for Tuesday: '))
wednesday = int(input('Votes for Wednesday: '))
thursday = int(input('Votes for Thursday: '))
friday = int(input('Votes for Friday: '))

if monday > tuesday and monday > wednesday and monday > thursday and monday > friday:
    print('Monday is the chosen day for lives!')
elif tuesday > monday and tuesday > wednesday and tuesday > thursday and tuesday > friday:
    print('Tuesday is the chosen day for lives!')
elif wednesday > monday and wednesday > tuesday and wednesday > thursday and wednesday > friday:
    print('Wednesday is the chosen day for lives!')
elif thursday > monday and thursday > tuesday and thursday > wednesday and thursday > friday:
    print('Thursday is the chosen day for lives!')
elif friday > monday and friday > tuesday and friday > wednesday and friday > thursday:
    print('Friday is the chosen day for lives!')