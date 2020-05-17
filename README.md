# 2048-game    
Ivlabs 2048 project    
Both linux and windows program work in exactly same manner, however, the linux progarm uses readchar library to take moves as input without pressing enter, on the other hand windows program uses msvcrt library for the same.    
In the first step user is asked to choose an option from PLAY and QUIT.    
![](step1.jpg)
option "1" starts whereas "2" quits the game, any other input is considered as invalid.    
In the second step user is asked to eneter SIZE OF BOARD"n". Pressing ENTER without giving any value will create board of default size"5".    
![](step2.jpg)
Similarly, input is taken in third step which desides target score"w". Default score here is 2048 if user does not pass any input and presses enter.    
![](step3.jpg)
After the value of "w" is passed the game commenses, thereafter, all the MOVES are taken WITHOUT the need of pressing ENTER.    
![](step4.jpg)
Every next step commenses only when the user enter "W" "A" "S" OR "D", where w = up;a = left; s = down; d = right.Other inputs are considered invalid.    
![](nextsteps.jpg)
When the player reaches or crosses the target score he/she wins.    
The process then starts once again.    
![](nextround.jpg)    
It asks for the same inputs again.    
![](match2.jpg)    
![](lost.jpg)
If player fails to reach the target score, he/she looses
