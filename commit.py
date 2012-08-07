from os import system

branch = "master"

system( "git add -u ." )

issue = raw_input( "Which issue were you trying to fix? \n" )
results = raw_input( "What have you achieved? \n" )
limits = raw_input( "What limitations have you discovered? \n" )

system( "git commit -m \"%s\"" %  ("%s\n%s\n%s\n" % (issue, results, limits)) )
system( "git push origin %s" % branch )