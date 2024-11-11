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
parser.add_argument("-l", "--list", action="store_true")
parser.add_argument("-c", "--create", action="store_true")
parser.add_argument("-d", "--delete", type=int)

args = parser.parse_args()

if args.list:
	# get list of notes
	cursor.execute("SELECT * from `notes`")
	notes = cursor.fetchall()

	if (len(notes)):
		for note in notes:
			print("{0}. {1}".format(note[0], note[1]))
			print("Text: " + note[2])
			print("\n\n")
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
		except EOFError:
			break
		textNote += line + "\n"

	cursor.execute('''
		INSERT INTO `notes` (name, text) VALUES (?, ?)
	''', (nameNote, textNote))

	connection.commit() # save changes
elif args.delete is not None:
	# delete note with id
	cursor.execute("DELETE FROM `notes` WHERE id = ?", (args.delete,))

	connection.commit() # save changes

connection.close() # close connection
