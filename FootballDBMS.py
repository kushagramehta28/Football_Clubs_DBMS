import pymysql
conn = pymysql.connect (user = 'root', host = 'localhost', password = 'password')
cursor = conn.cursor()

def database(Database_name):
    St = 'Create database ' + Database_name
    cursor.execute(St)

def usedatabase(Database_name):
    St = "Use " + Database_name
    cursor.execute (St)
    
def table_details(Table_name, Table_fields):
    cursor.execute ("Create table" + " " + Table_name + " " + "(" + Table_fields + ")")
    conn.close()

def del_player(database, tablename, playername):
    St = "Use " + database
    cursor.execute(St)
    T = "delete from " + tablename + " where Player_name = '" + playername + "'"
    cursor.execute(T)

def add_field(table_name,field_name,field_type,field_limit):
    St = "alter table " + table_name + " add " + field_name + " " + field_type + "(" + field_limit + ")"
    cursor.execute(St)
    conn.close()

def add_field1(table_name,field_name,field_type,field_limit):
    St = "alter table " + table_name + " add " + field_name + " " + field_type 
    cursor.execute(St)
    conn.close()

ch = 'y'
while ch == 'y' or ch == 'Y':
    print ("1. Create a database for your club.")
    print ("2. Create tables for your team.")
    print ("3. Enter data in a table.")
    print ("4. Delete transferred player details.")
    print ("5. Forgot to add a field? Add it now.")
    print ("6. Update player details.")
    print ("7. Print players stats.")

    x = int(input("\nWhat are you here for? "))

    if x == 1:
        Name = input("Enter database name - ")
        database(Name)
        print ("Your database ", Name, " is created :)")

    elif x == 2:
        Database = input("Which database do you want to add a table to? ")
        usedatabase(Database)
        TName = input("What name do you want to give to this table? ")
        print("\nPlease add field names in the following format")
        print("Player_name char(50), Field 2 <datatype>(<character limit>, ....")
        print("Please only use the above format and include Player_name in all tables with P in caps. Thank You :)")
        TFields = input("\nEnter field details - ")
        table_details(TName,TFields)
        print("Yay! Your table is created :)")
        
    elif x == 3:
        cont = 'y'
        while cont == 'y' or cont == 'Y': 
            Database = input("Which database do you want to use? ")
            usedatabase(Database)
            cursor.execute("show tables")
            J = cursor.fetchall()
            i = 1
            while i <= len(J):
                print ("Table ", i , " in this database is ", J[i-1][0])
                i += 1
            Taddname = input("Which table among these do you want to add records to? ")
            F = []
            rec = 'y'
            while rec == 'y' or rec == 'Y':
                T = []
                cursor.execute('desc ' + Taddname)
                G = cursor.fetchall()
                i = 0
                while i < len(G):
                    st = "Enter " + G[i][0] + " : "
                    k = input(st)
                    T.append(k)
                    i += 1
                F.append(T)
                print(F)
                rec = input("Do you want to add more records in same table? Y/N?")
            k = len(F[0])
            fr = "("
            i = 0
            while i < k:
                if i < k-1:
                    fr = fr + "%s,"
                else:
                    fr = fr + "%s)"
                i += 1 
            st = "insert into " + Taddname + " values" + fr
            i = 0
            while i < len(F):
                val = []
                k = 0
                while k < len(F[i]):
                    val.append(F[i][k])
                    k += 1
                cursor.execute(st,val)
                conn.commit()
                i += 1
            print ("All your records are added sir/madam :)")
            cont = input("Do you want to add more records in another table? Y/N?")

    elif x == 4:
        print("Oh! So you transferred a player?? Major bag alert haha")
        database = input("Enter database - ")
        Table = input("Enter table - ")
        Name = input("Enter player_name - ")
        del_player(database,Table,Name)

    elif x == 5:
        Database = input("Which database do you want to use? ")
        usedatabase(Database)
        cursor.execute("show tables")
        J = cursor.fetchall()
        i = 1
        while i <= len(J):
            print ("Table ", i , " in this database is ", J[i-1][0])
            i += 1
        Taddname = input("Which table among these do you want to add a field to? ")
        Tfield = input("Enter name of the field you want to create - ")
        print ("These are the datatypes - ")
        print ("char, integer, date, float")
        Ttype = input("Enter character type - ")
        Tlim = input("Do you want to add limit?Y/N? - ")
        if Tlim == "y" or Tlim == "Y":
            Tlim = input("Enter limit in numbers - ")
            add_field(Taddname,Tfield,Ttype,Tlim)
        elif Tlim == "n" or Tlim == "N":
            Tlim = ""
            add_field1(Taddname,Tfield,Ttype,Tlim)         
        
    elif x == 6:
        print("So, you made a mistake? Don't worry you can undo it :)")
        Database = input("Which database do you want to use? ")
        usedatabase(Database)
        cursor.execute("show tables")
        J = cursor.fetchall()
        i = 1
        while i <= len(J):
            print ("Table ", i , " in this database is ", J[i-1][0])
            i += 1
        Taddname = input("Which table among these do you want update records in? ")
        cursor.execute('desc ' + Taddname)
        G = cursor.fetchall()
        i = 1
        while i <= len(G):
            print ("Field ", i , " in this table is ", G[i-1][0])
            i += 1
        Fedit = input("Which field do you want to edit? - ")
        cursor.execute("select Player_name from " + Taddname)
        T = cursor.fetchall()
        i = 1
        while i <= len(T):
            print ("Name ", i , " in this table is ", T[i-1][0])
            i += 1
        k = "Enter for which person do you want to change " + Fedit + " - "
        Nedit = input(k)
        Nrec = input("Enter new record - ")
        L = [Nrec,Nedit]
        cursor.execute("update " + Taddname + " set " + Fedit + " = %s where Player_name = %s" , L)
        conn.commit()
        print ("Record is updated :)")

    elif x == 7:
        Database = input("Which database do you want to use? ")
        usedatabase(Database)
        cursor.execute("show tables")
        G = cursor.fetchall()
        i = 1
        while i <= len(G):
            print("Table ", i , " in this database is ", G[i-1][0])
            i += 1
        m = input("Do you have a player stats table already made? Y/N?")
        if m == "N" or m == 'n':
            print("Don't worry, we have made one for you :) Kindly add details.")
            cursor.execute("create table Player_stats(Name char(50), goals char(10), matches_played char(10), yellow_cards char(10), red_cards char(10), injuries char(10))")
            Taddname = "Player_stats"
            F = []
            rec = 'y'
            while rec == 'y' or rec == 'Y':
                T = []
                cursor.execute('desc ' + Taddname)
                G = cursor.fetchall()
                i = 0
                while i < len(G):
                    st = "Enter " + G[i][0] + " : "
                    k = input(st)
                    T.append(k)
                    i += 1
                F.append(T)
                print(F)
                rec = input("Do you want to add more records in same table? Y/N?")
            k = len(F[0])
            fr = "("
            i = 0
            while i < k:
                if i < k-1:
                    fr = fr + "%s,"
                else:
                    fr = fr + "%s)"
                i += 1 
            st = "insert into " + Taddname + " values" + fr
            i = 0
            while i < len(F):
                val = []
                k = 0
                while k < len(F[i]):
                    val.append(F[i][k])
                    k += 1
                cursor.execute(st,val)
                conn.commit()
                i += 1
            print ("All your records are added sir/madam :)")
        cursor.execute("select * from Player_stats")
        f = cursor.fetchall()
        print(f)
        p = input("Enter player name whose stats you want - ")
        i = 0
        G = []
        while i < len(f):
            if f[i][0] == p:
                G.append(f[i])
            i += 1
        if len(G) != 0:
            St = "----------------------------------------------------------------"
            print (St)
            k = "| Name - " + G[0][0] + "                          Matches Played - " + G[0][2]
            t = len(St)
            o = len(k)
            r = t - o
            D = ""
            i = 0
            while i < r:
                if i < r-1:
                    D += " "
                elif i < r:
                    D += "|"
                i += 1
            k = k + D
            print (k)
            print ("----------------------------------------------------------------")
            k = "| Average goals scored - " + str(int(G[0][1])/int(G[0][2]))
            t = len(St)
            o = len(k)
            r = t - o
            D = ""
            i = 0
            while i < r:
                if i < r-1:
                    D += " "
                elif i < r:
                    D += "|"
                i += 1
            k = k + D
            print (k)
            print (St)
            k = "| Average Yellow Cards taken - " + str(int(G[0][3])/int(G[0][2]))
            t = len(St)
            o = len(k)
            r = t - o
            D = ""
            i = 0
            while i < r:
                if i < r-1:
                    D += " "
                elif i < r:
                    D += "|"
                i += 1
            k = k + D
            print (k)
            print (St)
            k = "| Average Red Cards taken - " + str(int(G[0][4])/int(G[0][2]))
            t = len(St)
            o = len(k)
            r = t - o
            D = ""
            i = 0
            while i < r:
                if i < r-1:
                    D += " "
                elif i < r:
                    D += "|"
                i += 1
            k = k + D
            print (k)
            print (St)
            k = "| Average Injuries taken - " + str(int(G[0][5])/int(G[0][2]))
            t = len(St)
            o = len(k)
            r = t - o
            D = ""
            i = 0
            while i < r:
                if i < r-1:
                    D += " "
                elif i < r:
                    D += "|"
                i += 1
            k = k + D
            print (k)
            print (St)
        else:
            print("Record doesn't exist.")
            
    ch = input("Do you want to continue? Y/N?")

  


    
        
        
    
