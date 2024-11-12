import sqlite3, argparse

# connection db
connection = sqlite3.connect("nts.db")
cursor = connection.cursor()

# create 'notes' table
cursor.execute('''
CREATE TABLE IF NOT EXISTS `notes` (
id INTEGER PRIMARY KEY,
name VARCHAR(255) NOT NULL,
text TEXT NOT NULL
);
''')

connection.commit() # save changes

# get arguments for app
parser = argparse.ArgumentParser()
parser.add_argument("-l", "--list", action="store_true", help="show list of notes")
parser.add_argument("-c", "--create", action="store_true", help="create new note")
parser.add_argument("-d", "--delete", type=int, metavar="ID", help="delete note by id")
parser.add_argument("-en", "--edit-name", type=int, metavar="ID", help="edit name note by id")
parser.add_argument("-et", "--edit-text", type=int, metavar="ID", help="edit text note by id")
parser.add_argument("-f", "--find", nargs="+", metavar="KEYWORDS", help="find note")

args = parser.parse_args()

if args.list:
	# get list of notes
	cursor.execute("SELECT * from `notes`")
	notes = cursor.fetchall()

	if (len(notes)):
		for note in notes:
			print("{0}. {1}".format(note[0], note[1]))
			print("Text: " + note[2])
			print("\n")
	else:
		print("The list is empty")
elif args.create:
	# create new note
	nameNote = input("Input name the note: ")

	# input multiline text
	print("Input text note (Ctrl + D or Ctrl + Z to save it):")
	textNote = ""

	while True:
		try:
			line = input()
			textNote += line + "\n"
		except EOFError:
			break

	cursor.execute("INSERT INTO `notes` (name, text) VALUES (?, ?)", (nameNote, textNote))

	connection.commit() # save changes
elif args.delete is not None:
	# delete note with id
	cursor.execute("DELETE FROM `notes` WHERE id = ?", (args.delete,))

	connection.commit() # save changes
elif args.edit_name is not None:
	# edit name note
	nameNote = input("Input new note name: ")

	cursor.execute("UPDATE `notes` SET name = ? WHERE id = ?", (nameNote, args.edit_name))

	connection.commit() #save changes
elif args.edit_text is not None:
	# edit text note
	print("Input updated text note (Ctrl + D or Ctrl + Z to save it):")
	textNote = ""

	# input multiline text
	while True:
		try:
			line = input()
			textNote += line + "\n"
		except EOFError:
			break

	cursor.execute("UPDATE `notes` SET text = ? WHERE id = ?", (textNote, args.edit_text))

	connection.commit() # save changes
elif args.find is not None:
	# find a notes by keyword
	cursor.execute("SELECT * FROM `notes`")
	notes = cursor.fetchall()

	i = 0

	# print notes which has substring
	for note in notes:
		print("keyword: {0}".format(args.find[i]))
		print("---------------------------------------------------------------")

		for keyword in args.find:
			if note[2].find(keyword) == -1:
				continue

			print("{0}. {1}".format(note[0], note[1]))
			print("Text: " + note[2])
			print("\n")

		print("===============================================================")
		i += 1

connection.close() # close connection
