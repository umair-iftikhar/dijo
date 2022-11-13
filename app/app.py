import dijo


def dj(): 
    
    entry = input('DIJO>>')

    if entry[0] == "0":
        print("Thanks for using Dijo")
    elif entry[0].lower() == "g":
        print("\nGuide: T = Task, E = Event/Meeting, N = Notes, D = Decision")
        print("       ! = Important Task, @projectName, 0 for exit\n")
        dj()
    else:
        if dijo.validate_entry(entry):
            dijo.new_entry(dijo.create_entry(entry))
        else:
            print("Invalid Entry, please try again.")
        dj()
    

dj()
