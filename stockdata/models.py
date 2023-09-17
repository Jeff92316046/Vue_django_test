# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from collections import namedtuple
import sqlite3,copy
from django.db import connection

class Data(models.Model):
    
    stock = models.TextField(blank=True, null=True)
    date = models.TextField(blank=True, null=True)
    number = models.TextField(blank=True, null=True)
    people = models.TextField(blank=True, null=True)
    share = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'data'


def search_sql_by_stock(stock,number_min,number_max):
    print(stock+" "+number_min+" "+number_max)
    def clean_str(a):
        return int(str(a).replace(",",""))
    

    '''
    Note that if you want to include literal percent signs in the query,
    you have to double them in the case you are passing parameters:
    '''
    con = sqlite3.connect('db.sqlite3')
    cursor = con.cursor()
    cursor.execute("SELECT DISTINCT * FROM data WHERE stock = '" + str(stock) + "' ORDER BY date ASC" )
    
    result = [[],[],[]]
    data = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    data_2 = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
    j=0
    for i in cursor.fetchall():
        
        data_2[j%15].append(clean_str(i[3])) 
        data[j%15].append(clean_str(i[4])) 
        j += 1
    cursor.execute("SELECT DISTINCT * FROM data WHERE stock = '" + str(stock) + "'and number = " +str(number_min) +" ORDER BY date ASC" )
    
    for i in cursor.fetchall():
        result[0].append(i[1])
    data_2[15] = copy.deepcopy(data_2[int(number_min)-1])
    for i in range(int(number_min),int(number_max)):
        
        for j in range(len(data_2[i])):
            data_2[15][j] += data_2[i][j]
    data[15] = copy.deepcopy(data[0])
    
    for i in range(1,len(data)-1):
        for j in range(len(data[i])):
            data[15][j] += data[i][j]
    
    for i in range(len(data[0])):
        for j in range(len(data)-1):
            data[j][i] = data[j][i] / data[15][i]
            
        """ result[0].append(i[1])
        result[1].append(clean_str(i[3]))
        result[2].append(clean_str(i[4])) """
    result[2] = copy.deepcopy(data[int(number_min)-1])
 
    for i in range(int(number_min),int(number_max)):
        for j in range(len(data[i])) :
            result[2][j] += data[i][j]
    result[1] = copy.deepcopy(data_2[15])
    print(str(len(result[0]))+" "+str(len(result[1]))+" "+str(len(data[1])))
    return result
#

