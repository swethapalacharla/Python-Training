'''
Distance Travled
'''


TotalDis = 10_000
Hr1Day = int(input("enter no of hours bicycled in 1 day"))
Dis1Hr = int(input("distance travelled in one  of hours"))

Dis1Day = Hr1Day * Dis1Hr
TDays = int(TotalDis/Dis1Day)
TMonths = int(TDays/30)
TYears = (TDays/365)
THrs = TDays * Hr1Day

print('TotalNoOfDays', TDays)
print('TotalNoOfMonths', TMonths)
print('TotalNoOfYears', TYears)
print('TotalNoOfHours', THrs)
