import fnmatch
import os
 
rootPath = '.'
pattern = 'urls.py'
 
output = "" 

for root, dirs, files in os.walk(rootPath):
    for filename in fnmatch.filter(files, pattern):
        print( os.path.join(root, filename))
        
        with open( os.path.join(root, filename) ) as source:
            output += "\n%s" % ( source.read() )
            

with open( "all_urls.py", "w" ) as target:
    target.write( output )