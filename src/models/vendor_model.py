from database import DBManager
from typing import List

class VendorModel(object):

    def ensure_table_exists(self) -> str:
        """
        Makes sure the table VENDORS exists, if not creates it.
        """
        try:
            conn = DBManager.get_connection()        
            cursor = conn.cursor()
            create_query = """
            CREATE TABLE IF NOT EXISTS VENDORS (
                NIF         VARCHAR(10)     PRIMARY KEY,
                NAME        VARCHAR(200)    NOT NULL,
                ADDRESS     VARCHAR(300),
                PHONE       VARCHAR(20)
            );
            """
            cursor.execute(create_query)
            DBManager.close_connection()
            return "OK"
        except Exception as error:
            return "An error occured when creating vendors table: {error}"

    def insert_vendor(self, nif:str, name:str, address:str, phone:str) -> str:
        """Inserts a new register in the VENDORS table
        
        Keyword arguments:
        nif                 -- the primary key and vendor ID
        name                -- name of the vendor
        address             -- fiscal address of the vendor
        phone               -- phone for contacting the vendor.
        Return:             return 'OK' in case the query was correctly executed. Otherwise returns the error raised
        """
        try:
            conn = DBManager.get_connection()
            cursor = conn.cursor()
            insert_query = """
            INSERT INTO VENDORS
            (?, ?, ?, ?);
            """
            cursor.execute(insert_query, (nif, name, address, phone))
            DBManager.close_connection()
            return "OK"
        except Exception as error:
            return "An error occured when inserting vendor {nif} into vendors table: {error}"
        
    def update_vendor(self, new_nif:str, name:str, address:str, phone:str, old_nif:str) -> str:
        """Updates a certain register from the VENDORS table.
        As there are not so many fields, it will update them all for 
        easy development.
        As 'ON UPDATE CASCADE' has been abled, the primary key can be modified
        
        Keyword arguments:
        new_nif             -- the new ID of the vendor
        name                -- name of the vendor
        address             -- fiscal address of the vendor
        phone               -- phone for contacting the vendor.
        old_nif             -- the previous nif. If the nif has not been modified, it could happen that new_nif = old_nif
        Return:             return 'OK' in case the query was correctly executed. Otherwise returns the error raised
        """
        try:
            conn = DBManager.get_connection()
            cursor = conn.cursor()
            update_query = """
            UPDATE VENDORS 
            SET NIF = (?), NAME = (?), ADDRESS = (?), PHONE = (?)
            WHERE NIF = (?);
            """
            cursor.execute(update_query, (new_nif, name, address, phone, old_nif))
            DBManager.close_connection()
            return "OK"
        except Exception as error:
            return "An error occured when updating vendor {old_nif} from vendors table: {error}"
        
    def delete_vendor(self, nif:str) -> str:
        """It does not delete a vendor, but anonymizes the data,
        so we can keep the invoices that were related to that vendor.
        
        Keyword arguments:
        nif                 -- ID of the vendor to anonymize
        Return: return 'OK' in case the query was correctly executed. Otherwise returns the error raised
        """
        try:
            conn = DBManager.get_connection()
            cursor = conn.cursor()
            unkown_counter_query = """
            SELECT COUNT(*) FROM VENDORS WHERE NAME LIKE 'UNKNOWN%';
            """
            cursor.execute(unkown_counter_query)
            # Gets first item of tuple
            unknown_count = cursor.fetchone()[1]
            delete_query = f"""
            UPDATE VENDORS
            SET NIF = 'UNKNOWN{unknown_count + 1}', NAME = 'UNKNOWN{unknown_count + 1}'
            WHERE NIF = (?);
            """
            cursor.execute(delete_query, (nif))
            DBManager.close_connection()
            return "OK"
        except Exception as error:
            return "An error occured when anonymizing vendor {nif} from vendors table: {error}"

