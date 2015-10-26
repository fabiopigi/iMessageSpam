on run argv
	tell application "Messages"
		set contact to buddy (item 1 of argv) of service "E:your@appleID.com"
		set mes to (item 2 of argv)
		send mes to contact
	end tell
end run