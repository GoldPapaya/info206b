# print the key/value pair of a dictionary sorted on value
def printSortedDictionary( D ):
    DS = sorted(D.items(), key=lambda x:x[1], reverse=True)               
    for k in DS:
        print(k)

# strip word of punctuation and convert to all lower-case
def stripWord( w ):
    w = w.lower()
    return( w )

# process text file
myfile = open( 'lessons/doi.txt', 'r' )
doi = {}
for line in myfile:
    for word in line:
        for c in word:
            c = stripWord( c )
            if( len(c) > 0 ) and c.isalpha():
                if c in doi: 
                    doi[c] += 1
                else:
                    doi[c] = 1
                    
myfile.close()
printSortedDictionary( doi )