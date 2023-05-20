
import sqlite3 as sl


def create_table():
    sqlite_connection = sl.connect('DB1.db')  # Имя базы данных
    cursor = sqlite_connection.cursor()
    print("Подключен к SQLite")
    cursor.execute("""CREATE TABLE IF NOT EXISTS Main( 
       NameCulture TEXT, 
       Areas_of_growth TEXT, 
       Subject_RF TEXT, 
       Types_of_soils TEXT,
       Day_length_summer__by_region INTEGER,
       Day_length_winter_by_region INTEGER, 
       Day_length_spring_by_region INTEGER, 
       Day_length_autumn_by_region INTEGER,
       Number_of_light_days INTEGER, 
       pharmacopoeia TEXT, 
       Red_Book TEXT, 
       Red_Book_Region TEXT, 
       Sowing_period TEXT,
       Harvest_period TEXT, 
       Content_of_BAS_chemical_composition TEXT,
       What_medical_preparations_contain_the_name TEXT,
       Annual_demand_of_medicinal_raw_materials INTEGER);
    """)
    sqlite_connection.commit()


def insert_varible_into_table(NameCulture, Areas_of_growth, Subject_RF, Types_of_soils,
                              Day_length_summer__by_region,
                              Day_length_winter_by_region, Day_length_spring_by_region, Day_length_autumn_by_region,
                              Number_of_light_days, pharmacopoeia, Red_Book, Red_Book_Region, Sowing_period,
                              Harvest_period, Content_of_BAS_chemical_composition,
                              What_medical_preparations_contain_the_name,
                              Annual_demand_of_medicinal_raw_materials):
    try:
        sqlite_connection = sl.connect('DB1.db')  # Имя базы данных
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_insert_with_param = """INSERT INTO Main
                                      (NameCulture, Areas_of_growth, Subject_RF, Types_of_soils, Day_length_summer_by_region,
                      Day_length_winter_by_region, Day_length_spring_by_region, Day_length_autumn_by_region,
                      Number_of_light_days, pharmacopoeia, Red_Book, Red_Book_Region, Sowing_period,
                      Harvest_period, Content_of_BAS_chemical_composition,
                      What_medical_preparations_contain_the_name,
                      Annual_demand_of_medicinal_raw_materials)
                                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);"""
        data_tuple = (NameCulture, Areas_of_growth, Subject_RF, Types_of_soils, Day_length_summer__by_region,
                      Day_length_winter_by_region, Day_length_spring_by_region, Day_length_autumn_by_region,
                      Number_of_light_days, pharmacopoeia, Red_Book, Red_Book_Region, Sowing_period,
                      Harvest_period, Content_of_BAS_chemical_composition,
                      What_medical_preparations_contain_the_name,
                      Annual_demand_of_medicinal_raw_materials)
        cursor.execute(sqlite_insert_with_param, data_tuple)
        sqlite_connection.commit()
        print("Запись успешно вставлена  таблицу", cursor.rowcount)
        cursor.close()
    except sl.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


