'''
String reverse
'''
ActualStr = 'India defeated england and spain defeated france'
Rstring = ' '.join(reversed(ActualStr.split()))
Fstring = Rstring.replace("defeated", "lost to")
print(Fstring)

