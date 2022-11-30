import re

url=input("URL:").strip()

name=re.sub(r"https://twitter.com/" , "" , url)
print(f"Name:{name}")