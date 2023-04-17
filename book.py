import csv
import operator


book = "THE C PROGRAMMING "
getcmd = "HELLO"
getrating = 5
command = ""
rating = 0
with open("books.csv") as login_info:
    read = csv.reader(login_info)
    data = list(read)
    change = 0
    index = 0
    print("HI",data)
    for i in data:
        print(i[8],book.lower())
        if book.lower() in i[1].lower() :
            change = 1
            command = i[7]
            cmd = command.split("|||")
            if not i[5]:
                i[5]=0
            rating = i[5]
            command += "|||" + getcmd
            if not i[8]:
                i[8]=0
            rating = int(rating) * int(i[8]) + getrating
            i[8] = int(i[8])+ 1
            data[index][7] = command
            data[index][5] = rating
            data[index][8] = i[8] + 1
            index += 1
if change == 0:
    print({"message": "fail"})
with open("books.csv", 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
    print({"message": "success"})