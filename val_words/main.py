#Valorant text color editor
message = input("what is the message you wanna say:\n")
array = ["enemy","system","notification","team","warning"]
colors = ["red","yellow","green","blue","purple"]
color = input("type r for red, y for yellow, g for green, b for blue, p for purple, a for all, i for backwards-rainbow:\n")
color = color.lower()
endstring = ""
j = len(message)-1
if(color == "r"):
    print("<"+array[0]+">"+message+"</>")
elif(color == "y"):
    print("<"+array[1]+">"+message+"</>")
elif (color == "g"):
    print("<" + array[2] + ">" + message + "</>")
elif (color == "b"):
    print("<" + array[3] + ">" + message + "</>")
elif(color == "p"):
    print("<"+array[4]+">"+message+"</>")
elif(color == "a"):
    for i in range(len(message)):
        endstring += "<"+array[i%5]+">"+message[i:i+1]+"</>"
    print(endstring)
elif(color == "i"):
    while j > -1:
        endstring +="<"+array[(j)%5]+">"+message[j:j+1]+"</>"
        j-=1
    print(endstring)