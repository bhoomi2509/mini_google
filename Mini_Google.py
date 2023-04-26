import json
from difflib import get_close_matches
import time

content = json.load(open("wordbook.json"))

def getmeaning(user_input):
    if user_input.lower() in content:
        return content[user_input.lower()]
    elif user_input.upper() in content:
        return  content[user_input.upper()]
    elif user_input.title() in content:
        return  content[user_input.title()]
    elif user_input.upper() in content:
        return  content[user_input]
    elif len(get_close_matches(user_input , content.keys())[0]) > 0:
        closematches=(get_close_matches(user_input , content.keys())[0])
        user_decesion=input("Did You Mean %s ?[Y/N]" % closematches)

        if user_decesion.lower()=='y':
            return(content[closematches])
        elif user_decesion.lower()=='n':
            return ("Sorry..! Please check For spelling Mistake And try again..! ")
        else:
            print("Please Provide Proper output")
            exit()
    else:
        print("Sorry..! Please check For spelling Mistake And try again..! ")



def call_me():
    user_input=input("Enter The Word Which You Want To Search:")
    output=getmeaning(user_input)
    if type(output)==list:
        for i in output:
            print(i)
            time.sleep(1)
            yes_no = input("Do you want to continue..?[Y/N]")
            if yes_no.lower() == 'y':
                call_me()
            elif yes_no.lower() == 'n':
                print("See You again Next Time...Bye..!!")
                exit()
            else:
                print("You had not given proper output..Bye..!!!!")
                exit()
    else:
        print(output)
        call_me()
call_me()








