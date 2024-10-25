package me.anon.lil;

import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

public class App {

    public App() {
        System.out.println();
        System.out.println("Thank you for using my tool. Please ensure you downloaded this with the source version.");
        System.out.println("The current version is 3.0 (yes I made 3 other versions of this).");
        System.out.println();
        System.out.println("IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT IMPORTANT");
        System.out.println("Please do not re-distribute this. You are not allowed to post or upload this anywhere.");
        System.out.println("The current supported versions are chapters 1-4. Run the 'verify events' to ensure the program works.");
        System.out.println();
        System.out.println("Remember, God Is Dead. Praise be! ssssssssssssssssss ttttttttttttttttttttttt");
        System.out.println();
        System.out.println();
        baseCommand(true);
    }

    public void baseCommand(boolean showToolTip) {
        if (showToolTip) {
            System.out.println("Please enter the command number (1-20), you wish to execute.");
            System.out.println("  1. Search for event name.");
            System.out.println("  2. Search for dialogue.");
            System.out.println("  3. Advanced dialogue search.");
            System.out.println("  4. Dump all lines from an event.");
            System.out.println("  5. Dump events.");
            System.out.println("  6. List all event files.");
            System.out.println("  7. Verify events.");
            System.out.println("  8. Get current word count.");
            System.out.println("  9. List all characters.");
            System.out.println("  10. Automatically enable renpy console.");
            System.out.println("  11. Manually enable renpy console.");
            System.out.println("  12. List all events containing a character.");
            System.out.println("  13. Faster head-patting.");
            System.out.println("  19. Help and bug information.");
            System.out.println("  0. Exit.");
        }
        System.out.println();
        System.out.print("> ");
        System.gc();
        Scanner scanner = new Scanner(System.in);
        while (scanner.hasNextLine()) {
            String command = scanner.nextLine();
            if (command.equalsIgnoreCase("1")) {
                searchForEvent(scanner);
                break;
            } else if (command.equalsIgnoreCase("2")) {
                searchForLine(scanner);
                break;
            } else if (command.equalsIgnoreCase("3")) {
                detailSearchLine(scanner);
                break;
            } else if (command.equalsIgnoreCase("4")) {
                dumpLinesFromEvent(scanner);
                break;
            } else if (command.equalsIgnoreCase("5")) {
                dumpEventsFromFile(scanner);
                break;
            } else if (command.equalsIgnoreCase("6")) {
                listEventFiles();
                break;
            } else if (command.equalsIgnoreCase("7")) {
                verifyEvents();
                break;
            } else if (command.equalsIgnoreCase("8")) {
                getTotalWordCount();
                baseCommand(true);
                break;
            } else if (command.equalsIgnoreCase("9")) {
                listCharacters();
                break;
            } else if (command.equalsIgnoreCase("10")) {
                enableScripting(scanner);
                baseCommand(true);
                break;
            } else if (command.equalsIgnoreCase("11")) {
                scriptingTutorial();
                baseCommand(true);
                break;
            } else if (command.equalsIgnoreCase("12")) {
                allEventsWithCharacter(scanner);
                baseCommand(true);
                break;
            } else if (command.equalsIgnoreCase("13")) {
                fasterHeadPat(scanner);
                baseCommand(true);
                break;
            } else if (command.equalsIgnoreCase("19")) {
                System.out.println("    Help Information");
                System.out.println("If you are running into issues with the program please run 'Verify events.' If you get errors during the command, this program will not work with your version of the game." +
                        "Supported chapter are 1-4.");
                System.out.println("Please ensure you are running this program inside of your lessons in love directory. The jar file should be in the same place as the .exe file used to open the game.");
                System.out.println();
                System.out.println("    Known Issues");
                System.out.println("The replay information can be inaccurate. It can be displayed improperly or set to 'Unknown'. If the replay is Unknown, the event does not have a replay. For example, when you talk to the characters in the dorm you get a" +
                        " generic event. This generic event does not have a replay as it is generic.");
                System.out.println("Chapter 2 events may display as chapter 1 events. This is because there are few chapter 2 events which are located in 'scripts.rpy'. This script file is the chapter 1 script file." +
                        " Sel did not organize the game well when he made the new chapter (no disrespect to him, the game works with how he did it. It just makes this tool a little inaccurate).");
                baseCommand(true);
            } else if (command.equalsIgnoreCase("0")) {
                System.exit(0);
                break;
            } else {
                System.out.println("Invalid command.");
                baseCommand(false);
            }
        }
    }

