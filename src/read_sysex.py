# Hard coded stuff playting around with a single sysex file.
# Can we read and parse the sysex-file?

# Opening the binary file in binary mode as rb(read binary)
f = open("../patches/foo.sysex", mode="rb")
 
# Reading file data with read() method
data = f.read()
 
# Knowing the Type of our data
print(type(data))
 
# Printing our byte sequenced data 
print(data)
 
# Closing the opened file
f.close()
