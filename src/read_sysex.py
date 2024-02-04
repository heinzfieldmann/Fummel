# Hard coded stuff playting around with a single sysex file.
# Can we read and parse the sysex-file?

# Opening the binary file in binary mode as rb(read binary)
# Let do it with one file to examine the file structure.
# We have some metadata about the patches and also the patch data
# 8 bytes are metadata? And rest are patch data.
# The patch data is stored in 32 consecutive 128 byte chunks.
# It would be quite easy to map them 
# I want to put the data in a database. Perhaps etcd?
# I might be able to do a hash of the 128 byte struct do avaid storing duplicates if I do large scale imports of patches.

file_name="../patches/bass001.syx"
sysex_file = open(file_name, mode="rb")
 
# Reading file data with read() method
s = sysex_file.read()
no_bytes=(len(s))

#Store the file metadata in variables.
S_start, S_ID, S_status, S_format, S_bytecount_msb, S_bytecount_lsb = s[0:6]

# Hm. In bulk data exchange is 1 or 32 the two exclusive numbers of patches?
# S_format = 0 (1 voice) S_format = 9 (32 voices)
if S_format == 0:
    no_patches = 1
elif S_format == 9:
    no_patches = 32
else:
    exit(1)

print("The file",file_name,"has",no_patches,"DX7 patch(es)")

#print(S_format)
# meta data format.
#     11110000  F0   Status byte - start sysex
#     0iiiiiii  43   ID # (i=67; Yamaha)
#     0sssnnnn  00   Sub-status (s=0) & channel number (n=0; ch 1)
#     0fffffff  00   format number (f=0; 1 voice)
#     0bbbbbbb  01   byte count MS byte
#     0bbbbbbb  1B   byte count LS byte (b=155; 1 voice)


# Closing the opened file
sysex_file.close()

#How to do the patch mapping if the 128 byte patch definitation?

# Something like this for each patch?
# Assign each byte to a named variable
#b0, b1, b2, b3, b4, b5, b6, b7, b8, b9, b10, b11, b12, b13, b14, b15, \
#b16, b17, b18, b19, b20, b21, b22, b23, b24, b25, b26, b27, b28, b29, b30, b31, \
#b32, b33, b34, b35, b36, b37, b38, b39, b40, b41, b42, b43, b44, b45, b46, b47, \
#b48, b49, b50, b51, b52, b53, b54, b55, b56, b57, b58, b59, b60, b61, b62, b63, \
#b64, b65, b66, b67, b68, b69, b70, b71, b72, b73, b74, b75, b76, b77, b78, b79, \
#b80, b81, b82, b83, b84, b85, b86, b87, b88, b89, b90, b91, b92, b93, b94, b95, \
#b96, b97, b98, b99, b100, b101, b102, b103, b104, b105, b106, b107, b108, b109, \
#b110, b111, b112, b113, b114, b115, b116, b117, b118, b119, b120, b121, b122, \
#b123, b124, b125, b126, b127 = s[patchdatasubset]
