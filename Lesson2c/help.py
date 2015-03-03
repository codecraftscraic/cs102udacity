user_file = open("help.txt", "a")

user_input = raw_input("Say something! ")

input_to_file = ("User says: "+user_input+"\n")

user_file.write(input_to_file)

user_file.close()
