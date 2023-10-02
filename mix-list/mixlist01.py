#!/user/bin/env python3


# my_list = [ "192.168.0.5", 5060, "UP" ]
# iplist = [ 5060, "80", 55, "10.0.0.1", "10.20.30.1", "ssh" ]

# print("The IP addresses from the list are: " + str(iplist[3]) + " & " +  str(iplist[4]) )
# print("The first item in the list (IP): " + my_list[0] )

# print("The second item in the list (port): " + str(my_list[1]) )

# print("The last item in the list (state): " + my_list[2] )

wordbank= ["indentation", "spaces"]


tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']


wordbank.append(4)

num = int(input("Enter a number between 0 and 20: " ))

student_name = tlgstudents[num]

print(student_name + " always uses " + str(wordbank[-1]) + " " + wordbank[1] + " to indent" )
