import cx_Oracle as ora

database = 'HOMEDICINE2/hd1234@localhost:1521/orcl'

def getDetail(MD_CODE):
    conn = ora.connect(database)
    # print(MD_CODE)
    cursor = conn.cursor()
    sql_get ="SELECT MD_CODE,MD_TITLE,MD_GRADE, \
             MD_DATE,MD_HITS,MD_RATING, MD_IMAGE,MD_SHAPE, \
             MD_COLOR, MD_TYPE,MD_LINE,\
             dbms_lob.substr(MD_EFFECT,DBMS_LOB.GETLENGTH(MD_EFFECT)), \
             dbms_lob.substr(MD_CAPA,DBMS_LOB.GETLENGTH(MD_CAPA)), \
             dbms_lob.substr(MD_CAUTION,DBMS_LOB.GETLENGTH(MD_CAUTION)), \
             MD_SAVE,MD_INGREDIENT,MD_COMPANIES,MD_CLASS, \
             MD_APPR,MD_IN FROM MEDICINE  "


    cursor.execute(sql_get)
    datas = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return datas

def getDetail1_1(MD_CODE):
    conn = ora.connect(database)
    # print(MD_CODE)
    cursor = conn.cursor()
    sql_get ="SELECT MD_CODE,MD_TITLE,MD_GRADE, \
             MD_DATE,MD_HITS,MD_RATING, MD_IMAGE,MD_SHAPE, \
             MD_COLOR, MD_TYPE,MD_LINE,\
             dbms_lob.substr(MD_EFFECT,DBMS_LOB.GETLENGTH(MD_EFFECT)), \
             dbms_lob.substr(MD_CAPA,DBMS_LOB.GETLENGTH(MD_CAPA)), \
             dbms_lob.substr(MD_CAUTION,DBMS_LOB.GETLENGTH(MD_CAUTION)), \
             MD_SAVE,MD_INGREDIENT,MD_COMPANIES,MD_CLASS, \
             MD_APPR,MD_IN FROM MEDICINE "


    cursor.execute(sql_get)
    datas = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return datas

def getDetail2(MD_CODE):
    conn = ora.connect(database)
    # print(MD_CODE)
    cursor = conn.cursor()
    sql_get = "SELECT MD_CODE,MD_TITLE,MD_APPR ,MD_RATING,MD_HITS FROM MEDICINE "
    cursor.execute(sql_get)
    datas = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return datas

def getDetail2_1(MD_CODE):
    conn = ora.connect(database)
    # print(MD_CODE)
    cursor = conn.cursor()
    sql_get ="SELECT MD_CODE,MD_TITLE,MD_APPR ,MD_RATING,MD_HITS FROM MEDICINE ORDER BY MD_CODE desc"
    cursor.execute(sql_get)
    datas = cursor.fetchall()
    conn.commit()
    cursor.close()
    conn.close()
    return datas

def search_ingr(MD_CODE):
    conn = ora.connect(database)
    cursor = conn.cursor()
    sql_get = "SELECT MD_TITLE,MD_INGREDIENT, dbms_lob.substr(MD_EFFECT,DBMS_LOB.GETLENGTH(MD_EFFECT)) from medicine where MD_INGREDIENT like '%아세트%' "
    cursor.execute(sql_get)
    datas = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return datas

def search_effect(MD_CODE):
    conn = ora.connect(database)
    cursor = conn.cursor()
    sql_get = "SELECT MD_TITLE,MD_INGREDIENT, dbms_lob.substr(MD_EFFECT,DBMS_LOB.GETLENGTH(MD_EFFECT)) from medicine where MD_EFFECT like '%감기%' "
    cursor.execute(sql_get)
    datas = cursor.fetchone()
    conn.commit()
    cursor.close()
    conn.close()
    return datas