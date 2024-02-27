
def main():
    file = input("File name: ").lower().replace(" ","")
    if file[-4:] == ".gif":
        return "image/gif"
    elif file[-4:] == ".jpg":
        return "image/jpeg"
    elif file[-5:] == ".jpeg":
        return "image/jpeg"
    elif file[-4:] == ".png":
        return "image/png"
    elif file[-4:] == ".pdf":
        return "application/pdf"
    elif file[-4:] == ".txt":
        return "text/plain"
    elif file[-4:] == ".zip":
        return "application/zip"
    else:
        return "application/octet-stream"

print(main())

