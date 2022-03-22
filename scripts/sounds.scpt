#set theQuery to "DELL U2720QM"
#set theQuery to "MacBook Pro扬声器"
set theQuery to "慧泽的AirPods Pro"

tell application "System Preferences"
    reveal pane "声音"
end tell

tell application "System Events"
    tell application process "System Preferences"
        repeat until exists tab group 1 of window "声音"
        end repeat
        tell tab group 1 of window "声音"
            click radio button "输出"
            tell table 1 of scroll area 1
                select (row 1 where value of text field 1 is theQuery)
            end tell
        end tell
    end tell
end tell

if application "System Preferences" is running then
    tell application "System Preferences" to quit
end if

return theQuery
