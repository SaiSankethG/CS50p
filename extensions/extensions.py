name=input("File name:")
new_name=name.lower()
if '.gif' in new_name:
    print("image/gif")
elif '.png' in new_name:
    print("image/png")
elif '.jpg' in new_name:
    print("image/jpedg")
elif '.jpeg' in new_name:
    print("image/jpeg")
elif '.pdf' in new_name:
    print("application/type")
elif '.zip' in new_name:
    print("application/type")
elif '.txt' in new_name:
    print("text/plain")
else:
    print("application/octet-stream")