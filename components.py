# CLASSES AND METHODS
class Person():
    

    def __init__(self, name, bio, age):
        # your code goes here!
        self.name = name
        self.bio = bio
        self.age = age
        # self.members = []
        # self.president = []

class Club():
    def __init__(self, name, description):
        # your code goes here!
        self.name = name
        self.description = description
        # persons = Person()
        self.members = []
        self.president = ""
    

    def assign_president(self, person):
        # your code goes here!
        self.president = person
        


    def recruit_member(self, person):
        # your code goes here!
          self.members.append(person)
    


    def print_member_list(self):
        # your code goes here!
        # for num, item in enumerate(self.members):
        #     print(num+1, item)
        #     print()
        print("Memebers:")
        for member in self.members:
            if member is self.president:
                print("%s (%s years old, president) - %s" % (member.name,str(member.age),member.bio))
            else:
                print("%s (%s years old) - %s" % (member.name,str(member.age),member.bio))
           
            
