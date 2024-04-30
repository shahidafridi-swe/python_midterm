
class Star_Cinema:
    hall_list = []

    def entry_hall(self, rows,cols,hall_no):
        hall = Hall(rows,cols,hall_no)
        self.hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self,  rows, cols, hall_no) -> None:
        self.__seats = {}
        self.__show_list = []
        self.__rows = rows
        self.__cols = cols
        self.hall_no = hall_no

    def entry_show(self, id, movie_name, time):
        show = (id, movie_name,time)
        self.__show_list.append(show)
        seats = []
        for i in range(self.__rows):
            seats.append([])
            for j in range(self.__cols):
                seats[i].append(0)
        self.__seats[id] = seats
    
    def book_seats(self, id):
        isShow =False
        for key, value in self.__seats.items():
            if id == key:
                isShow = True
        if not isShow:
            print(f"Sorry {id} show is not available")
        else:
            try:
                quantity = int(input("How many ticket do you want to book: "))
                if 0 < quantity <=self.__rows*self.__cols:
                    try:
                        for i in range(quantity):
                            print(f"\n------------ No: {i+1} ------------")


                            row = int(input("Enter the row: "))
                            col = int(input("Enter the column: "))
                            if 0 < row <= self.__rows and 0 < col <= self.__cols:
                                if self.__seats[id][row-1][col-1] != 1:
                                    self.__seats[id][row-1][col-1] = 1
                                    print(f"Your selected seat (Row: {row}, Column: {col}) has booked successfully!")

                                else:
                                    print(f"Your selected seat (Row: {row}, Column: {col}) is already booked. Please Try Another One.")
                            else:
                                print(f"Please enter the value of row between: 1-{self.__rows} and column between: 1-{self.__cols}")
                    except ValueError:
                        print("Please enter the numeric value for row and column")
                else:
                    print(f"Please enter the ticket quantity between 1-{self.__rows*self.__cols}")
            except ValueError:
                print("Please enter the numeric value for how many ticket you want")
    
        

    def view_show_list(self):
        print("\nThe show list:")
        for show in self.__show_list:
            print(show)
    
    def view_available_seats(self,id):
        isShow = False
        for key, value in self.__seats.items():
            if key ==id:
                isShow = True
                print(f"\nThe available seat of ID: {id}")
                for r in value:
                    print(r)
        if not isShow:
            print(f"\nSorry !!! There are no show of ID: {id}, Try Again")


  

cineComplex = Hall(7,7,420)
cineComplex.entry_show('111',"3idiots", "7pm")
cineComplex.entry_show('333',"Aynabaji", "7pm")


print("\n------- Welcome to cineComplex -------")
while True:
    
    print("\nOptions:")
    print("------------------------------------------")

    print("\t1. VIEW ALL SHOW TODAY")
    print("\t2. VIEW AVAILABLE SEATS")
    print("\t3. BOOK TICKET")
    print("\t4. EXIT")

    op = input("Enter Option: ")

    if op == '1':
        cineComplex.view_show_list()
        
    elif op =='2':
        id = input("Enter the show ID: ")
        cineComplex.view_available_seats(id)
    elif op == '3':
        id = input("Enter the show ID: ")
        cineComplex.book_seats(id)
    elif op == '4':
        break
    else:
        print("\n!!! Please enter the correct option (1/2/3/4) !!!")
    