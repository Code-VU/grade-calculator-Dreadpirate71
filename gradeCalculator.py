def calculateGrade():
    # Implement your solution in between the two comment blocks
    print("Calculating Grade")
    # This first line is provided for you

    grade = input("Enter score:")
    try:
        float(grade)
        if float(grade) > 1.0 or float(grade) < 0.0:
            print ('Bad score')
        elif float(grade) >= 0.9:
            print ('A')
        elif float(grade) >= 0.8 and float(grade) < 0.9:
            print ('B')
        elif float(grade) >= 0.7 and float(grade) < 0.8:
            print ('C')
        elif float(grade) >= 0.6 and float(grade) < 0.7:
            print ('D')
        elif float(grade) < 0.6:
            print ('F')
    except:
        print ('Bad score')

    # end assignment

## if you want to test locally before you try to sync
## uncomment calculateGrade() and run > python calculateGrade.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
##calculateGrade()