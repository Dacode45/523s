import subprocess, os
import sys

# The following variables control the command line
# program = "./ans_check5 "
# arg_pattern = 'a'
# pattern_max = 48

def run_pattern(program, arg_pattern, pattern_max):
    for i in range(int(pattern_max)):
        print "Trying input with length", i
        cs = program + " " + arg_pattern*i
        print "Command: %s" % cs
        print "******************"
        proc = subprocess.Popen([cs], shell=True,
                                stdin=subprocess.PIPE,
                                stdout=subprocess.PIPE)
        print proc.communicate()[0]
        print "******************"
        print "Return value: %i, %s" % (proc.returncode,
                                        os.strerror(proc.returncode))

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: %s arg_pattern pattern_max"%sys.argv[0])
    else:
        run_pattern(*sys.argv[1:])
