# UTILS AND FUNCTIONALITY
from data import  population, clubs
from components import Club, Person

my_name = "Alaa"
my_age = 25
my_bio = "Computer Engineer"
myself = Person(my_name, my_bio, my_age)

def introduction():
    print("Hello, %s. Welcome to our portal." % my_name)
    options()

def options():
    # your code goes here!
   
    print( "Would you like to:")
    print( "1) Create new club. \n or:\n")
    print( "2) Browse and join clubs \n or:\n")
    print( "3) View existing clubs \n or:\n")
    print( "4) Display members of a club \n or:\n")
    print( "-1) Close application \n")
    
    option = input("Enter number: ")
    
    if option == "1":
       create_club()
    elif option == "2":
       join_clubs()
    elif option == "3":
       view_clubs()
    elif option == "4":
       view_club_members()
    elif option == "-1":
       exit()
          



    

def create_club():
    # your code goes here!
    name = input("Pick a name for your new club: ")
    print()
    description = input("What is your club about ? ")
    club = Club(name,description)
    print()
    print("Enter the number of people you would like to recruit to your new club or -1 to stop: \n------------------------------------------------")
    print()
    counter = 1
    for p in population:
        print("[ %d ] %s \n" % (counter,p.name))
        counter+=1

    print()
    club.assign_president(myself)
    club.recruit_member(myself)
    member = input()
    avergae = 0
    count = 0
    while member != "-1":
        club.recruit_member(population[int(member)-1])
        avergae = avergae + population[int(member)-1].age
        count+=1
        member = input()

    print()
    print("Here's your club:")
    print(club.name+"\n"+club.description+"\n")
    club.print_member_list()
    print()
    print("The average age in this club: %s years old" % (int(avergae/count)))
    print()

    

def view_clubs():
    # your code goes here!
    print()
    for club_object in clubs:
           print("\tName: %s\n\tDescription: %s\n\tMembers: %s" %(club_object.name,club_object.description,str(len(club_object.members))))
           print()
    
    

def view_club_members():
    # your code goes here!
    
    view_clubs()
    c_name = input("Enter the name of the club whose members you'd like to see: ")
    result = "False"
    
    for club_object in clubs:
        if c_name == club_object.name:
            print()
            club_object.print_member_list()
            result = "True"
            break
    
    if result == "False":
       print("Club does not exsist..Please enter the name again")
       view_club_members()

    
    

    

def join_clubs():
    # your code goes here!

    view_clubs()
    join_club = input("Enter the name of the club you would like to join: ")
    print()
    result = "False"
    
    for club_object in clubs:
        if join_club == club_object.name:
                club_object.recruit_member(myself)
                print(my_name+" just joined "+club_object.name+"\n------------------------------")
                print()
                result = "True"
                break

    if result == "False":
        print("Club does not exsist..Please enter the name again") 
        join_clubs()
    
    
    

def application():
    introduction()
    # your code goes here!
    
