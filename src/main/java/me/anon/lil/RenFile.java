package me.anon.lil;

import java.io.File;
import java.io.IOException;
import java.nio.file.Files;
import java.util.Collection;
import java.util.HashSet;
import java.util.List;

public class RenFile {
    private final File file;

    private final Collection<Event> events = new HashSet<>();

    public RenFile(File file) {
        this.file = file;
        scanEvents();
    }

    // all events inside the script beginning with label
    public void scanEvents() {
        // Scans and caches all the events for the file
        try {
            List<String> lines = Files.readAllLines(file.toPath());
            Event event = null;
            for (String s : lines) {
                if (s.trim().startsWith("label ")) {
                    // Event has been found...
                    String eventName = s.trim().replace("label ", "").replace(":", "");

                    event = new Event(eventName, file, lines.indexOf(s));

                    events.add(event);
                } else if (s.trim().startsWith("jump")) {
                    if (event != null) {
                        event.addLine(s);
                    }
                    event = null;
                } else {
                    if (event != null) {
                        event.addLine(s);
                    }
                }
            }

            lines.clear(); // clear to reduce memory usage
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public File getFile() {
        return file;
    }

    public Collection<Event> getEvents() {
        return events;
    }
}
