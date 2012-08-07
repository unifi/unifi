from os import system, linesep

branch = "master"

system( "git add -u ." )

goals = raw_input( "What were your trying to add or fix? \n" )
results = raw_input( "What have you achieved? \n" )
issues  = raw_input( "What issues have you discovered? \n" )

system( "git commit -m \"%s\"" % \
        "; ".join( [goals, results, issues] )
)

system( "git push origin %s" % branch )