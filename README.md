# TOPBot


I went back to the very first computer game that I ever played and did not realize how much of a grind it was to get to endgame. I guess as a kid I didn't mind pouring hours and hours into a game. Wrote a quick script so that my character would keep grinding with me away from the computer.


Written in Python with pyautogui and pywin32,

the script must have an image of the level, and name of the mob. However, to get this image you must abide by some conditions:

  1. The picture MUST be taken with pyautogui's screenshot() function
  2.The picture MUST be taken in the same MONITOR that you will put the TOP client in.
  
"AnchoredX" and "AnchoredY" is the coordinates that your character will go to if he hasn't attacked anything within the timespan that you decide.

You can either grind out levels using attackHere()

or if you do attackAndLoot() it goes to the monster to loot it too.
  WARNING: i've run the bot for hours at a time only to lose all of the progress using attackAndLoot(). It's tough to use right and could use some more refining.
  
  TIPS:
      1. Try not to use attackAndLoot() with monsters that span a wide area, remember the character will go to the monster's corpse after it dies, and searches for monsters there. If the monsters spawn in a wide area, your character's going to go travelling on it's own, maybe even aggro'ing some stronger mobs.
      2. If your character is handling small fry, just pass in the surrounding mobs levels and nametags so the bot kills them too, maybe use attackHere() to stop looting useless trash from irrelevant mobs.
      