    public void searchForEvent(Scanner scanner) {
        System.out.println("Please enter the event name. (example: 'beachmas19')");
        System.out.println("To go back type 'exit'.");
        System.out.println();
        System.out.print("> ");

        String event = scanner.nextLine();
        if (event.equalsIgnoreCase("exit")) {
            baseCommand(true);
            return;
        }

        System.out.println("Searching for '" + event + "'");
        for (RenFile renFile : Main.getRenFiles()) {
            for (Event event1 : renFile.getEvents()) {
                if (event1.getName().equalsIgnoreCase(event)) {
                    printEventInfo(event1);
                    break;
                }
            }
        }
        System.out.println();
        searchForEvent(scanner);
    }

    public void searchForLine(Scanner scanner) {
        System.out.println("Please enter the dialogue you wish to search for (example: 'You're disgusting').");
        System.out.println("To go back type 'exit'.");
        System.out.println();
        System.out.print("> ");

        String line = scanner.nextLine();
        if (line.isEmpty() || line.equalsIgnoreCase(" ")) {
            searchForLine(scanner);
            return;
        }

        if (line.equalsIgnoreCase("exit")) {
            baseCommand(true);
            return;
        }

        System.out.println("Searching for '" + line + "'");

        for (RenFile renFile : Main.getRenFiles()) {
            for (Event event : renFile.getEvents()) {
                for (String s : event.getLines()) {
                    if (s.toLowerCase().contains(line.toLowerCase())) {
                        printEventInfo(event);
                        printDialogueInfo(event, line);
                    }
                }
            }
        }

        // Once done repeat
        System.out.println();
        searchForLine(scanner);
    }

    public void detailSearchLine(Scanner scanner) {
        System.out.println("Please enter the dialogue you wish to search for (example: 'You're disgusting').");
        System.out.println("Type 'exit' to go back.");
        System.out.print("> ");
        String line = scanner.nextLine();
        if (line.equalsIgnoreCase("exit")) {
            baseCommand(true);
            return;
        }
        System.out.println();
        System.out.println("Please enter the character you wish to search for (example 'ami')");
        System.out.println("Type 'exit' to go back.");
        System.out.print("> ");
        String chara = scanner.nextLine();
        if (chara.equalsIgnoreCase("exit")) {
            detailSearchLine(scanner);
            return;
        }

        Character character = Character.getCharacter(chara);
        if (character == null) {
            System.out.println("ERROR: Character '" + chara + "' does not exist.");
            detailSearchLine(scanner);
            return;
        }

        System.out.println("Character: " + character.getName());
        System.out.println("Character Alias: " + character.getAlias() + ".");

        System.out.println("Character found. Searching...");

        for (RenFile renFile : Main.getRenFiles()) {
            for (Event event : renFile.getEvents()) {
                for (String s : event.getLines()) {
                    if (s.toLowerCase().contains(line.toLowerCase())) {
                        s = s.trim();
                        String alias = s.split("\"")[0];
                        alias = alias.trim();
                        if (alias.equalsIgnoreCase(character.getAlias())) {
                            printEventInfo(event);
                            printDialogueInfo(event, s);
                        }
                    }
                }
            }
        }
        System.out.println();
        System.out.println();
        detailSearchLine(scanner);
    }

    public void dumpEventsFromFile(Scanner scanner) {
        System.out.println("Please enter the event file name. (example: 'nikievents.rpy')");
        System.out.println("You can view all event files by using the 'List all event files.' command.");
        System.out.println("To go back type 'exit'.");
        System.out.println();
        System.out.print("> ");
        String fileName = scanner.nextLine();

        if (!fileName.endsWith("rpy")) {
            fileName = fileName + ".rpy";
        }

        boolean found = false;
        for (RenFile renFile : Main.getRenFiles()) {
            if (renFile.getFile().getName().toLowerCase().equalsIgnoreCase(fileName)) {
                found = true;
                for (Event event : renFile.getEvents()) {
                    System.out.println("Event: " + event.getName());
                }
            }
        }

        if (!found) {
            System.out.println("Could not find file '" + fileName + "'.");
            dumpEventsFromFile(scanner);
            return;
        }
        System.out.println();
        System.out.println();
        baseCommand(true);
    }

    public void dumpLinesFromEvent(Scanner scanner) {
        System.out.println("Please enter the event name. (example: 'beachmas19')");
        System.out.println("To go back type 'exit'.");
        System.out.println();
        System.out.print("> ");
        String eventName = scanner.nextLine();
        for (RenFile renFile : Main.getRenFiles()) {
            for (Event event : renFile.getEvents()) {
                if (event.getName().toLowerCase().contains(eventName)) {
                    System.out.println("Line amount: " + event.getLines().size());
                    for (String s : event.getLines()) {
                        System.out.println(s);
                    }
                }
            }
        }
        System.out.println();
        System.out.println();
        baseCommand(true);
    }

