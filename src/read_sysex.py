# Hard coded stuff playting around with a single sysex file.
# Can we read and parse the sysex-file?

# Opening the binary file in binary mode as rb(read binary)
# Let do it with one file to examine the file structure.
# We have some metadata about the patches and also the patch data
# The patch data is stored in 32 consecutive 128 byte chunks.
# It would be quite easy to map them 
# I want to put the data in a database. Perhaps etcd?
# I might be able to do a hash of the 128 byte struct do avaid storing duplicates if I do large scale imports of patches.

sysex_file = open("../patches/bass001.syx", mode="rb")
 
# Reading file data with read() method
sysexdata = sysex_file.read()
 
no_bytes=(len(sysexdata))

#Print start of sysex. First item. Should be xf0/240/11110000
S_start=(sysexdata[0])
print(S_start)
#Print end of sysex. Last item. shoud be xf7/247/11111011
S_stop=(sysexdata[no_bytes-1])
print(S_stop)
# MachineID. Yamaha x43/67
S_ID=(sysexdata[1])
print(S_ID)

# Closing the opened file
sysex_file.close()
