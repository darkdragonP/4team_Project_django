import cx_Oracle
import os
from django.apps import AppConfig


class UserConfig(AppConfig):
    name = 'user'

def OutputTypeHandler(cursor, name, defaultType, size, precision, scale):
    defaultType == cx_Oracle.CLOB
    return cursor.var(cx_Oracle.LONG_STRING, arraysize = cursor.arraysize)

# Oracle DB Setting
os.putenv('NLS_LANG', '.UTF8') # Language ENV
os.environ['PATH'] = 'C:\Users\Kosmo_33\Desktop\4team\homedicin' # Oracle Client ENV
# Connection : DB / Password / Url
connection = cx_Oracle.connect('HOMEDICINE', 'hd1234', 'localhost/orcl')
connection.outputtypehandler = OutputTypeHandler # Setting Output Handler
cursor = connection.cursor() # Connection Cursor