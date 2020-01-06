#Author : Mary Princy. Edward
#This script is meant for conforming, security misconfiguration
import requests

Clickjacking = 0

XSS_filtering = 0

Content_Security = 0

Sniffing_Protection = 0

tmp = input("Enter the Domain name to scan :  ")

url = "http://"+tmp

res = requests.get(url)

for num in res.headers:
	
	num = num.lower()
  
	if num == "x-frame-options":
  
		print("Clickjacking protection = Enabled")
    
		Clickjacking += 1
    
	elif num == "X-XSS-Protection":
  
		print("XSS filtering = Enabled")
    
		XSS_filtering += 1
    
	elif num == "Content-Security-Policy":
  
		print("Content Security Policy = Enabled")
    
		Content_Security += 1
    
	elif num == "X-Content-Type-Options":
  
		print("Sniffing Protection : Enabled")
    
		Sniffing_Protection += 1
    
	elif num == "location":
  
		print("Check Open Redirection Attack")
		
if Clickjacking == 0:

	print("Clickjacking protection = Not Enabled")
  
if XSS_filtering == 0:

	print("XSS filtering = Not Enabled")
  
if Content_Security == 0:

	print("Content Security Policy = Not Enabled")
  
if Sniffing_Protection == 0:

	print("Sniffing Protection : Not Enabled")
