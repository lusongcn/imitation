# -*- coding: utf-8 -*-
import sys

class imitationConfig(object):
    def __init__(self):
        self.hostUrl = "https://ptorch.com/"

    def defaultDescribe(self):
        print " ___________ "
        print " \033[07m  imitation.py! \033[27m           # CSS"
        print "      \                     # Image"
        print "       \   \033[1;31m,__,\033[1;m             # Js"
        print "        \  \033[1;31m(\033[1;moo\033[1;31m)____\033[1;m         # Html"
        print "           \033[1;31m(__)    )\ \033[1;m  "
        print "           \033[1;31m   ||--|| \033[1;m\033[05m*\033[25m\033[1;m      [ Song Lu | https://ptorch.com ]\r\n\r\n"

        print "	\033[0;33;40m[ Options ]\033[0m"
        print "	-h	Display this help message"

        print "	-i	Imitation a single page"
        print "		Recommended for testing"

        print "	-l	Imitation website from a List"
        print "		Recommended to put the document in this project"

        print "	-e	Has program"

        print "	-v	Version of the program"

    def singleImitation(self):
        host = raw_input("> HostUrl: ").lower()
        return host

    def listImitation(self):
        host = raw_input("> List file address: ").lower()
        return host

    def Version(self):
        print "Imitation Website version "+"\033[0;33;40m 1.0\033[0m"

    def Porblem(self):
        print "Discuss："+"\033[0;33;40m https://ptorch.com\033[0m"
        print "QQGroup："+"\033[0;33;40m 168117787\033[0m"

    def getInstructions(self):
        if len(sys.argv) < 2 or sys.argv[1] == '-h':
            self.defaultDescribe()
            return "end"
        elif sys.argv[1] == '-v':
            self.Version()
            return "end"
        elif sys.argv[1] == '-e':
            self.Porblem()
            return "end"
        elif sys.argv[1] == '-i':
            require = self.singleImitation()
            return ["single",require]
        elif sys.argv[1] == '-l':
            require = self.listImitation()
            return ["list",require]
