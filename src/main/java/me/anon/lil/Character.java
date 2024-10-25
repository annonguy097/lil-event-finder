package me.anon.lil;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.util.*;

public class Character {
    private final String alias;
    private final String name;
    private final String fileName;

    private final static Collection<Character> characters = new HashSet<>();

    public Character(String alias, String name) {
        this.alias = alias;
        this.name = name;
        String file = name + "Events.rpy";
        File verifyFile = new File(System.getProperty("user.dir") + "/game/" + file);
        if (!verifyFile.exists()) {
            this.fileName = "N/A";
        } else {
            this.fileName = file;
        }
    }

    public static void loadCharacters() {
        // All characters are defined in definitions.rpy
        try {
            List<String> lines = Files.readAllLines(new File(System.getProperty("user.dir") + "/game/definitions.rpy").toPath());

            for (String s : lines) {
                if (s.trim().startsWith("define ") && s.contains("Character(")) {
                    // Character found!
                    s = s.trim(); // Trim removes excessive spaces.
                    s = s.replace("define", "");
                    // Now we have x = Character(
                    // Get x
                    String[] keyValue = s.split("=", 2);
                    String alias = keyValue[0].trim();

                    // Now to dissect the value to get the character name
                    String value = keyValue[1];
                    value = value.trim();
                    value = value.replace("Character(", "");
                    // Now we should have "Maya", color="#18b500", who_outlines=[(absolute(2.5), "#000", absolute(0), absolute(0))])
                    // Each character has 7 parameters so we can just split base on the parameter
                    String[] params = value.split(",");
                    String characterName = params[0].replace("\"", ""); // Remove the quotes

                    // Create the character
                    characters.add(new Character(alias, characterName));
                }
            }

            lines.clear(); // Clear resource usage

        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public String getName() {
        return name;
    }

    public String getAlias() {
        return alias;
    }

    public String getFileName() {
        return fileName;
    }

    public String getDisplayFileName() {
        String[] eventSplit = fileName.replace(".rpy", "").split("Events");
        String chara = eventSplit[0];
        return chara + ' ' + "Event";
    }

    public static Character getEventLocation(File file) {
        return characters.stream().filter(characters -> characters.getFileName().equalsIgnoreCase(file.getName())).findAny().orElse(null);
    }

    public static Collection<Character> getCharacters() {
        return characters;
    }

    public static Character getCharacter(String name) {
        return characters.stream().filter(character -> character.getName().equalsIgnoreCase(name)).findAny().orElse(characters.stream().filter(character -> character.getAlias().equalsIgnoreCase(name)).findAny().orElse(null));
    }
}
