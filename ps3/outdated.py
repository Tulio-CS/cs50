months = {
    "January":"01",
    "February":"02",
    "March":"03",
    "April":"04",
    "May":"05",
    "June":"06",
    "July":"07",
    "August":"08",
    "September":"09",
    "October":"10",
    "November":"11",
    "December":"12"
}


def is_valid(day,month):
    if day > 30 or int(month) > 12:
        return False
    else:
        return True

def outdated():
    date = input("Date: ")
    if "/" in date:
        date = date.replace(" ","").split("/")
        if date[0] in months.keys():
            return outdated()
        if is_valid(int(date[1]),int(date[0])):
            if len(date[0]) == 1:
                date[0] = "0"+date[0]
            if len(date[1]) == 1:
                date[1] = "0"+date[1]
            iso = "{}-{}-{}".format(date[2],date[0],date[1])
            return iso
        else:
            outdated()
    else:
        try:
            date = date.split(",")
            date[0] = date[0].split(" ")
            date[1] = date[1].replace(" ","")
            if date[0][1] in months.keys():
                return outdated()
            elif is_valid(int(date[0][1]),months[date[0][0]]):
                if len(date[0][1]) == 1:
                    date[0][1] = "0"+date[0][1]
                iso = "{}-{}-{}".format(date[1],months[date[0][0]],date[0][1])
                return iso
            else:
                outdated()
        except IndexError:
            outdated()


if __name__ == "__main__":
    print(outdated())




