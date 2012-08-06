from os import system

system( "git add -u ." )
system( "git commit -m \"%s\"" % raw_input( "Commit message:\n" ) )
system( "git push origin master" )