# Lesson 3:

#Reading a file:

##with open ("states.txt","r")as states_file:
##    states = states_file.read()
##print states 

#Creating a list from the file, rather than a string:

##with open ("states.txt","r")as states_file:
##    states = states_file.read().split("\n")
##print states 

#Working with a CSV file, creating lists within lists, rather than strings:

##with open ("states.csv","r") as states_file:
##    states = states_file.read().split("\n") 
##
##    for index, state in enumerate(states):
##        states[index] = state.split(",")
##    print states

##Creating two separate lists from a cSV:
##
##with open ("states.csv","r") as states_file:
##    states = states_file.read().split("\n")
##
##    for index, state in enumerate(states):
##       states[index] = state.split(",")
##       state_abbrs.append(states[index][0]) 
##
##state_abbrs = []
##state_names= []
##
##for state in states:
##    state_abbrs.append(state[0])
##    state_names.append(state[1])
##print state_abbrs
##print state_names


#Write to new file: LOOK ON GIT HUB FOR THE INFO, GOT LOST HERE: 

##with open ("states.html","w") as new_file:
##    new_file.write(states_option_list) 
##
##state_option_list = ""
##state_option_list +=

#Dictionaries:
#dictionary = {}

##contacts ={"Shannon":"202-555-1234","Bridgit":"703-555-1222","Alison":"315-555-1111"}
##print contacts["Shannon"]
##contacts["Kristen"]="301-333-1212" #Adding to the dictionary
##print contacts 
##print contacts.get("Frankenstien") #Get method, like find, does not produce an error message
##print contacts.get("Frankenstein","This lets you set the message that you will receive when the key returns none")
##
##attendees = {"Oct 29" : ["Emily","Erika","Joanne"],"Nov 29":["Jenna","Elizabeth"],"Sept 18":["Andrea","Casey","Hannah"]}
##print attendees["Oct 29"]


#Dictionary within a dictionary:

contacts = {
    "Shannon": {"Phone":"202-555-1234","twitter":"@shannon01","Github":"shannonturner"},
    "Bridgit" : {"Phone":"703-555-1222","twitter":"@bri","Github":"bri"},
    "Allison":{"Phone": "315-555-1111","twitter":"@alison","Github":"Allison"}
}
##
##for contact in contacts.keys():
##    print contact
##    print contacts.get(contact).get("Phone")
##    print contacts.get(contact)["Phone"]
##
##for contact in sorted(contacts.keys()):
##    print contact
##
##for info in contacts.values():
##    print info
##
##for contact,info in contacts.items():
##    print contact,"--", info


for contact,info in contacts.items():
    print contact+"'s contact information is:"
    print "\tPhone: "+contacts.get(contact)["Phone"]
    print "\tTwitter: "+contacts.get(contact)["twitter"]
    print "\tGitHub: "+contacts.get(contact)["Github"]
    


























        
    
