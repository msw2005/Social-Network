from Runs import Runner
from loading import Loader
from printer_console import ConsolePrinter
#gsgsgs

print("Social network simulator.")
Runner(Loader(), ConsolePrinter()).run_program(input("Enter a file name for network data: "))
