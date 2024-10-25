import os
import re

from operator import length_hint

# INSTRUCTIONS:
# Create a new file called 'event finder.bat'
# Right-click -> edit
# Add the following lines and save (ctr+s)
# "lib/py3-windows-x86_64/python.exe" "event finder.py"
# PAUSE
# Make sure to add the 'PAUSE'. Yes it's on a different line. Without pause, if any problems occur the console window will never open or immediately close.

# THIS IS SIGNIFICANTLY SLOWER THAN THE JAVA VERSION
# ONLY USE THIS IF YOU ARE HAVING ISSUES WITH THE JAVA VERSION
# ALSO NOTE I HAVE NEVER CODED IN PYTHON BEFORE
# BOTH VERSIONS WILL RECEIVE UPDATES WHEN NECESSARY
#
# Issues:
# The word count is different from the Java version. I have no idea why. It's only off about 100 words which isn't significant.
# Python is either really slow or I suck at coding in it.
# Due to how python writes files there will be no 'cheating' commands. Use the Java version if you want those.
#
# License
# I honestly don't care what you do with the Python version. Re-post, modify, copy, do whatever you want with it.
# I'm not proud of this code given I never used python before. I'm not going to gatekeep it.
# I was on coke when I wrote this whole thing in 10 minutes. Good luck with fixing and debugging.
#
# Version 1.0.0
def main():
    print("Verifying game folder...")

    main_dir = os.path.dirname(os.path.realpath("__file__"))
    game_dir = main_dir + "/game/"
    nsfw_dir = game_dir + "/scripts/subscribestar/"

    renpy_files = []

    ren_file = []

    characters = []

    if not os.path.isdir(game_dir):
        print("Please place the .py file inside of your lessons in love directory.")
        exit(1)

    for fn in os.listdir(game_dir):
        f = os.path.join(game_dir, fn)
        if os.path.isfile(f) and fn.endswith(".rpy"):
            renpy_files.append(f)

    for fn in os.listdir(nsfw_dir):
        f = os.path.join(nsfw_dir, fn)
        if os.path.isfile(f) and fn.endswith(".rpy"):
            renpy_files.append(f)

    size = length_hint(renpy_files)
    print("Collected " + str(size) + " scripts")
    print("Building event cache (This may take several minutes)...")

    count = 0
    pcount = 0
    for fn in renpy_files:
        pcount = pcount + 1
        # Filter
        if "autopatch" in fn or "checker" in fn or "definitions" in fn or "dlcmenu" in fn or "gui" in fn or "jukebox" in fn or "options" in fn or "profile_outfits" in fn or "screens" in fn or "unlockables" in fn or "setup" in fn:
            continue

        ref = RenFile(fn)
        events = ref.get_events()
        for event in events:
            count = count + 1
            event.gather_replay_info()
        ren_file.append(ref)
        round1 = round((pcount / len(renpy_files)) * 100, 2)
        print("Processed " + ref.name + " " + str(round1) + "%")
    print("Finished event cache.")

    print("Collecting characters...")
    def_file = os.path.join(game_dir, "definitions.rpy")
    if not os.path.isfile(def_file):
        print("ERROR: Could not find definitions file")
    else:
        def_filer = open(def_file, encoding="utf8")
        for line in def_filer:
            line = re.sub("\s\s+", " ", line)
            line = line.strip()
            if line.startswith("define") and "Character(" in line:
                line = line.replace("define", "")
                key_value = line.split("=", 2)
                alias = key_value[0]
                alias = re.sub("\s\s+", " ", alias)
                alias = alias.strip()

                character_name = key_value[1]
                character_name = re.sub("\s\s+", " ", character_name)
                character_name = character_name.strip()
                character_name = character_name.replace("Character(", "")

                params = character_name.split(",")
                character_name = params[0].replace("\"", "")

                character = Character(character_name, alias)
                characters.append(character)

    print("Collected " + str(count) + " events")
    print("Collected " + str(len(characters)) + " characters")
    con = Console(ren_file, characters)
    con.app()

