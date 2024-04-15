import pandas as pd


def check():
    f = open("Dtb_Prop.txt", "r")
    host = f.readline()
    host = host[:-1]
    user = f.readline()
    user = user[:-1]
    passwd = f.readline()
    passwd = passwd[:-1]
    database = f.readline()
    f.close()
    import mysql.connector as sqltor
    mycon = sqltor.connect(host=host, user=user, passwd=passwd, database=database)
    cursor = mycon.cursor()
    c_com = ("Andhra_Pradesh", "Arunachal_Pradesh", "Assam", "Bihar", "Chhattisgarh",
             "Goa", "Gujarat", "Haryana", "Himachal_Pradesh", "Jammu_Kashmir",
             "Jharkhand", "Karnataka", "Kerala", "Madhya_Pradesh", "Maharashtra",
             "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab",
             "Rajasthan", "Sikkim", "Tamil_Nadu", "Tripura", "Uttar_Pradesh",
             "Uttarakhand", "West_Bengal", "Total_States", "A_N_Islands",
             "Chandigarh", "D_N_Haveli", "Daman_Diu", "Delhi", "Lakshadweep",
             "Puducherry", "Total_UTs", "Total_Overall")
    for i in c_com:
        drop = "Drop Table if exists {}".format(i)
        cursor.execute(drop)
    data = pd.read_csv(r'Traffic_accidents_by_month_of_occurrence_state.csv')
    df = pd.DataFrame(data)
    r_value = 0
    c = 0
    for i in range(len(c_com)):
        t_create = "create table {} (Acc_Type varchar(25)," \
                "Year int, January int, February int, March int, April int," \
                "May int, June int, July int, August int, September int," \
                "October int, November int, December int, Total int)".format(c_com[i])
        cursor.execute(t_create)
    for row in df.itertuples():
        insert = "Insert into {} values ('{}',{},{},{},{},{},{},{},{},{},{},{},{},{},{})".format(
            c_com[c], row.TYPE, row.Year, row.JANUARY, row.FEBRUARY, row.MARCH, row.APRIL, row.MAY, row.JUNE,
            row.JULY, row.AUGUST, row.SEPTEMBER, row.OCTOBER, row.NOVEMBER, row.DECEMBER, row.TOTAL)
        cursor.execute(insert)
        r_value += 1
        if (r_value % 48) == 0:
            c += 1
    mycon.commit()
    mycon.close()
