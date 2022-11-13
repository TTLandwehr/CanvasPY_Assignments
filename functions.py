import logging

def create_file():
    print("in function")
    try:
        file1=open("APIKEY.txt","r")
        print("APIKEY.txt was found opening file and returning APIKEY")
        return file1.readline()
    except:
        key=input("No file detected: please input API key if you are unsure of how to generate API key press 1 for more info\n")
        if key.isnumeric():
            print("First past your school's Canvas URL\n")
            url=input()
            file1=("APIKEY.txt","w")
            file1.write(url)
            file1.close()
            print("In order to generate API key for canvas log into canvas and navigate to account and then settings.")
            print("Once in settings navigate to 'Approved Integrations' you should just need to scroll down.")
            print("Click on the new access token and enter in a purpose and expiration to move onto the next page. When on the next page copy the text next to 'Token'")
            key=input("Please paste API key now\n")
            file1=open("APIKEY.txt","w")
            file1.write(key)
        else:
            print("First past your school's Canvas URL\n")
            url=input()
            file1=("APIKEY.txt","w")
            file1.write(url)
            key=input("Please paste API key now\n")
            file1.close()
            file1.open("APIKEY.txt","r")


            
            


