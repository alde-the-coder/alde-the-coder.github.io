import random, os, string
link = input("link\n")
if "http://" not in link:
    link = "http://" + link
letters = string.ascii_letters
while True:
    name = ''.join(random.choice(letters) for i in range(6))
    listofnames= os.listdir(path=".")
    if name in listofnames:
	    continue
    else:
	    break
os.mkdir(name)
with open("template1", "r") as template1file:
    template1 = template1file.read()
with open("template2", "r") as template2file:
    template2 = template2file.read()
with open(name+"/index.html", "w") as indexfile:
    indexfile.write(template1)
    indexfile.write(link)
    indexfile.write(template2)