    public void listEventFiles() {
        System.out.println("Showing all event files...");
        for (RenFile renFile : Main.getRenFiles()) {
            System.out.println(renFile.getFile().getName());
        }
        System.out.println();
        System.out.println();
        baseCommand(true);
    }

    public void listCharacters() {
        for (Character character : Character.getCharacters()) {
            System.out.println("Character: " + character.getName());
            System.out.println("Character Alias: " + character.getAlias());
            System.out.println("Character File: " + character.getFileName());
            System.out.println();
            System.out.println();
        }
        baseCommand(true);
    }

    public void verifyEvents() {
        boolean verify = true;
        for (RenFile renFile : Main.getRenFiles()) {
            System.out.println("Verifying " + renFile.getFile().getName());
            for (Event event : renFile.getEvents()) {
                try {
                    printEventInfo(event);
                } catch (Exception ignored) {
                    verify = false;
                }
            }
        }
        System.out.println();
        if (!verify) {
            System.out.println("ERROR: There was an error verifying the events. This tool may not work properly, use with discretion.");
        } else {
            System.out.println("All events verified successfully.");
        }
        System.out.println();
        baseCommand(true);
    }

    public void fasterHeadPat(Scanner scanner) {
        System.out.println("This will modify the head-pat minigame to increase the increment of head-pats to five.");
        System.out.println("To do this, the program will need to write data onto your pc.");
        System.out.println("Please enter 'Y' to continue or literally anything else to go back.");
        System.out.print("> ");
        String conf = scanner.nextLine();
        if (!conf.equalsIgnoreCase("y")) {
            if (conf.equalsIgnoreCase("anything else")) {
                System.out.println("Smart ass.");
            }
            baseCommand(true);
            return;
        }
        System.out.println("Verifying file...");
        File headPatFile = new File(System.getProperty("user.dir") + "/game/headpatcentral.rpy");
        if (!headPatFile.exists()) {
            System.out.println("ERROR: Could not verify file.");
            baseCommand(true);
            return;
        }
        if (!headPatFile.delete()) {
            System.out.println("ERROR: Unable to delete file. Please ensure the program has file permissions.");
            baseCommand(true);
            return;
        }
        LinkedList<String> lines = new LinkedList<>();
        try {
            // Get file from resources using class path
            // java.io.InputStream
            ClassLoader classloader = Thread.currentThread().getContextClassLoader();

            InputStream inputStream = classloader.getResourceAsStream("headpatcentral.rpy");
            InputStreamReader streamReader = new InputStreamReader(inputStream, StandardCharsets.UTF_8);
            BufferedReader reader = new BufferedReader(streamReader);
            for (String line; (line = reader.readLine()) != null; ) {
                lines.add(line);
            }
        } catch (IOException e) {
            System.out.println("ERROR: Could not write file. Please ensure the program has file permissions.");
            System.out.println(e.getMessage());
        }
        try {
            FileWriter writer = new FileWriter(headPatFile);
            for (String s : lines) {
                writer.write(s);
                writer.write("\n");
            }
            writer.close();
            System.out.println("Successfully written file!");
        } catch (IOException e) {
            System.out.println("ERROR: Could not write file. Please ensure the program has file permissions.");
            System.out.println(e.getMessage());
        }
        System.out.println();
        System.out.println();
        baseCommand(true);
    }

    public static void allEventsWithCharacter(Scanner scanner) {
        System.out.println("Please enter the character you wish to search for: ");
        System.out.print("> ");
        String chara = scanner.nextLine();
        Character character = Character.getCharacter(chara);
        if (character == null) {
            System.out.println("ERROR: No such character '" + chara + "'.");
            allEventsWithCharacter(scanner);
            return;
        }
        System.out.println("Collecting...");
        List<Event> events = new ArrayList<>();
        for (RenFile renFile : Main.getRenFiles()) {
            for (Event event : renFile.getEvents()) {
                if (event.saidByCharacter(character)) {
                    events.add(event);
                }
            }
        }

        for (Event event : events) {
            System.out.println(event.getName());
        }
        System.out.println();
        System.out.println();
    }

