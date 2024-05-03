MAX_TRIES = 6

FILE_PATH = (r"hangman words.txt") 

#add another \ to any exist \ to avoid syntax warning
HANGMAN_ASCII_ART = ("""Welcome to the game Hangman!\n
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \\ / _` | '_ ` _ \\ / _` | '_ \\ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\\__,_|_| |_|\\__, |_| |_| |_|\\__,_|_| |_|
                      __/ |                      
                     |___/
""")

#dictionary with the hangman situations
HANGMAN_PHOTOS = {
1: """   
x-------x
""",
2: """   
x-------x
|
|
|
|
|""",
3: """     
x-------x
|       |
|       0
|
|
|""",
4: """       
x-------x
|       |
|       0
|       |
|
|""",
5: """     
x-------x
|       |
|       0
|      /|\\
|
|""",
6: """     
x-------x
|       |
|       0
|      /|\\
|      /
|""",
7: """       
x-------x
|       |
|       0
|      /|\\
|      / \\
|"""
}