from time import time

def main():
    override = input("Would you like to override the time command? ")
    return True if override.upper().startswith('Y') else time() >= 1546362000
    #time can be whatever
