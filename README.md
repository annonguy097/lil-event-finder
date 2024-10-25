# LIL-Event-Finder
This tool is made for [lessons in love](https://www.lessonsinlovegame.com). It is an offline wiki tool which allows you to search events.
The program does not pull information from the wiki but instead uses your local files to collect information.
This is also compatible with any DLC content as well as supporter versions of the game.

There are many "cheating" commands. I do not care as this is a single player game, and you are only affecting your own experiences. The commands were added not to cheat through the content but used as a way to easily progress to other routes and decisions.
Also in order to cheat properly you need to know how python works. If you are willing to learn a programming language to cheat through the resets, then by all means go ahead.
I will say, the resets are easier than learning python.

This program may be in violation of the Lessons In Love official discord rules. One of the big reasons is the modified 'headpatcenteral.rpy'. Another reason this might not be allowed is the 'cheating' commands which I can't stress enough aren't for cheating.
You have been properly warned by me about the violations. Any subsequence bans or other forms of punishment are from neglect of this warning.

Lastly, thanks to the few people who helped me test this and for their feedback. Without their help I would not be able to verify if this works on Mac or Linux.

### 18+
For anyone who stumbled across this randomly be warned the game is 18+. The game will contain harsh, violent, morally wrong, and sexual themes.

### Data Warning
Some of the commands will write data onto your pc. To keep your data safe the program will request authorization when it needs to write. You have the option to deny all data write requests.

## Licensing
You are prohibited from posting modified or unmodified versions of this program anywhere. You can not upload any compiled code onto Discord, google drive, or any other file sharing services. This includes posting any jar file which contains my code or any variation of it.

I'm not being blamed because someone wanted to post a version of this infected with malware. DO NOT DOWNLOAD FROM ANY UNOFFICIAL SITES. The only site this was uploaded too was GitHub. 

## Java and Python
There is both a Java and a Python version. The python version works the same as the Java version, but it's significantly slower.
I recommend the Java version over the Python version. The python version doesn't have as many commands as the Java version.


Note: I have never programmed in Python before, and I am not taking criticism over the code. It works and that's all that matters to me. I do not care if I "improperly" name functions or variables. If you don't like it fix it yourself.

### Install python
Create a new file called `event finder.bat` where the game .exe is located. Edit the file in notepad and add the following two lines.
```bash
"lib/py3-windows-x86_64/python.exe" "event finder.py"
PAUSE
```

Note: Python is already packed with the game files. The command just uses that python version to execute the file. This makes the python version significantly easier to install.

## Install
Please download the jar from the releases tab. Place jar inside of your lessons in love directory (where the .exe is located).
Next download [java 21](https://www.oracle.com/java/technologies/downloads/#jdk21-windows) mis installer if you are on windows.

Make a new file called start.bat. Edit the file in notepad and add the following lines. Note, this file should be in the same place as the .jar and .exe.

`java -Xmx1G -jar lil-event-finder-3.0-SNAPSHOT.jar`

Warning: The program caches all the data associated with every event. This takes quite a bit of memory, and you may run into errors if your system has less than 4GB of ram.
You can modify the `-Xmx` command to cap the memory resources. The lowest recommended value is 500M. `-Xmx500M`.

## Usage
The following is a preview of the commands.

Type the number that correlates to the command. 
```
  1. Search for event name.
  2. Search for dialogue.
  3. Advanced dialogue search.
  4. Dump all lines from an event.
  5. Dump events.
  6. List all event files.
  7. Verify events.
  8. Get current word count.
  9. List all characters.
  10. Automatically enable renpy console.
  11. Manually enable renpy console.
  12. List all events containing a character.
  19. Help and bug information.
  0. Exit.
  > _
```

Searching event/dialogue
```
> I'll find you again
Searching for 'I'll find you again'
Event: beachmas19
  Location: Chapter 3
  File: chap3.rpy
  Event Line Number: 20713
  Replay Name: I Will Deliver You to the Fireflies
  Line: m "I'll find you again."
  Line Number: 20958
```

Writing data confirmation
```
> 13
This will modify the head-pat minigame to increase the increment of head-pats to five.
To do this, the program will need to write data onto your pc.
Please enter 'Y' to continue or literally anything else to go back.
> y
Verifying file...
Successfully written file!
```

Advanced dialogue search
```
Please enter the dialogue you wish to search for (example: 'You're disgusting').
Type 'exit' to go back.
> You're disgusting

Please enter the character you wish to search for (example 'ami')
Type 'exit' to go back.
> otoha
Character: Otoha
Character Alias: o.
Character found. Searching...
Event: otohaspecial15p1
  Location: Otoha Event
  File: OtohaEvents.rpy
  Event Line Number: 2388
  Replay Name: King Midas
  Line: o "Somewhere I belooooong. Fucking Linkin Park, man. So good. I bet they wouldn't struggle with fucking bullshit like this. I'm a fake. I'm pathetic. Fuck you, Otoha. Fuck you. Piece of shit. You're disgusting."
  Line Number: 2566
```

### Renpy Console
Renpy console should only be enabled for replays. I do not condone cheating the resets with the console.

If you want to view a replay that changes with decisions made then you can use the console. Inside the console you need to change the variable that is associated with decision you missed.
For example, if you replay Maya's event `Now More Than Ever`, you will not see the dialogue that is associated with the event `A Place That Only Exists In Our Minds`.
To see this extra dialogue, start the replay then enter the renpy console. Enter the command `mayadorm35 = True` and close the console.

If you start changing variables please never save your game. This **WILL** break your save. Always load back to the original save after every variable. You have been warned, and I'm not responsible for people losing 100hr+ save files.

## Issues 
This is a list of all known issues with the program.

### Building event cache stalling
The event cache is a long process. If it appears to be stuck I recommend waiting for at most 10 minutes. If nothing happens after 10 minutes, allow the program access to more resources. You can increase the `-Xmx` parameter or remove it entirely.
`java -Xmx4G -jar lil-event-finder-3.0-SNAPSHOT.jar` or `java -jar lil-event-finder-3.0-SNAPSHOT.jar`

If the above seemed to have done nothing then your computer may be a limitation. The hard-drive can severely impact this process if it is slow. I do not recommend using this tool if it takes longer than 5 minutes to load. I cannot ask anyone to constantly sit through the painfully long loading process.

### Incorrect chapter locations
Some chapter 2 events will display as chapter 1. This issue is caused by some of the ch2 events being inside the script.rpy file. There is no fixes for this.

### 'java' is not recognized as an internal or external command, operable program or batch file. OR The bat file does not open a console.
You need to have java 21 installed onto your pc. Please see the `install` instructions above.

### Out of Memory
Your system does not have the sufficient resources to open the program. Trying adding the `-Xmx` launch arg. You can range between `500mb` to `1GB`.
`java -Xmx500M -jar lil-event-finder-3.0-SNAPSHOT.jar`

### Inaccurate word count
The word count that is calculated is roughly 300k short of Sel's number. I'm not sure if this is an issue as I do not know how he calculates it. The number from the program is achieved by removing all programming lines and only calculates what's inside the text box.
For example, when Maya says "I'll find you again" the program for that line is `m "I'll find you again"`. My program does not count the 'm' as a word and it removes it from the count.

Seeing as there is like 2 million+ words it's not an easy function to test and debug. There may be a logical oversight when I made it.

## How does this exactly work? (Nerdy stuff)
The program is essentially a huge file scanner which scans every .rpy file. These files contain the code and instructions for the game. Every event begins with the `label` command. This program reads every chunk of code between the label and the `jump`.
A jump is used to switch to a different event. All of this information is gathered during the caching process and is saved into memory for quick access. Since the events contain all the programming up to the jump command it's quite easy to filter them.

