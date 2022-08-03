# ap-angle-calculator
Calculates the angles to go on the nether roof for the next portal in all portals

Make sure all the files from APanglesv2.zip are in the folder that Mime's program is in (you have to take the files out, dont just drop the whole folder in)

First, double click the run_exe file. This will start Mime's program and save the output to a new file called coords.txt. You will not be able to see the output in the console, you will have to open coords.txt to see what the instructions in Mime's program are. If you know a way to make it output to both the console and file (in windows) please tell me because google could not.

You have to close and reopen coords.txt to see new outputs from Mime's program.

All inputs to Mime's program should be in the console as if it was normal, don't try to edit coords.txt at all (it won't let you anyway).

After you have found the first 8 strongholds, saved strongholds.qs, and pressed enter, double click the file called run_py. This will open a second console with my program running on it.

You will be prompted to enter your current coordinates on the nether roof and then press enter. After this, you will alternate between pressing enter on Mime's program and then on mine. If you get the same stronghold and location twice on my program, it means you forgot to press enter on Mime's.

My program will give the you the angles that I calculated and the coords from mime's program so you don't have to keep opening coords.txt.

You will not get a warning for 8th ring strongholds. Just play as normal and enter "0" to Mime's program if you encounter a missing stronghold. Then, press enter on my program as normal and it will give you the same stronghold number with a different angle and coords.

If you forget to set spawn and have to restart from 0 0, enter "d" into mime's program as normal. Then you will have to check coords.txt to see the instructions Mime has after you do this. Once you get the next stronghold on Mime's program, press enter on mine. Unfortunately, it will give you the wrong stronghold number but with the correct angle and coords so don't panic. It will fix itself on the next one.

If for whatever reason you need to pathfind again starting from some random coordinate, you can't. It will crash my program and I don't want to fix it.

If you press enter twice in a row on Mime's program, you will miss the angle and you'll have to find the direction on your own (and the coords from coords.txt). My program automatically updates with Mime's program so the next ones will still be correct. Pressing enter twice in a row on my program in an attempt to "fix" it will do absolutely nothing but output the same thing twice.

It's a bit scuffed but it works


Credits to TalkingMime for the original all portals calculator, I've gained a new appreciation for it after trying to make my own program

Thanks to DesktopFolder cause I would have given up or gone insane or probably both if he wasn't there to help me with confusing python things and troubleshooting



