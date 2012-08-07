from os import system, linesep

branch = "master"

system( "git add -u ." )

goals = raw_input( "What were your trying to add or fix? \n" )
results = raw_input( "What have you achieved? \n" )
issues  = raw_input( "What issues have you discovered? \n" )

commit_call = "git commit "

for s in [goals, results, issues]:
    commit_call += ("-m \"%s\" " % s)


system( commit_call );

system( "git push origin %s" % branch )