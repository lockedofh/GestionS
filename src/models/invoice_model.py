from database import DBManager
from datetime import date

class InvoiceModel(object):

    def ensure_table_exists(self) -> str:
        """
        Makes sure the table INVOICES exists, if not creates it.º
        """
        try:
            conn = DBManager.get_connection()        
            cursor = conn.cursor()
            create_query = """
            CREATE TABLE IF NOT EXISTS INVOICES (
                NIF             VARCHAR(10),
                ID_INVOICE      VARCHAR(50),
                EMITTED_DATE    DATE,
                EFFECTIVE_DATE  DATE,
                BASE            NUMBER(7, 2),
                VAT             NUMBER(7, 2)
                PRIMARY KEY     (NIF, ID_INVOICE),
                FOREIGN KEY     (NIF) REFERENCES VENDORS(NIF) ON UPDATE CASCADE
            );
            """
            cursor.execute(create_query)
            DBManager.close_connection()
            return "OK"
        except Exception as error:
            return "An error occured when creating invoices table: {error}"

    def insert_invoice(self, nif:str, id_invoice:str, emitted_date:date, effective_date:date, base:float, vat:float) -> str:
        """Inserts a new register in the INVOICES table
        
        Keyword arguments:
        nif                 -- vendor ID
        id_invoice          -- id of the invoice
        emitted_date        -- date when the invoice was created and emitted to customer
        effective_date      -- date of when the invoice needs to be effective (this is the relevant date for reporting)
        base                -- invoice amount without VAT
        vat                 -- only VAT amount
        Return:             return 'OK' in case the query was correctly executed. Otherwise returns the error raised
        """
        try:
            conn = DBManager.get_connection()
            cursor = conn.cursor()
            insert_query = """
            INSERT INTO INVOICES
            (?, ?, ?, ?, ?, ?)
            """
            cursor.execute(insert_query, (nif, id_invoice, emitted_date, effective_date, base, vat))
            DBManager.close_connection()
            return "OK"
        except Exception as error:
            return "An error occured when inserting invoice {id_invoice} into invoices table: {error}"
        
    def update_invoice(self, new_nif:str, new_id_invoice:str, emitted_date:date, effective_date:date, base:float, vat:float, old_nif:str, old_id_invoice:str) -> str:
        """Updates a certain register from the INVOICES table.
        As there are not so many fields, it will update them all for 
        easy development.
        As 'ON UPDATE CASCADE' has been abled, the primary key can be modified
        
        Keyword arguments:
        new_nif                 -- new ID of the vendor
        new_id_invoice          -- new id of the invoice
        emitted_date            -- date when the invoice was created and emitted to customer
        effective_date          -- date of when the invoice needs to be effective (this is the relevant date for reporting)
        base                    -- invoice amount without VAT
        vat                     -- only VAT amount
        old_nif                 -- original vendor ID
        old_id_invoice          -- original id of the invoice
        Return:                 return 'OK' in case the query was correctly executed. Otherwise returns the error raised
        """
        try:
            conn = DBManager.get_connection()
            cursor = conn.cursor()
            update_query = """
            UPDATE INVOICES 
            SET NIF = (?), ID_INVOICE = (?), EMITTED_DATE = (?), EFFECTIVE_DATE = (?), BASE = (?), VAT = (?)            
            WHERE NIF = (?) AND ID_INVOICE = (?)
            """
            cursor.execute(update_query, (new_nif, new_id_invoice, emitted_date, effective_date, base, vat, old_nif, old_id_invoice))
            DBManager.close_connection()
            return "OK"
        except Exception as error:
            return "An error occured when updating invoice {old_id_invoice} from invoices table: {error}"
        
    def delete_invoice(self, nif:str, id_invoice:str) -> str:
        """Deletes a certain invoice
        
        Keyword arguments:
        nif                     -- vendor ID
        id_invoice              -- invoice ID
        Return:                 return 'OK' in case the query was correctly executed. Otherwise returns the error raised
        """
        try:
            conn = DBManager.get_connection()
            cursor = conn.cursor()
            delete_query = f"""
            DELETE FROM INVOICES
            WHERE NIF = (?) AND ID_INVOICE = (?)
            """
            cursor.execute(delete_query, (nif))
            DBManager.close_connection()
            return "OK"
        except Exception as error:
            return "An error occured when deleting invoice {id_invoice} from invoices table: {error}"

        


            
        

        