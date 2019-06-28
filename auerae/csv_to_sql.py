import pandas as pd
import mysql.connector


def mysql_connect(hostname, name, passwd, path_to_db):

    try:

        conn = mysql.connector.connect(host=hostname, user=name,password=passwd)
        dataframe = pd.read_csv('uni_db.csv')

        if conn.is_connected():


            if  'UniversityDB' != conn.database:
                conn.cursor().execute("CREATE DATABASE UniversityDB")
            conn.database = 'UniversityDB'

            print(conn.database)
            mycursor = conn.cursor()
            mycursor.execute('SHOW TABLES')
            tables = mycursor.fetchall()
            existing_tbls = [x[0] for x in tables]

            if 'Students' not in existing_tbls:
                mycursor.execute("CREATE TABLE Students ( student_id INT NOT NULL, student_name VARCHAR(25)," +
                                                           "student_address VARCHAR(40), student_branch VARCHAR(40),"+
                                                            "PRIMARY KEY (student_id));")


            if 'Professors' not in existing_tbls:
                mycursor.execute("CREATE TABLE `Professors` ( professor_id INT NOT NULL, professor_name VARCHAR(25)," +
                                                          "subject VARCHAR(25), PRIMARY KEY (professor_id));")

            if 'Subjects' not in existing_tbls:
                mycursor.execute("CREATE TABLE Subjects ( subject_id INT NOT NULL, professor_id INT NOT NULL, " +
                                                        "PRIMARY KEY (subject_id), FOREIGN KEY (professor_id) REFERENCES " +
                                                        "Professors (professor_id) ON DELETE CASCADE) ENGINE=INNODB;")


            if 'Exams' not in existing_tbls:
                mycursor.execute("CREATE TABLE Exams (exam_id INT NOT NULL, exam_name VARCHAR(25), exam_marks INT NOT NULL," +
                                                      " PRIMARY KEY (exam_id)) ENGINE=INNODB ;")

            if 'Score' not in existing_tbls:
                mycursor.execute("CREATE TABLE Score ( score_id INT NOT NULL, student_id INT NOT NULL," +
                                                       "subject_id INT NOT NULL, marks INT NOT NULL," +
                                                       "exam_id INT NOT NULL,  PRIMARY KEY (score_id)," +
                                                       " FOREIGN KEY (student_id) REFERENCES " +
                                                       "Students (student_id) ON DELETE CASCADE," +
                                                       "FOREIGN KEY (subject_id) REFERENCES Subject (subject_id) " +
                                                       "ON DELETE CASCADE, FOREIGN KEY (exam_id) REFERENCES " +
                                                       "Exams (exam_id) ON DELETE CASCADE) ENGINE=INNODB;")



            mycursor.execute('SHOW TABLES')
            tables = mycursor.fetchall()
            existing_tbls = [x[0] for x in tables]
            print(existing_tbls)

            if "Students" in existing_tbls:

               for index, row in dataframe.iterrows():
                    sql = "INSERT INTO Students ( student_id, student_name, student_address, student_branch) VALUES (%s, %s, %s)"
                    val = (row['student_id'],row['student_name'], row['student_address'], row['student_branch'])
                    mycursor.execute(sql, val)
               mycursor.execute("SELECT * FROM Students")
               myresult = mycursor.fetchall()

               for x in myresult:
                    print(x)

            if "Professors" in existing_tbls:

               for index, row in dataframe.iterrows():
                    sql = "INSERT INTO Professors ( professor_id, professor_name, subject) VALUES (%s, %s, %s)"
                    val = (row['professor_id'],row['professor_name'], row['subject'])
                    mycursor.execute(sql, val)
               mycursor.execute("SELECT * FROM Students")
               myresult = mycursor.fetchall()

               for x in myresult:
                    print(x)



            if "Subjects" in existing_tbls:

               for index, row in dataframe.iterrows():
                    sql = "INSERT INTO Subjects ( subject_id, professor_id) VALUES (%s, %s, %s)"
                    val = (row['subject_id'],row['subject_professor_id'])
                    mycursor.execute(sql, val)
               mycursor.execute("SELECT * FROM Subjects")
               myresult = mycursor.fetchall()

               for x in myresult:
                    print(x)



            if "Exams" in existing_tbls:

               for index, row in dataframe.iterrows():
                    sql = "INSERT INTO Exams ( exam_id, exam_name, exam_marks) VALUES (%s, %s, %s)"
                    val = (row['exam_id'],row['exam_name'], row['exam_marks'])
                    mycursor.execute(sql, val)
               mycursor.execute("SELECT * FROM Exams")
               myresult = mycursor.fetchall()

               for x in myresult:
                    print(x)

            if "Score" in existing_tbls:

               for index, row in dataframe.iterrows():
                    sql = "INSERT INTO Score ( score_id, score_student_id, score_subject_id, marks, score_exam_id) VALUES (%s, %s, %s)"
                    val = (row['score_id'],row['score_student_id'], row['score_subject_id'], row['marks'], row['score_exam_id'])
                    mycursor.execute(sql, val)
               mycursor.execute("SELECT * FROM Exams")
               myresult = mycursor.fetchall()

               for x in myresult:
                    print(x)


    except Exception as e:
        print(e)

    finally:
            conn.commit()
            conn.close()

mysql_connect('localhost', 'root', 'admin', 'uni_db.csv')

