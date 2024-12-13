import mysql.connector

connection = mysql.connector.connect(
    user="root", 
    password="dennis09052003", 
    host="localhost",
    database="abc"
)
cursor = connection.cursor()
# ("INVENTORY", ("item_id","=", "1"),"itemstock=195")
def update_table(table_name,condition,new_value): # use table table_name instead of namex
    """
        params:
            table_name:str(table table_name)
            condition :tuple
            new_value: string(new value)
        use:to update the value of the row
        """
    condition="".join(condition)
    try :
        cursor.execute(f""" UPDATE {table_name}
                            SET {new_value}
                            WHERE {condition};
                            COMMIT;""") 
        print("Value Updated Successfully!!!!")
    except Exception as e:
        print(e)


cursor2=update_table("INVENTORY", ("item_id","=","2"),"itemstock=1500")