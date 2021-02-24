
fh = open('Try.txt','a')
for i in range (10):
    fh.writelines("This is us %d\n" %i)
    
fh.close()