    public void printEventInfo(Event event) {
        System.out.println("Event: " + event.getName());
        if (EventLocation.getEventLocation(event.getFile().getName()) != null) {
            System.out.println("  Location: " + EventLocation.getEventLocation(event.getFile().getName()).getName());
        } else {
            if (Character.getEventLocation(event.getFile()) != null) {
                System.out.println("  Location: " + Character.getEventLocation(event.getFile()).getDisplayFileName());
            } else {
                System.out.println("  Location: Unknown");
            }
        }
        System.out.println("  File: " + event.getFile().getName());
        System.out.println("  Event Line Number: " + event.getLi());
        System.out.println("  Replay Name: " + event.getReplay());
    }

    public void printDialogueInfo(Event event, String line) {
        System.out.println("  Line: " + event.getFullLine(line).trim());
        System.out.println("  Line Number: " + event.getLineIndex(line));
        System.out.println();
        System.out.println();
    }

    public void scriptingTutorial() {
        System.out.println("To enable the developer console for RenPy please open your lessons in love folder (where the exe is located).");
        System.out.println("Navigate to the renpy folder and search for the file called '00console.rpy'");
        System.out.println("Open this file with any text editor (note default notepad is trash I recommend note++).");
        System.out.println("Search for the line (ctr+f) 'config.console ='");
        System.out.println("You should eventually find the following lines:");
        System.out.println("init -1500 python:\n" +
                "\n" +
                "    # If true, the console is enabled despite config.developer being False.\n" +
                "    config.console = False");
        System.out.println("Change the false value to 'True'.");
        System.out.println("Save the file (ctrl+s) and restart your game if it's opened.");
        System.out.println("Once in game open your save and close any menus. Press 'shift+O' (it's o (oh) not zero hard to tell sometimes).");
        System.out.println("Congrats! You are now a cheater. You can type in commands here but you will need to know how python works.");
        System.out.println();
        System.out.println();
    }

    public void enableScripting(Scanner scanner) {
        System.out.println("This tool will automatically enable scripting. Make sure the application has proper file permissions.");
        System.out.println("WARNING: This will write data onto your pc!");
        System.out.println("Please enter 'Y' to continue. Or type literally anything else to back out.");
        System.out.print("> ");
        String conf = scanner.nextLine();
        if (conf.equalsIgnoreCase("y")) {
            System.out.println("Verifying file...");
            File conFile = new File(System.getProperty("user.dir") + "/renpy/common/00console.rpy");
            if (!conFile.exists()) {
                System.out.println("ERROR: Could not locate script file. This program cannot enable scripting for you.");
                baseCommand(true);
                return;
            }
            System.out.println("Deleting file...");
            if (!conFile.delete()) {
                System.out.println("ERROR: Could not delete file. Please close your game.");
                baseCommand(true);
                return;
            }
            LinkedList<String> lines = new LinkedList<>();
            try {
                // Get file from resources using class path
                // java.io.InputStream
                ClassLoader classloader = Thread.currentThread().getContextClassLoader();
                InputStream inputStream = classloader.getResourceAsStream("00console.rpy");
                InputStreamReader streamReader = new InputStreamReader(inputStream, StandardCharsets.UTF_8);
                BufferedReader reader = new BufferedReader(streamReader);
                for (String line; (line = reader.readLine()) != null; ) {
                    lines.add(line);
                }
            } catch (IOException e) {
                System.out.println("ERROR: Could not write file. Please ensure the program has file permissions.");
                System.out.println(e.getMessage());
            }
            try {
                FileWriter writer = new FileWriter(conFile);
                for (String s : lines) {
                    writer.write(s);
                    writer.write("\n");
                }
                writer.close();
                System.out.println("Successfully written file!");
            } catch (IOException e) {
                System.out.println("ERROR: Could not write file. Please ensure the program has file permissions.");
                System.out.println(e.getMessage());
            }
            System.out.println();
            System.out.println();
            baseCommand(true);
        } else {
            if (conf.equalsIgnoreCase("literally anything else")) {
                System.out.println("Smart ass.");
            }
            System.out.println();
            System.out.println();
        }
    }

    public void getTotalWordCount() {
        System.out.println("Calculating...");
        int wordCount = 0;
        for (RenFile renFile : Main.getRenFiles()) {
            int eventWordCount = 0;
            int words = 0;
            for (Event event : renFile.getEvents()) {
                words = event.getWordCount();
                wordCount += words;
                eventWordCount += words;
            }
            System.out.println("File: " + renFile.getFile().getName() + " (" + eventWordCount + ")");
        }

        System.out.println("The current word count is approximately " + wordCount);
        System.out.println("This does not include programming lines or DLC content (care packages).");
        System.out.println();
        System.out.println();
    }
}
