import sys
print "welcome."
print "please enter a string:"
sys.stdout.flush()
line = sys.stdin.readline().strip()
print "you entered %d characters " % len(line)
