import re
name=input("Whats your name?").strip()
re.search(r"^.+, .+$" , name)