import mysql.connector
from mysql.connector import Error

def convertToBinaryData(filename):
    # Convert digital data to binary format
    with open(filename, 'rb') as file:
        binaryData = file.read()
    return binaryData

def insertBLOB(id, name, photo,personality_traits ):
    print("Inserting BLOB into python_ information table")
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='python_db',
                                             user='root',
                                             password='Nopassword08')

        cursor = connection.cursor()
        sql_insert_blob_query = """ INSERT INTO python_information
                          (id, name, photo, personality_traits) VALUES (%s,%s,%s,%s)"""

        CelPicture = convertToBinaryData(Img)
        file = convertToBinaryData(personality_traits)

        # Convert data into tuple format
        insert_blob_tuple = (id, name, CelPicture, file)
        result = cursor.execute(sql_insert_blob_query, insert_blob_tuple)
        connection.commit()
        print("Image and file inserted successfully as a BLOB into python_information table", result)

    except mysql.connector.Error as error:
        print("Failed inserting BLOB data into MySQL table {}".format(error))

    finally:
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

insertBLOB(1, "Amitabh Bachchan", "C:\PYTHON CODE\INTERN_TASK\Img\Amitabh-bachchan.jpg",
           "C:\PYTHON CODE\INTERN_TASK\personality_traits\Amitabh_Bachchan.txt")
insertBLOB(2, "Priyanka Chopra", "C:\PYTHON CODE\INTERN_TASK\Img\Priyanka-chopra.jpg",
           "C:\PYTHON CODE\INTERN_TASK\personality_traits\Priyanka_Chopra.txt")
insertBLOB(3, "Ranbir Kapoor ", "C:\PYTHON CODE\INTERN_TASK\Img\Ranbir-kapoor.jpg",
           "C:\PYTHON CODE\INTERN_TASK\personality_traits\Ranbir_Kapoor .txt")
insertBLOB(4, "Shilpa Shetty", "C:\PYTHON CODE\INTERN_TASK\Img\Shilpa-shetty.jpg",
           "C:\PYTHON CODE\INTERN_TASK\personality_traits\Shilpa_Shetty.txt")
