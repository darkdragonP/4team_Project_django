# This is an auto-generated Django model module.

from django.db import models
import cx_Oracle as ora

database = 'homedicine/hd1234@127.0.0.1/orcl'

def md_Board():
    conn = ora.connect(database)
    cursor = conn.cursor()
    sql_all = 'select * from medicine'
    cursor.execute(sql_all)
    ad_data =cursor.fetchall()
    conn.close()
    return ad_data

def select_md_board(sd_list):
    conn = ora.connect(database)
    cursor = conn.cursor()
    idx = sd_list
    sql_sel = 'SElECT * FROM medicine WHERE USER_CODE = '+ idx
    cursor.execute(sql_sel)
    datas = cursor.fetchall()
    conn.close()
    return datas

def detile_md_board(dt_list):
    conn = ora.connect(database)
    cursor = conn.cursor()
    idx = dt_list
    sql_sel = 'SElECT user_code, md_code, md_title, md_grade,' \
              'md_date, md_hits,md_rating, md_image, md_shape,' \
              'md_color, md_type, md_line, md_effect,' \
              'dbms_lob.substr(MD_CAPA,DBMS_LOB.GETLENGTH(MD_CAPA)),' \
              'dbms_lob.substr(md_caution, DBMS_LOB.GETLENGTH(md_caution)),' \
              'md_save, md_ingredient, md_companies, md_class,' \
              'md_appr, md_in FROM medicine WHERE md_code = '+ idx
    cursor.execute(sql_sel)
    datas = cursor.fetchall()
    conn.close()
    return datas

def insert_md_board(sd_list):
    print(sd_list)
    conn = ora.connect(database)
    cursor = conn.cursor()
    sql_in = 'insert into medicine (user_code, md_code,' \
             'md_title, md_grade, md_date, md_hits, md_line,' \
             'md_effect, MD_CAPA, md_caution, md_save,) ' \
             'values(admin_board_seq.nextVal, :1, :2, :3, sysdate)'
    cursor.execute(sql_in)
    cursor.close()
    conn.commit()
    conn.close()
    return conn

def update_md_board(sd_list):
    conn = ora.connect(database)
    cursor = conn.cursor()
    idx = sd_list
    sql_sel = 'SElECT * FROM medicine WHERE USER_CODE = '+ idx
    cursor.execute(sql_sel)
    datas = cursor.fetchall()
    conn.close()
    return datas

def delete_md_board(sd_list):
    conn = ora.connect(database)
    cursor = conn.cursor()
    num = sd_list
    sql_sel = 'delete into medicine WHERE admin_board_code = '+ num
    cursor.execute(sql_sel)
    datas = cursor.fetchall()
    conn.close()
    return datas