rows = ["A", "B", "C"]
price = 200
seats = []

for i in range(3):
    row = []
    for j in range(5):
        row.append("_")
    seats.append(row)


def load_bookings():
    try:
        f = open("bookings.txt", "r")
        for line in f:
            line = line.strip()
            if line != "":
                parts = line.split(",")
                code = parts[0]
                name = parts[1]
                r = rows.index(code[0])
                c = int(code[1]) - 1
                seats[r][c] = name
        f.close()
    except FileNotFoundError:
        pass


def save_bookings():
    f = open("bookings.txt", "w")
    for i in range(3):
        for j in range(5):
            if seats[i][j] != "_":
                f.write(rows[i] + str(j + 1) + "," + seats[i][j] + "\n")
    f.close()


def check_seat(code):
    if len(code) != 2:
        return False
    if code[0] not in rows:
        return False
    if code[1] not in "12345":
        return False
    return True


def seats_left():
    count = 0
    for i in range(3):
        for j in range(5):
            if seats[i][j] == "_":
                count = count + 1
    return count


def book_seat():
    text = input("Seat: ").upper()
    text = text.replace(",", " ")
    codes = text.split()
    if len(codes) == 0:
        print("No seat entered.")
        return
    for code in codes:
        if check_seat(code) == False:
            print("Invalid seat. Rows are A to C and seat numbers are 1 to 5.")
            return
        if codes.count(code) > 1:
            print("Seat " + code + " is entered more than once.")
            return
        r = rows.index(code[0])
        c = int(code[1]) - 1
        if seats[r][c] != "_":
            print("Seat " + code + " is already booked.")
            return
    name = input("Name: ").strip()
    if name == "":
        print("Name cannot be empty.")
        return
    for code in codes:
        r = rows.index(code[0])
        c = int(code[1]) - 1
        seats[r][c] = name
    save_bookings()
    amount = len(codes) * price
    if len(codes) == 1:
        print("Seat " + codes[0] + " booked for " + name + ". Amount: " + str(amount))
    else:
        print("Seats " + ", ".join(codes) + " booked for " + name + ". Amount: " + str(amount))
    if seats_left() == 0:
        print("Seats left: 0")
        print("Show is now housefull.")


def cancel_seat():
    code = input("Seat: ").upper().strip()
    if check_seat(code) == False:
        print("Invalid seat. Rows are A to C and seat numbers are 1 to 5.")
        return
    r = rows.index(code[0])
    c = int(code[1]) - 1
    if seats[r][c] == "_":
        print("Seat " + code + " is not booked.")
        return
    name = seats[r][c]
    seats[r][c] = "_"
    save_bookings()
    print("Booking of seat " + code + " for " + name + " cancelled. Refund: " + str(price))


def show_map():
    for i in range(3):
        line = "Row " + rows[i] + ":"
        for j in range(5):
            if seats[i][j] == "_":
                line = line + " _"
            else:
                line = line + " X"
        print(line)
    print("Seats left: " + str(seats_left()))


load_bookings()

while True:
    print()
    print("1 Book")
    print("2 Cancel")
    print("3 Seat map")
    print("4 Exit")
    choice = input("Enter option: ").strip()
    if choice == "1":
        book_seat()
    elif choice == "2":
        cancel_seat()
    elif choice == "3":
        show_map()
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid option. Enter 1, 2, 3 or 4.")
