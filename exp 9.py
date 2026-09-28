import re

text="""
hello students!
for any queries, contact abc@gmail.com or teacher123@college.edu.
you can also contact support@yahoo.com.
"""

email_pattern = r'[a-zA-z0,_%+-]+@[a-zA-z0-9,_]+\,[a-zA-Z]{2,}'
emails=re.findall(email_pattern,text)

print("email address found")

for email in emails:
  print(email)
