

def kasiski(file):
    text = open(file, "r")
    
    keys = dict()
    
    # Loop through each line of the file
    for line in text:
        words = line.split(" ")
                            
        for word in words:
            if word in keys:
                keys[word] = keys[word] + 1
            else:
                keys[word] = 1
  
    for key in list(keys.keys()):
        print(key, ":", keys[key])