def get_event_location(event):
    file_name = event.filename
    file_split = file_name.split("/")

    split_length = len(file_split)

    fn = file_split[split_length - 1]

    if "Events" in file_name:
        character = fn.split("Events")[0]
        return character + " Event"
    else:
        if "script.rpy" in file_name:
            return "Chapter 1"
        elif "ch2" in file_name:
            return "Chapter 2"
        elif "ch3" in file_name or "chap3" in file_name:
            return "Chapter 3"
        elif "ch4" in file_name or "chap4" in file_name:
            return "Chapter 4"
        # TODO You will have to manually add additional chapters as they are released.
        else:
            return "Unknown"


def print_event_info(event):
    print("Event: " + event.name)
    print("  Location: " + get_event_location(event))

    file_split = event.filename.split("/")

    split_length = len(file_split)

    fn = file_split[split_length - 1]

    print("  File: " + fn)
    print("  Replay Name: " + event.replay_name)
    print("  Line Number: " + str(event.line_index))

def print_dialogue_info(event, full_line):
    print("  Line: " + full_line.strip())
    print("  Line Number: " + str(event.get_line_number(full_line)))

class Console:

    def __init__(self, ren_files, characters):
        self.ren_files = ren_files
        self.characters = characters
        print("")
        print("")
        print("Welcome to the Lessons In Love Event Finder.")
        print("This is the Python version which is significantly slower than the Java version.")
        print("If you have issues, create an issue report and switch to the Java version.")
        print("Both versions will be updated when necessary.")
        print("")
        print("Remember, God Is Dead. Praise be! ssssssssssssssssss ttttttttttttttttttttttt")
        print("")
        print("")

    def app(self):
        print("\nPlease enter the command number (1-10), you wish to use.")
        print("  1. Search for event name.")
        print("  2. Search for dialogue.")
        print("  3. Advanced dialogue search.")
        print("  4. Dump all lines from an event.")
        print("  5. Dump events.")
        print("  6. List all event files.")
        print("  7. Verify events.")
        print("  8. Get current word count.")
        print("  9. List all characters.")
        print("  10. List all events containing a character.")
        print("  0. Exit.")
        command = input("> ")
        if command == "1":
            self.search_event_name()
            self.app()
        elif command == "2":
            self.search_for_dialogue()
            self.app()
        elif command == "3":
            self.search_advanced_dialogue(True, "")
            self.app()
        elif command == "4":
            self.dump_lines_event()
            self.app()
        elif command == "5":
            self.dump_events()
            self.app()
        elif command == "6":
            self.list_event_files()
            self.app()
        elif command == "7":
            self.verify_events()
            self.app()
        elif command == "8":
            self.total_words()
            self.app()
        elif command == "9":
            self.list_all_characters()
            self.app()
        elif command == "10":
            self.characters_in_event()
            self.app()
        elif command == "0":
            exit(1)
        else:
            print("Command not found.")
            self.app()


    def search_event_name(self):
        print("\nPlease enter the event name. (example: 'beachmas19')")
        print("To go back type 'exit'.")
        name = input("> ")
        if name == "exit":
            self.app()
        else:
            for ren_file in self.ren_files:
                events = ren_file.get_events()
                for event in events:
                    if event.name == name.lower():
                        print_event_info(event)

    def search_for_dialogue(self):
        print("\nPlease enter the dialogue you wish to search for (example: 'You're disgusting').")
        print("To go back type 'exit'.")
        diag = input("> ")
        if diag == "exit":
            self.app()
        else:
            for ren_file in self.ren_files:
                events = ren_file.get_events()
                for event in events:
                    full_line = event.get_full_line(diag)
                    if not full_line is None:
                        # Print event info
                        # Print dialogue info
                        print_event_info(event)
                        print_dialogue_info(event, full_line)
                        print("")

    def search_advanced_dialogue(self, search, dialogue):
        if search:
            print("\nPlease enter the dialogue you wish to search for (example: 'You're disgusting').")
            print("To go back type 'exit'.")
            diag = input("> ")
            if diag == "exit":
                self.app()
        else:
            diag = dialogue
        print("Please enter the character you wish to search for (example 'ami')")
        print("To go back type 'exit'.")
        chara = input("> ").lower()
        if chara == "exit":
            self.search_advanced_dialogue(True, "")
        else:
            character = self.get_character(chara)
            if character is None:
                print("Could not find character '" + chara + ".'")
                self.search_advanced_dialogue(False, diag)
            else:
                for ren_file in self.ren_files:
                    events = ren_file.get_events()
                    for event in events:
                        full_line = event.get_full_line(diag)
                        if (not full_line is None) and character.alias == event.get_character_from_full_line(full_line):
                            print_event_info(event)
                            print_dialogue_info(event, full_line)
                            print("")

    def list_all_characters(self):
        print("Collecting...")
        for character in self.characters:
            print("Name: " + character.name + ".")
            print("Alias: " + character.alias + ".")

    def get_character(self, name):
        for character in self.characters:
            if name == character.name.lower() or name == character.alias.lower():
                return character
    def dump_lines_event(self):
        print("Please enter the event name.")
        ev = input("> ")
        if ev == "exit":
            self.app()
        else:
            event = self.get_event(ev)
            if event is None:
                print("Event '" + ev + "' does not exist.")
                self.dump_lines_event()
            for line in event.lines:
                print(line.strip())
            print("\n")
    def dump_events(self):
        print("Please enter the event file name. (example: 'nikievents.rpy')")
        print("You can view all event files by using the 'List all event files.' command.")
        print("To go back type 'exit'.")
        ev_file = input("> ").lower()
        if not ev_file.endswith(".rpy"):
            ev_file = ev_file + ".rpy"
        print("Collecting...")
        for ren_file in self.ren_files:
            if ren_file.name.lower() == ev_file:
                for event in ren_file.get_events():
                    print(event.name)
    def list_event_files(self):
        print("Collecting...")
        for ren_file in self.ren_files:
            print(ren_file.name)
    def verify_events(self):
        for ren_file in self.ren_files:
            events = ren_file.get_events()
            for event in events:
                print_event_info(event)
                print("\n")
        # Not sure how python error handling works so...
        print("If no errors had occurred the verification has been successful.")

    def total_words(self):
        # This is not accurate compared to the Java version
        print("Calculating...")
        count = 0
        for ren_file in self.ren_files:
            event_words = 0
            ecount = 0
            for event in ren_file.get_events():
                ecount = ecount + 1
                words = event.get_word_count(self.characters)
                count = count + words
                event_words = event_words + words
            print("File: " + ren_file.name + " (" + str(event_words) + ")")

        if count == 0:
            print("Error: Could not retrieve word count. There is a problem with the code.")
        else:
            print("The current word count is approximately " + str(count))
            print("This does not include programming lines or DLC content (care packages)")

    def auto_enable_console(self):
        print("This tool will automatically enable scripting. Make sure the application has proper file permissions.")
        print("WARNING: This will write data onto your pc!")
        print("Please enter 'Y' to continue. Or type literally anything else to back out.")
        conf = input("> ")
        if conf.lower() == "y":
            print("Not yet supported. Use the Java version instead.")

    def head_pat_fix(self):
        print("This tool will automatically enable scripting. Make sure the application has proper file permissions.")
        print("WARNING: This will write data onto your pc!")
        print("Please enter 'Y' to continue. Or type literally anything else to back out.")
        conf = input("> ")
        if conf.lower() == "y":
            print("Not yet supported. Use the Java version instead.")

    def characters_in_event(self):
        print("Please enter the character you wish to search for (example: 'ami')")
        print("To go back type 'exit'.")
        chara = input("> ")
        if chara.lower() == "exit":
            self.app()
        else:
            character = self.get_character(chara)

            print("Collecting...")
            if character is None:
                print("Could not find character '" + chara + "'.")
                self.characters_in_event()
            else:
                for ren_file in self.ren_files:
                    events = ren_file.get_events()
                    for event in events:
                        if event.is_said_by_character(character):
                            print(event.name)

    def get_event(self, name):
        for ren_file in self.ren_files:
            events = ren_file.get_events()
            # I'm stupid
            for event in events:
                if name.lower() == event.name.lower():
                    return event

