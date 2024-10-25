package me.anon.lil;

import java.util.Arrays;

public enum EventLocation {
    CHAPTER1("Chapter 1", "script.rpy"),
    CHAPTER2("Chapter 2", "ch2script.rpy"),
    CHAPTER2FIN("Chapter 2", "finalwarning.rpy"),
    CHAPTER3("Chapter 3", "chap3.rpy"),
    CHAPTER3GEN("Chapter 3", "chap3generics.rpy"),
    CHAPTER4("Chapter 4", "chap4.rpy"),
    CHAPTER4HUB("Chapter 4", "chap4hub.rpy"),
    CHAPTER4GEN("Chapter 3", "chap4generics.rpy"),
    CHAP4RESET("Chapter 4", "senseiquest.rpy"),
    CHAP5("Chapter 5", "chap5.rpy"),
    DORM("Dorm", "DormEvents.rpy"),
    DORM2("Dorm 2", "Dorm2Events.rpy"),
    LUST("Lust", "inappropriatecontent.rpy"),
    LUSTNUDE("Lust", "nudes.rpy"),
    LUSTANIM("Lust", "animatedscenes.rpy"),
    HEADPAT("Head-pat", "headpatcentral.rpy")
    ;

    final String name;
    final String fileName;
    EventLocation(String name, String fileName) {
        this.name = name;
        this.fileName = fileName;
    }

    public String getName() {
        return name;
    }

    public String getFileName() {
        return fileName;
    }

    public static EventLocation getEventLocation(String fileName) {
        return Arrays.stream(values()).filter(eventLocation -> eventLocation.getFileName().equalsIgnoreCase(fileName)).findAny().orElse(null);
    }
}
