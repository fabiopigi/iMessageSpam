on run argv
	tell application "Messages"
		set contact to buddy (item 1 of argv) of service "E:your@appleID.com"
		set flagPosixPath to (item 2 of argv) as POSIX file
		send flagPosixPath to contact
	end tell
end run