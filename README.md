# TOPBot


I went back to the very first computer game that I ever played and did not realize how much of a grind it was to get to endgame. I guess as a kid I didn't mind pouring hours and hours into a game. Wrote a quick script so that my character would keep grinding with me away from the computer.


Written in Python with pyautogui and pywin32,

the script must have an image of the level, and name of the mob. However, to get this image you must abide by some conditions:

  1. The picture MUST be taken with pyautogui's screenshot() function
  
  
  2.The picture MUST be taken in the same MONITOR that you will put the TOP client in.
  
I've attached some pictures that might also be useful as they drop the class advancement items which can be sold for a pretty penny and easy to kill. 
"AnchoredX" and "AnchoredY" is the coordinates that your character will go to if he hasn't attacked anything within the timespan that you decide. 

You can either grind out levels using attackHere()

or if you do attackAndLoot() it goes to the monster to loot it too.
  WARNING: i've run the bot for hours at a time only to lose all of the progress using attackAndLoot(). It's tough to use right and could use some more refining.
  
  TIPS:
  
      1. Try not to use attackAndLoot() with monsters that span a wide area, remember the character will go to the monster's corpse after it dies, and searches for monsters there. If the monsters spawn in a wide area, your character's going to go travelling on it's own, maybe even aggro'ing some stronger mobs.
      
      
      2. If your character is handling small fry, just pass in the surrounding mobs levels and nametags so the bot kills them too, maybe use attackHere() to stop looting useless trash from irrelevant mobs.
      
      
 
 things to note:


1. stupid igg devs for some reason made the skillbar FOCUSABLE???? thus if the bot clicks on the skillbar, the bot's automated keypresses will not register as hotkeys in the game. I just hide the skillbar, but you can set pyautogui to only scan a segment of your screen.

2. you can make this cross-platform by getting rid of pywin32, and using pyautogui's click() method. However, I faced a weird obstacle where pyautogui's actions were not registering in the game after a couple of hours. I solved it by clicking anywhere on the screen with pywin32 but its a hacky solution.
      
