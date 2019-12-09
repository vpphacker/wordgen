import time
import os
import sys
from itertools import permutations
from itertools import combinations
import argparse

def slowprint(s):

    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(1. / 1000)

def wordgen():
       os.system("clear")
       print ("\033[1;32m\007\n")
       os.system("figlet WordGen | lolcat")
       time.sleep(2)
       parser = argparse.ArgumentParser(
        description='This Programme try to create a list of password from entered word.')
       parser.add_argument('--minLength', help='minimum length of password', default=3)
       parser.add_argument('--maxLength', help='Maximum length of password', default=16)
       parser.add_argument('--initList', help='Path to the initial word list', default="")
       args = parser.parse_args()


       input_words = []
       output_words = []


       if args.initList != (""):
           f = open(args.initList, "r")
           for x in f:
               x = x.rstrip()
               input_words.append(x)
       else:
           print("                              ")
           slowprint ("\033[1;36m =================================================")
           slowprint("\033[1;33m|          Write Your Words and then for          |")
           slowprint ("\033[1;36m =================================================")
           slowprint ("\033[1;33m|         Finishing Enter \033[1;32m#VPPHacker\033[1;33m              |")
           slowprint ("\033[1;36m =================================================")
           print("\033[1;32m  ")
           while 1:
               inp = input()
               if inp.__eq__("#VPPHacker"):
                   break
               else:
                   input_words.append(inp)

       for i in range(0, input_words.__len__()):
           comb = combinations(input_words, i + 1)
           for wordSet in list(comb):
               passLength = 0
               for j in wordSet:
                   passLength += len(j)
               if args.minLength <= passLength <= args.maxLength:
                   perm = permutations(wordSet)
               for j in list(perm):
                   result = ("")
                   for k in range(0, j.__len__()):
                       result += j[k]
                   output_words.append(result)

       with open("output.txt", "w") as txt_file:
           for line in output_words:
               txt_file.write("".join(line) + "\n")

       print("               ")
       slowprint ("\033[1;36m =================================================")
       slowprint("\033[1;33m|     Conguleration " + str(len(output_words)) + " password generated!!!      |")
       slowprint ("\033[1;36m =================================================")
       slowprint ("\033[1;33m|      Thanks For Using Wordlist Generator        |")
       slowprint ("\033[1;36m =================================================")
       time.sleep(1)
       exit()

def about():
       os.system("clear")
       print ("\033[1;32m\007\n")
       os.system("figlet WordGen | lolcat")
       time.sleep(2)
       slowprint ("\033[1;91m -----------------------------------------------")
       slowprint ("\033[1;33m" + "         [+] Tool Name     =>\033[1;36m" + " WordGen")
       slowprint ("\033[1;33m" + "         [+] Autor         =>\033[1;36m" + " VPPHacker")
       slowprint ("\033[1;33m" + "         [+] Latest Update =>\033[1;36m" + " 01/12/2019")
       slowprint ("\033[1;33m" + "         [+] YouTube       =>\033[1;36m" + " VPPHacker")
       slowprint ("\033[1;33m" + "         [+] Github        =>\033[1;36m" + " VPPHacker")
       slowprint ("\033[1;91m -----------------------------------------------")
       slowprint ("\033[1;95m" + "          [+] www.vpphacker.com [+]          ")
       slowprint ("\033[1;91m -----------------------------------------------")
       magas = input("\033[1;33m [+] Press Enter To Continue [+]")
       if magas == " ":
           os.system("clear")
           return main()

       else:
           os.system("clear")
           return main()

def ext():
      slowprint ("\033[1;36m ==============================================")
      slowprint ("\033[1;33m|     Thanks For Using Worlist Generator       |")
      slowprint ("\033[1;36m ==============================================")
      time.sleep(1)
      exit()

def main():
      os.system("clear")
      print("\033[1;36m")
      os.system("figlet WordGen | lolcat")
      slowprint(" ")
      slowprint ("\033[1;33m    [ 01 ]\033[1;91m Generate WordList")
      slowprint ("\033[1;33m    [ 02 ]\033[1;91m About This Tool")
      slowprint ("\033[1;33m    [ 00 ]\033[1;91m Exit")
      print("     ")
      option = input("\033[1;36m    [ ++ ] WordList Generator [ ++ ] >> \033[1;32m")
      if option == "1":
          os.system("clear")
          wordgen()
          exit()

      elif option == "2":
          os.system("clear")
          about()
          exit()

      elif option == "0":
          os.system("clear")
          ext()
          exit()

      else:
          os.system("clear")
          slowprint ("\033[1;91m Enter Corret Number!!!")
          time.sleep(2)
          os.system("clear")
          return main()

main()
