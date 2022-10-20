import logging

def create_file():
    try:
        file1=open("APIKEY.txt","r")
        logging.info("APIKEY.txt was found opening file and returning APIKEY")
        return file1.readline()
    except:
        key=input("No file detected: please input API key if you are unsure of how to generate API key press 1 for more info\n")
        if key.isnumeric():
            print("In order to generate API key for canvas log into canvas and navigate to account and then settings.")
            print("Once in settings navigate to 'Approved Integrations' you should just need to scroll down.")
            print("Click on the new access token and enter in a purpose and expiration to move onto the next page. When on the next page copy the text next to 'Token'")
            key=input("Paste the key here to store API Key")
            file1=open("APIKEY.txt","w")
            file1.write(key)
            file1.close()
            file1=open("APIKEY.txt","r")
            return file1.readline()
        else:  
            file1=open("APIKEY.txt","w")
            file1.write(key)
            file1.close()
            file1=open("APIKEY.txt","w")
            return file1.readline()
            
            


