letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('''                                                                           
                                      8880GGCCCCLLG088888                                           
                                  88GLf1i;:::::::::;;i1tfG08                                        
                                8Cf1;::::::::::::::::::::;1fC08                                     
                             80L1;:::::::::::::::::::::::::::itL08                                  
                            Gfi:::::::::::::::::::::::::::::::::ifG8                                
                          8C1:::::::::::::::::::::::::::::::::::::;tC8                              
                         8Ci::::::::::::::::::::::::::::::::::::::::;1LG8                           
                       88C1;:::::::::::::::::::::::::::::::::::::::::::;1LG0888                     
                     8Gfi;::::::::::::::::::::::::::::::::::::::::::::::::;;itG                     
                   80f;::::::::::::::::::::::::::::::::::::::::::::::::::::;1G8                     
                   8Li::::::::::::::::::::::::::::::::::::::::::::::::::::;f0                       
                   0t;::::::;;:::::::::::::::::::::::::::::::::::::::::::iG                         
                   8Li::::::1Lf1i:::::::::::::::::::::::::::::::::::::::;f0                         
                   80t::::::t000GLt1;;::::::::::::::::::::::::::::::::::iG8                         
                     Gt::::;f000000GCLft1i;::::::::::::::::;ii1tffi::::;f8                          
                      0t;::1C00000000000GGCCCLLffttfffffLLCCGGG00Ct;:::f08                          
                   8GCCL1::tLCCCCGGGGG000000000000000000000000000Gf;,;f0                            
                  8G;,,... .,,,,,::::::;;;;iii1111tttffffLLLLCCCGCf;:1G88                           
                  80Lt; ,:;:::::,,,,,,,,,...     ...     ............,:;f8                          
                     L:.:tLCCCCCCCCCLLLLff1,    ,i1111iiiiii;;;;;::. .:if8                          
                     f: :1LCCCCCCCCCCCCCCCf.    :fLCCCCCCCCCCCCCLLf, ,G88                           
                   88L;.,1LCCCCCCCCCCCCCLL1.    :tLCCCCCCCCCCCCCCLt, ,0                             
                  800C1..iLCCCCCCCCCCLLCCf;.,:, ,1LCCCCCCCCCCCLLCfi..;0                             
                 80000L:..iLCCCCCCCLCCCLf;. if1..;fCCCCCCCCCLLCLLt, :f08                            
                 80000GL; .:ifLLLLLLLfti,..;LGC;. :tCCCCCCCCCCLL1, ,tG008                           
                  800000Ct;,..,:;;;;:....;fG000G1, .,itfffLffti,.,iL000008                          
                   88000000Cf1;:,,,::;1fCG000000GCt;,  ..,,,,..:1fG0000008                          
                     88888000GLLLLCCGG0000000000000GLf1i;;;i1tfC0000000088                          
                         800GLffLCG000000000000000000000GGG0000000000088                            
                         800GLftfCG00000000GGGGGG000000000000000008888                              
                         800GLftfLG00000000000000000000000000000008                                 
                         800GCftfLCG000000000000000000000000000GCG08                                
                         80000CLttfCG000000000000000000000000GLffLG08                               
                         80000GCfttfLG000000000000000000000GLftttLG8                                
                         800000GCftttfLCGG00000000000000GGCLfttfC08                                 
                         88000000GCLfttffLCCGGGGGGGGGGCCLfttffLC08                                  
                          880000000GGLLftttffffLLffftfffLffLCGG08                                   
                           8800000000GGGCLLLfttttttffffLCCCG00088                                   
                            880000000000000GGCCCCCGGGGG00000088                                     
                              88000000000000000000000000000088                                      
                                8800000000000000000000000888                                        
                                  8800G0000000000000008888                                          
                                  880GGGGGGGGGGGGGG0088                                             
                           80GGCLfttfG0000GGGGGGG00CftfLLCC08                                       
                        0Cfti;;:::::;fG00000000000G1::::::;itLG8                                    
''')
print("Welcome to the PyPassword Generator! Created by Arif")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

import random

password = ""

for char in range(0, nr_letters):
    password += random.choice(letters)

for char in range(0, nr_symbols):
    password += random.choice(symbols)

for char in range(0, nr_numbers):
    password += random.choice(numbers)

string = list(password)
random.shuffle(string)
password = "".join(string)

print(f"your password is: {password}")



