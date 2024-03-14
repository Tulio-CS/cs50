
def main():
    file = input("File name: ").lower().replace(" ","")
    extensions = {".gif":"image/gif",".jpg":"image/jpeg",".jpeg":"image/jpeg",".png":"image/png",".pdf":"application/pdf",".txt":"text/plain",".zip":"application/zip"}
    for key,items in extensions.items():
        if key in file:
            return items
    return "application/octet-stream"

if __name__ == "__main__":
    print(main())

