import mysql.connector


cnx = mysql.connector.connect(user='root' , password='784512@aA',
                              host = '127.0.0.1',database='people_info')
# print(1)


my_cursor = cnx.cursor()


