#!/usr/bin/python

import os
import re
import sys

class Grep:
    '''Replicates functionality of "grep -r".
    Takes: A search string pattern or regular expression
    and list of space separated files or directories.
    Returns: Filename: matched string, if the match was found.
    '''

    # Lambda function to determine whether a file is binary
    textchars = bytearray([7,8,9,10,12,13,27]) + bytearray(range(0x20, 0x100))
    is_binary_string = lambda self,bytes: bool(bytes.translate(None, self.textchars))

    def __init__(self, *arg):
        self.pattern = arg[0]
        self.location = arg[1:]

    def file_match(self, fname, pattern):
        '''Iterates through file line by line and performs
        regular expression search.
        Outputs matched filename and string.
        '''
        try:
            f = open(fname, "rt")
        except IOError:
            return
        is_binary = self.is_binary_string(f.read(1024))
        # returning to the begining of file
        f.seek(0)
        for line in f:
            if pattern.search(line):
                if is_binary:
                    print "Binary file %s matches" % fname
                else:
                    print "%s: %s" % (fname, line.rstrip())
        f.close()


    def grep(self, search_pattern, location):
        '''Iterates through files and directories and
        performs regular expression search
        '''
        re_pattern = re.compile(search_pattern)
        for loc in location:
            if os.path.isdir(loc):
                for dirpath, dirnames, fnames in os.walk(loc):
                    for fname in fnames:
                        fullpath = os.path.join(dirpath, fname)
                        self.file_match(fullpath, re_pattern)
            elif os.path.isfile(loc):
                self.file_match(loc, re_pattern)
            else:
                print "No such file or directory: %s" % loc

    def run(self):
        '''Executes search. Location is a tuple.
        '''
        self.grep(self.pattern, self.location[0])


if __name__ == '__main__':

    if len(sys.argv) <= 2:
        msg = "Usage: %s <pattern> <list files or locations>\n" % sys.argv[0]
        sys.stderr.write(msg)
        sys.exit(1)

    search = Grep(sys.argv[1], sys.argv[2:])
    search.run()
