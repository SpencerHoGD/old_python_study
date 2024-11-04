from datetime import date

now = date.today()
print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))


birthday = date(1990, 12, 16)
age = now - birthday
print(age.days)


from timeit import Timer


print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())
print(Timer('a,b = b,a', 'a=1; b=2').timeit())