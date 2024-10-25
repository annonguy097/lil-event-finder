package me.anon.lil;

import java.io.File;
import java.lang.management.MemoryUsage;
import java.util.*;
import java.util.logging.MemoryHandler;

public class Main {
    private static final LinkedHashSet<RenFile> renFiles = new LinkedHashSet<>();

    public static void main(String[] args) {
        // Verify game folder
        File gameDirectory = new File(System.getProperty("user.dir") + "/game/");
        if (!gameDirectory.exists()) {
            System.out.println("ERROR: Could not find game directory. Please place the jar file inside of your lessons in love folder.");
            return;
        }
        System.out.println("Caching scripts...");
        TreeMap<String, File> renpyFiles = new TreeMap<>();
        for (File file : gameDirectory.listFiles()) {
            if (file.getName().endsWith("rpy")) {
                renpyFiles.put(file.getName().toLowerCase(), file);
            }
        }

        File nfswRenpyFiles = new File(gameDirectory, "scripts/subscribestar/");
        for (File file : nfswRenpyFiles.listFiles()) {
            if (file.getName().endsWith("rpy")) {
                renpyFiles.put(file.getName().toLowerCase(), file);
            }
        }

        // Only going to explain gc once and that is here.
        // This program caches A LOT of text and variables. Some variables are un-needed and can be disposed of.
        // gc = Garbage Collection. GC is the process of removing stored references in memory like objects that are no longer being used.
        // GC helps keep the applications resource usage low.
        // It is recommended to start the application with the java param -Xmx1G
        // Why is this necessary? The game is massive. 100mb~ of code alone.
        System.gc();

        System.out.println("Collected " + renpyFiles.size() + " scripts.");

        System.out.println("Building event cache... (This may take several minutes depending on your hardware configuration)");

        for (File file : renpyFiles.values()) {
            // Gather events for file

            // Exclude pointless files which contain no events.
            // This does not interfere with game files and only reads the data in them.
            // There is no writing or modifications to the game.
            if (file.getName().contains("autopatch") || file.getName().contains("checker") ||
                    file.getName().contains("definitions") || file.getName().contains("dlcmenu.rpy") ||
                    file.getName().contains("gui") || file.getName().contains("jukebox") || file.getName().contains("newchecker") || file.getName().contains("options") ||
                    file.getName().contains("profile_outfits") || file.getName().contains("screens") ||
                    file.getName().contains("unlockables") || file.getName().contains("setup")) {
                continue;
            }
            try {
                renFiles.add(new RenFile(file));
            } catch (OutOfMemoryError error) {
                System.out.println("ERROR: Your PC does not have enough resources to use this tool. Close other applications and try again.");
                System.exit(1);
                break;
            }
        }

        System.gc();

        // This is very pointless and I could just make a static int and save myself this pointless loop.
        int count = 0;
        for (RenFile renFile : renFiles) {
            for (Event ignored : renFile.getEvents()) {
                count++;
            }
        }

        System.out.println("Collected " + count + " events.");

        System.out.println("Caching characters...");
        try {
            Character.loadCharacters();
        } catch (OutOfMemoryError e) {
            System.out.println("ERROR: Your PC does not have enough resources to use this tool. Close other applications and try again.");
            System.exit(1);
            return;
        }
        System.out.println("Collected " + Character.getCharacters().size() + " characters.");

        System.gc();

        new App();
    }

    public static Collection<RenFile> getRenFiles() {
        return renFiles;
    }
}
