package me.anon.lil;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.util.ArrayList;
import java.util.List;

public class Event {
    private final String name;
    private final File file;
    private final int li;
    private String replay;
    private final List<String> lines = new ArrayList<>();

    // Cache the screens.rpy file
    private final List<String> screens;

    public Event(String name, File file, int li) {
        this.name = name;
        this.file = file;
        this.li = li;
        try {
            screens = Files.readAllLines(new File(System.getProperty("user.dir") + "/game/screens.rpy").toPath());
            gatherReplayInfo();
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public void gatherReplayInfo() {
        // This will get the replay-name from the game files
        // All the replay information is stored in screens.rpy
        // if 'event' == true {
        //    // Replay button if they completed the event
        // } else {
        //   They have no completed the event and there is no alternative.
        // }
        // if 'event' == true {
        //    // Replay button if they completed the event
        // } elif {
        //   They missed the event. (The elif statement is not included for every event and signifies if an event can be missed.)
        // }
        // if cafe35 == True:
        //    textbutton _("I Died With You {b}✓{/b}"):
        //    text_style "mybutton"
        //    action Replay("cafe35", locked=False)
        // elif rindorm35 == True and rininvite == False:
        //    text _("{color=EF1A1A}{s}Love Life, Let Go{/s}{/color}")
        // else:
        //    text _("I Died With You")
        //
        //
        // None of this makes sense because I was on coke when I wrote it.
        // If it breaks for future updates then all I have to say is... Nose blows not it.
        boolean found = false;
        boolean failed = false;
        String replayName = "Unknown";
        String failedName = "";

        for (String s : screens) {
            // Forced filters. These were causing display issues.
            if (s.trim().toLowerCase().startsWith("textbutton _(\"back\")")) continue;
            if (s.trim().toLowerCase().startsWith("text _(\"----------")) continue;

            if (s.trim().startsWith("if") && found) {
                found = false;
            }
            if (s.trim().startsWith("if " + this.name + " ==")) {
                found = true;
            }

            if ((s.trim().startsWith("textbutton _") || s.trim().startsWith("text _")) && found) {
                replayName = s.trim().replace("textbutton _", "").replace(":", "").replace("{b}", "").replace("{/b}", "").replace("✓", "").replace("\"", "").strip();
                replayName = replayName.replace("text _", "");
                replayName = replayName.replace("{color=778EFF}", "").replace("{/color}", "");
                if (replayName.startsWith("(")) {
                    replayName = replayName.substring(1).strip();
                }

                if (replayName.endsWith(")")) {
                    replayName = replayName.substring(0, replayName.length() - 1).strip();
                }
            }

            if (s.trim().startsWith("elif") && found) {
                found = false;
                failed = true;
            }


            if (s.trim().startsWith("text _") && failed) {
                failedName = s.trim().replace("text _(\"", "").replace(":", "").replace("\"", "");
                failedName = failedName.replace("{color=EF1A1A}{s}", "").replace("{/s}{/color}", "");
                if (failedName.startsWith("(")) {
                    failedName = failedName.substring(1);
                }

                if (failedName.endsWith(")")) {
                    failedName = failedName.substring(0, failedName.length() - 1);
                }

                failed = false;
                found = false;
            }
        }

        if (!replayName.equalsIgnoreCase(failedName) && !failedName.isEmpty()) {
            this.setReplay("'" + replayName + "' Or '" + failedName + "'");
        } else {
            this.setReplay(replayName);
        }

        screens.clear(); // Clear to reduce memory usage
    }

    public String getReplay() {
        return replay;
    }

    public void setReplay(String replay) {
        this.replay = replay;
    }

    public void addLine(String line) {
        // For whatever reason sel uses a different type of apostrophe which causes issues when searching for dialogue.
        // This simply takes that weird symbol he uses and converts it to the standard. '’' converts to '''.
        // Same with quotes '“' is converted to '"'
        // Also line formats like bold.
        lines.add(line.replace("’", "'").replace("“", "\"").
                replace("{i}", "").replace("{/i}", "").replace("{b}", "").
                replace("{/b}", "").replace("{s}", "").replace("{/s}", ""));
    }

    public boolean contains(String line) {
        for (String s : lines) {
            return s.toLowerCase().contains(line.toLowerCase());
        }

        return false;
    }

    public int getLineIndex(String line) {
        for (String s : lines) {
            if (s.toLowerCase().contains(line.toLowerCase())) {
                int index = lines.indexOf(s);
                return index + 1 + li + 1;
            }
        }

        return -1;
    }

    public boolean saidByCharacter(Character character) {
        for (String s : lines) {
            s = s.trim();
            String alias = s.split("\"")[0].trim();
            if (alias.equalsIgnoreCase(character.getAlias())) {
                return true;
            }
        }

        return false;
    }

    public String getFullLine(String line) {
        for (String s : lines) {
            if (s.toLowerCase().contains(line.toLowerCase())) {
                return s;
            }
        }

        return "";
    }

    // This will only get the word count of dialogue not programming lines
    public int getWordCount() {
        int toReturn = 0;
        for (String s : getLines()) {
            s = s.trim();
            boolean prg = true; // Programming line flag i.e $ var = 12
            // Does not include the character call
            // m "I'll find you again
            // Is converted to
            // I'll find you again
            for (Character character : Character.getCharacters()) {
                if (s.startsWith(character.getAlias() + " \"")) {
                    s = s.replace(character.getAlias() + " \"", "");
                    prg = false;
                } else if (s.trim().startsWith("\"") && s.endsWith("\"")) {
                    // Narration dialogue.
                    // "It’s too full of memories of her."
                    prg = false;
                }
            }
            if (!prg) {
                String[] words = s.split(" ");
                toReturn += words.length;
            }
        }
        return toReturn;
    }

    public String getName() {
        return name;
    }

    public File getFile() {
        return file;
    }

    public List<String> getLines() {
        return lines;
    }

    public int getLi() {
        return li + 1;
    }
}
