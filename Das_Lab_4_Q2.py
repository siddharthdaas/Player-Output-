# To import the sqlite package.

import sqlite3

# To define the method viewRecord() to view the records of the table.

def viewRecords(conn):

    #To execute the query to select the records ordered by

    #number of wins in descending order.

    cur = conn.execute("SELECT name,wins,losses,ties "+

    "FROM Player ORDER by wins desc")

    #Display the header of the table.

    print("{0:16}{1:10}{2:10}{3:10}{4:10}".format

    ("Name", "Wins", "Losses", "Ties", "Games"))

    print("-" * 60)

   

    #Start the for loop till the number of rows in

    #the cursor and display all the records.

    for r in cur:

        print("{0:10}{1:10}{2:12}{3:8}{4:11}".format

        (r[0].capitalize(), r[1], r[2], r[3], r[1]

         + r[2] + r[3]))

    print()

#To define the method addARecord() to add a record to the table

def addARecord(conn):

    #Get the cursor by calling the method cursor() using conn object.

    c = conn.cursor()

    #Get the name of the player.

    playerName = input("Name: ")

    #To execute a query to select the player with the input name.

    c.execute("SELECT name FROM Player WHERE name = ?",

    (playerName,))

    #To fetch all the rows from cursor object.

    data = c.fetchall()

    #If the length of the data is 0, then user input name is unique

    if len(data) == 0:

        #To get the number of wins, losses, ties from the user

        numWins = int(input("Wins: "))

        numLosses = int(input("Losses: "))

        numTies = int(input("Ties: "))

        #To store all 4 attributes in the database

        data = (playerName, numWins, numLosses, numTies)

        #Write the required insert query.

        insertQuery = 'INSERT INTO Player VALUES \
            (?,?,?,?)'

        #To execute the required insert query with user input data 

        conn.execute(insertQuery, data)

        #To display a message confirming that the record is added to database.

        print(playerName.capitalize(), " was added to "+

        "database.\n")

    #Otherwise, display an appropriate message.

    else:

        print("This name is already present in the "+

        "database.")

#To define the method deleteRecord() to delete a record.

def deleteRecord(conn):

    #To get the name of the player to delete the record.

    playerName = input("Name: ")

    #To execute the delete query.

    conn.execute("DELETE from Player where name =?",

    (playerName,))

    #To display a message showing that the record is deleted

    print(playerName.capitalize(), "was deleted from "+

    "database.\n")

#To define the method updateRecord() to update a record in the table

def updateRecord(conn):

    #Get the cursor by calling the method cursor() using

    #conn object.

    c = conn.cursor()

    #Get the name of the player to update its attributes.

    playerName = input("Enter a name of player whose "+

    "details you want to update: ")

    #Execute a query to select the player with the input

    #name.

    c.execute("SELECT name FROM Player WHERE name = ?",

    (playerName,))

    #Fetch all the rows from cursor object.

    data = c.fetchall()

    #If length of the data is 0, then user input name is

    #unique.

    if len(data) != 0:

   

        #Get the new number of wins, losses, ties from

        #the user.

        numWins = int(input("Enter new number of "+

        "wins: "))

        numLosses = int(input("Enter new number of "+

        "losses: "))

        numTies = int(input("Enter new number of "+

        "ties: "))

        #Store all 4 attributes in the data.

        data = (numWins, numLosses, numTies, playerName)

   

        #Write the required update query.

        updateQuery = '''UPDATE Player

                         SET wins = ?,

                             losses = ?,

                             ties = ?

                         WHERE name = ?'''

        #Execute the required update query with user

        #input data.

        c.execute(updateQuery, data)

        #Display a message confirming that the record is

        #updated to database.

        print("The record with the name ",

        playerName.capitalize(), " is updated.\n")

    #Otherwise, display an appropriate message.

    else:

        print("This name is not present in the "+

        "database.")

#Define the method displayMenu() to show the menu of

#choices.

def displayMenu():

    #Display the command menu.

    print("\nCOMMAND MENU")

    print("view - View Player")

    print("add - Add a Player")

    print("del - Delete a Player")

    print("update - Update a Player")

    print("exit - Exit Program\n")

#Define the main() function.

if __name__ == '__main__':

    print("Player Manager")

    #Establish a sqlite database connection and open the

    #database file players_Data.db.

    conn = sqlite3.connect('players_Data.db')

    #Execute the create table query to create a table

    #named as Player in the database.

    conn.execute('''CREATE TABLE IF NOT EXISTS Player

    (

        name   TEXT    NOT NULL,

        wins   INT     NOT NULL,

        losses INT     NOT NULL,

        ties   INT     NOT NULL

    );''')

    #Call the function displauMenu() to show the

    #command menu.

    displayMenu()

    #Start the while loop.

    while True:

        #Prompt the user to enter a command.

        inputCommand = input("Command: ")

        #If the command entered is view, then call the

        #function viewRecords() and pass the sqlite

        #database connection object conn.

        if inputCommand.lower() == "view":

            viewRecords(conn)

        #If the command entered is add, then call the

        #function addARecord() and pass the sqlite

        #database connection object conn.

        elif inputCommand.lower() == "add":

            addARecord(conn)

        #If the command entered is del, then call the

        #function deleteRecord() and pass the sqlite

        #database connection object conn.

        elif inputCommand.lower() == "del":

            deleteRecord(conn)

        #If the command entered is update, then call

        #the function updateRecord() and pass the

        #sqlite database connection object conn.

        elif inputCommand.lower() == "update":

            updateRecord(conn)

        #If the command entered is exit, then

        #display a message "bye!" and break the

        #while loop.

        elif inputCommand.lower() == "exit":

            print("Bye!")

            break

    #Close and commit the sqlite databse connection

    #using commit() and close() functions.

    conn.commit()

    conn.close()