class Event:
    def __init__(self, name, filename, line_index):
        self.name = re.sub("\s\s+", " ", name).strip()
        self.filename = filename.replace("\\", "/")
        self.line_index = line_index + 1
        self.lines = []
        self.replay_name = "Unknown"
        game_dir = os.path.dirname(os.path.realpath("__file__")) + "/game/"
        self.screens = os.path.join(game_dir, "screens.rpy")

    # This is why the program takes forever to build cache.
    # If you know a better solution please fix
    def gather_replay_info(self):
        found = False
        failed = False
        rep_name = "Unknown"
        failed_name = ""

        fr = open(self.screens, encoding="utf8")
        for line in fr:
            line = re.sub("\s\s+", " ", line)
            line = line.strip()
            if line.lower().startswith("textbutton _(\"back\""): continue
            if line.lower().startswith("text _(\"-------------"): continue
            if line.startswith("if") and found:
                found = False
            if line.startswith("if " + self.name + " =="):
                found = True
            if (line.startswith("textbutton _") or line.startswith("text _")) and found:
                rep_name = line.replace("textbutton _", "").replace(":", "").replace("{b}", "").replace("{/b}", "").replace("{i}", "").replace("{/i}", "").replace("{s}", "").replace("{/s}", "").replace("text _", "").replace("{color=778EFF}", "").replace("{/color}", "")
            if line.startswith("elif") and found:
                found = False
                failed = True
            if (line.startswith("text _")) and failed:
                failed_name = failed_name.replace("text _(\"", "").replace(":", "").replace("\"", "").replace("{color=EF1A1A}{s}", "").replace("{/s}{/color}", "")
                failed = False
                found = False
            if not rep_name == failed_name and not failed_name == "":
                self.replay_name = "'" + rep_name + "' Or '" + failed_name + "'"
            else:
                self.replay_name = rep_name
        self.screens = []
        self.replay_name = self.replay_name.replace("(\"", "").replace("\")", "")
    def add_line(self, line):
        line = line.replace("’", "'").replace("“", "")
        line = line.replace("{s}", "").replace("{/s}", "").replace("{i}", "").replace("{/i}", "").replace("{b}", "").replace("{/b}", "")
        self.lines.append(line)

    def get_lines(self):
        return self.lines

    def contains_line(self, line):
        return line in self.lines

    def get_full_line(self, diag):
        for line in self.lines:
            if diag.lower() in line.lower():
                return line

    def get_character_from_full_line(self, line):
        alias = line.split("\"")[0]
        alias = re.sub("\s\s+", " ", alias)
        alias = alias.strip()
        return alias.lower()

    def get_line_number(self, full_line):
        index = self.lines.index(full_line)
        return index + self.line_index

    def get_replay_name(self):
        return self.replay_name

    def get_word_count(self, characters):
        count = 0
        for line in self.lines:
            line = re.sub("\s\s+", "", line)
            line = line.strip()
            prgm = True
            for character in characters:
                if line.startswith(character.alias + " \""):
                    line = line.replace(character.alias + " \"", "")
                    prgm = False
                elif line.startswith("\"") and line.endswith("\""):
                    prgm = False
            if not prgm:
                split = line.split(" ")
                count = count + len(split)
        return count

    def is_said_by_character(self, character):
        for line in self.lines:
            line = re.sub("\s\s+", " ", line)
            line = line.strip()
            alias = line.split(" \"")
            if len(alias) > 0:
                alias = alias[0]
                alias = re.sub("\s\s+", " ", alias)
                if character.alias == alias:
                    return True


class Character:
    def __init__(self, name, alias):
        self.name = name
        self.alias = alias

class RenFile:

    def __init__(self, name):
        self.file = name
        name = name.replace("\\", "/")
        split = name.split("/")
        index = len(split)
        name = split[index - 1]
        self.name = name
        self.events = []
        self.collect_events()

    def collect_events(self):
        filer = open(self.file, encoding="utf8")
        count = 0
        event = 0
        for line in filer:
            count = count + 1
            # Removes excessive white spaces
            line = re.sub("\s\s+", " ", line)
            line = line.strip()
            if line.startswith("label "):
                event_name = line.replace("label ", "").replace(":", "")
                event_name = event_name.strip()
                event = Event(event_name, self.name, count)
                self.events.append(event)
            elif line.startswith("jump"):
                if event != 0:
                    event.add_line(line)
                event = 0
            else:
                if event != 0:
                    event.add_line(line)

    def get_events(self):
        return self.events


if __name__ == '__main__':
    main()