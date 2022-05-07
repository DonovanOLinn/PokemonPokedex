from subprocess import call


class Basketball_UI:


    def __init__(self):
        pass

    def find_info():
        data = apicall

        firstname = data[firstname]
        secondname = data[secondname]
        team = data[team]
        position = data[position]


        Player_firstway(firstname, secondname, team, position)
        Player_secondway(data)


class Player_firstway:
    def __init__(self, firstname, secondname, team, position):
        self.firstname = firstname
        self.secondname = secondname
        
        
        
        pass


class Player_secondway:
    def __init__(self, data):
        self.firstname = data[firstname]
        self.secondname = data[secondname]
        



if data.status_code == 200:
    data = data.json()
else:
    print(data.status_code)
    print("ERROR ERROR ERROR, much like Lugia, the pokemon you entered does not exist. Check your spelling and try again")