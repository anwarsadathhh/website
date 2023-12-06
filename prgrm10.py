y1= int(input("Enter the starting year: "))
y2= int(input("Enter the ending year: "))
if y1 >y2:
    print("end year must must be greater than or equal to the start year.")
else:
    print(f"Leap years from{y1} to {y2}")
    for year in range(y1,y2+1):
        if(year%4==0and year%100!=0)or(year%400==0):
           print  (year)
