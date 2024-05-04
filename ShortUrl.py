import pyshorteners
import pyshorteners.shorteners 
a= input("enter Link")
p=pyshorteners.Shortener()
sc=p.tinyurl.short(a)
print(sc)

