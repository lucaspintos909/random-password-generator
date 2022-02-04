# importing required modules
from ast import Pass
import os, sys, argparse, pyperclip, shutil

from source import random_password_generator as rpg

# create a parser object
parser = argparse.ArgumentParser(description="Random Password Generator.")

# add arguments
parser.add_argument("--length", nargs="?", default="15", type=int, metavar="num",
                    help="Password length")

parser.add_argument("--numbers", nargs="?", default="1", type=int, metavar="num",
                    help="Number of numbers in the password")

parser.add_argument("--symbols", nargs="?", default="1", type=int, metavar="num",
                    help="Number of symbols in the password")

# parse the arguments from standard input
args = parser.parse_args()

# generate the password
result = rpg.generate(args.length, args.numbers, args.symbols)

columns = shutil.get_terminal_size().columns

if not result["valid"]:
  print(f"**** Error: {result['message']}".center(columns))
  sys.exit()

if os.name == "posix":
  os.system("clear")
else:
  os.system("cls")

pyperclip.copy(result["password"])

print(f"Password: {result['password']} \n".center(columns))
print(f"**** The password has been copied to the clipboard! ****".center(columns))