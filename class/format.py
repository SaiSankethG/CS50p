import re
name=input("Whats your name?").strip()
matches=re.search(r"^(.+), (.+)$" , name)
