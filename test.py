#Get the name of the files from the directory
from os import listdir
#Open the file to writen to
output = open('D:\\CBL-website\\output.txt', "a")

#Loop to get all the years
for year in range (1990, 1996):
    #title of each year
    yearHeader = (f"--------------------------------{year}-----------------------\n\n\n\n\n\n\n\n")
    output.write(yearHeader)
    #Specifie the directory of the current year from the above loop
    directory = f"D:\\CBL-website\\grad-pictures\\{year}"
    #loop through each file
    for file in listdir (directory):
        # Get the initial
        initial = file[0]
        #Handle the issue of "-" and "_" between first and last name
        if file.count("-") == 0:
            hyphen = file.index("_")
        else:
            hyphen = file.index("-")
        # Get and capitalize first initial
        initial = file[hyphen+1].capitalize()
         # Get and capitalize last name
        lname = file[0: hyphen].capitalize()
        
        
        #OUtputing the HTML code
        output.write('<div class="pictures"> \n' )
        string1 = f'<img src="../grad-pictures/{year}/{file}" alt="{initial}. {lname}" width="146px" height="auto"> \n'
        output.write(string1)
        output.write('<div class="overlay">\n')
        output.write('<h2>Preview</br>Image</h2>\n')
        output.write('</div>\n')
        string2 = f"<h3>{initial}. {lname}</h3> \n"
        output.write(string2)   
        output.write("</div>\n")