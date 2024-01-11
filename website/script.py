from scipy.optimize import minimize
import json
import mysql.connector
import sys

# establish the database connection
cnx = mysql.connector.connect(user='root', password='',
                            host='localhost',
                            database='login_register')

# create a cursor object
cursor = cnx.cursor()

# execute a query
query = ("SELECT total_cal FROM questionnaire WHERE user_id = (SELECT max(user_id) FROM questionnaire)")
cursor.execute(query)

# fetch the data

for row in cursor:
    total_cal = row[0]
    
# Define the variable names

monday = ['omlette_sen_1', 'chicken_griki_1', 'ceasar_1', 'veg_salad_1']
tuesday = ['auzu_2', 'lasis_2', 'dabig_jogurt_2', 'veg_salad_2']
wednesday = ['omlete_darz_3', 'vista_3', 'biezpien_3', 'darz_salad_3']
thuersday =['musli_4', 'liellopu_4', 'siera_pankuka_4', 'darz_salad_4']
friday = ['sok_uzputenis_5', 'kart_biez_5', 'pankuk_med_5', 'veg_salad_5']
saturday = ['aug_jog_6', 'lasanja_6', 'kebabs_6', 'veg_salad_6']
sunday = ['siera_kuka_7', 'brok_zupa_7', 'kart_pankuk_7', 'darz_salad_7']

# Create a dictionary to map variable names to indices

monday_dict = {name: i for i, name in enumerate(monday)}
tuesday_dict = {name: i for i, name in enumerate(tuesday)}
wednesday_dict = {name: i for i, name in enumerate(wednesday)}
thuersday_dict = {name: i for i, name in enumerate(thuersday)}
friday_dict = {name: i for i, name in enumerate(friday)}
saturday_dict = {name: i for i, name in enumerate(saturday)}
sunday_dict = {name: i for i, name in enumerate(sunday)}

# Define the objective function

def objective(x):
    return sum(x)

# Define the constraints

# Monday

def proteins_1(x):
    return 13*x[monday_dict['omlette_sen_1']] + 27*x[monday_dict['chicken_griki_1']] + 8*x[monday_dict['ceasar_1']] + 1*x[monday_dict['veg_salad_1']] - (0.2 * total_cal) / 4

def fats_1(x):
    return 11*x[monday_dict['omlette_sen_1']] + 5*x[monday_dict['chicken_griki_1']] + 6*x[monday_dict['ceasar_1']] + 2*x[monday_dict['veg_salad_1']] - (0.3 * total_cal) / 9

def carbo_1(x):
    return 2*x[monday_dict['omlette_sen_1']] + 25*x[monday_dict['chicken_griki_1']] + 5*x[monday_dict['ceasar_1']] + 4*x[monday_dict['veg_salad_1']] - (0.5 * total_cal) / 4

def calories_day_1_1(x):
    return 155*x[monday_dict['omlette_sen_1']] + 0*x[monday_dict['chicken_griki_1']] + 0*x[monday_dict['ceasar_1']] + 0*x[monday_dict['veg_salad_1']] - (0.2 * total_cal)

def calories_day_1_2(x):
    return 0*x[monday_dict['omlette_sen_1']] + 225*x[monday_dict['chicken_griki_1']] + 0*x[monday_dict['ceasar_1']] + 35*x[monday_dict['veg_salad_1']] - (0.45 * total_cal)

def calories_day_1_3(x):
    return 0*x[monday_dict['omlette_sen_1']] + 0*x[monday_dict['chicken_griki_1']] + 100*x[monday_dict['ceasar_1']] - (0.2 * total_cal)

def calories_day_1_total(x):
    return 155*x[monday_dict['omlette_sen_1']] + 225*x[monday_dict['chicken_griki_1']] + 100*x[monday_dict['ceasar_1']] + 35*x[monday_dict['veg_salad_1']] - total_cal

#-----------------------------------------------------------------

# Tuesday

def proteins_2(x):
    return 5*x[tuesday_dict['auzu_2']] + 25*x[tuesday_dict['lasis_2']] + 5*x[tuesday_dict['dabig_jogurt_2']] + 1*x[tuesday_dict['veg_salad_2']] - (0.2 * total_cal) / 4

def fats_2(x):
    return 3*x[tuesday_dict['auzu_2']] + 13*x[tuesday_dict['lasis_2']] + 4*x[tuesday_dict['dabig_jogurt_2']] + 2*x[tuesday_dict['veg_salad_2']] - (0.3 * total_cal) / 9

def carbo_2(x):
    return 15*x[tuesday_dict['auzu_2']] + 0*x[tuesday_dict['lasis_2']] + 7*x[tuesday_dict['dabig_jogurt_2']] + 4*x[tuesday_dict['veg_salad_2']] - (0.5 * total_cal) / 4

def calories_day_2_1(x):
    return 105*x[tuesday_dict['auzu_2']] + 0*x[tuesday_dict['lasis_2']] + 0*x[tuesday_dict['dabig_jogurt_2']] + 0*x[tuesday_dict['veg_salad_2']] - (0.2 * total_cal)

def calories_day_2_2(x):
    return 0*x[tuesday_dict['auzu_2']] + 206*x[tuesday_dict['lasis_2']] + 0*x[tuesday_dict['dabig_jogurt_2']] + 35*x[tuesday_dict['veg_salad_2']] - (0.45 * total_cal)

def calories_day_2_3(x):
    return 0*x[tuesday_dict['auzu_2']] + 0*x[tuesday_dict['lasis_2']] + 80*x[tuesday_dict['dabig_jogurt_2']] + 0*x[tuesday_dict['veg_salad_2']] - (0.2 * total_cal)

def calories_day_2_total(x):
    return 105*x[tuesday_dict['auzu_2']] + 206*x[tuesday_dict['lasis_2']] + 80*x[tuesday_dict['dabig_jogurt_2']] + 35*x[tuesday_dict['veg_salad_2']] - total_cal

#-----------------------------------------------------------------
# Wednesday

def proteins_3(x):
    return 7*x[wednesday_dict['omlete_darz_3']] + 31*x[wednesday_dict['vista_3']] + 18*x[wednesday_dict['biezpien_3']] + 2*x[wednesday_dict['darz_salad_3']] - (0.2 * total_cal) / 4

def fats_3(x):
    return 10*x[wednesday_dict['omlete_darz_3']] + 4*x[wednesday_dict['vista_3']] + 1*x[wednesday_dict['biezpien_3']] + 1*x[wednesday_dict['darz_salad_3']] - (0.3 * total_cal) / 9

def carbo_3(x):
    return 3*x[wednesday_dict['omlete_darz_3']] + 0*x[wednesday_dict['vista_3']] + 3*x[wednesday_dict['biezpien_3']] + 10*x[wednesday_dict['darz_salad_3']] - (0.5 * total_cal) / 4

def calories_day_3_1(x):
    return 134*x[wednesday_dict['omlete_darz_3']] + 0*x[wednesday_dict['vista_3']] + 0*x[wednesday_dict['biezpien_3']] + 0*x[wednesday_dict['darz_salad_3']] - (0.2 * total_cal)

def calories_day_3_2(x):
    return 0*x[wednesday_dict['omlete_darz_3']] + 165*x[wednesday_dict['vista_3']] + 0*x[wednesday_dict['biezpien_3']] + 53*x[wednesday_dict['darz_salad_3']] - (0.45 * total_cal)

def calories_day_3_3(x):
    return 0*x[wednesday_dict['omlete_darz_3']] + 0*x[wednesday_dict['vista_3']] + 90*x[wednesday_dict['biezpien_3']] + 0*x[wednesday_dict['darz_salad_3']] - (0.2 * total_cal)

def calories_day_3_total(x):
    return 134*x[wednesday_dict['omlete_darz_3']] + 165*x[wednesday_dict['vista_3']] + 90*x[wednesday_dict['biezpien_3']] + 53*x[wednesday_dict['darz_salad_3']] -  total_cal

#-----------------------------------------------------------------
# Thursday

def proteins_4(x):
    return 10*x[thuersday_dict['musli_4']] + 28*x[thuersday_dict['liellopu_4']] + 16*x[thuersday_dict['siera_pankuka_4']] + 2*x[thuersday_dict['darz_salad_4']] - (0.2 * total_cal) / 4

def fats_4(x):
    return 10*x[thuersday_dict['musli_4']] + 17*x[thuersday_dict['liellopu_4']] + 9*x[thuersday_dict['siera_pankuka_4']] + 1*x[thuersday_dict['darz_salad_4']] - (0.3 * total_cal) / 9

def carbo_4(x):
    return 55*x[thuersday_dict['musli_4']] + 0*x[thuersday_dict['liellopu_4']] + 26*x[thuersday_dict['siera_pankuka_4']] + 10*x[thuersday_dict['darz_salad_4']] - (0.5 * total_cal) / 4

def calories_day_4_1(x):
    return 340*x[thuersday_dict['musli_4']] + 0*x[thuersday_dict['liellopu_4']] + 0*x[thuersday_dict['siera_pankuka_4']] + 0*x[thuersday_dict['darz_salad_4']] - (0.2 * total_cal)

def calories_day_4_2(x):
    return 0*x[thuersday_dict['musli_4']] + 250*x[thuersday_dict['liellopu_4']] + 0*x[thuersday_dict['siera_pankuka_4']] + 53*x[thuersday_dict['darz_salad_4']] - (0.45 * total_cal)

def calories_day_4_3(x):
    return 0*x[thuersday_dict['musli_4']] + 0*x[thuersday_dict['liellopu_4']] + 250*x[thuersday_dict['siera_pankuka_4']] + 0*x[thuersday_dict['darz_salad_4']] - (0.2 * total_cal)

def calories_day_4_total(x):
    return 340*x[thuersday_dict['musli_4']] + 250*x[thuersday_dict['liellopu_4']] + 250*x[thuersday_dict['siera_pankuka_4']] + 53*x[thuersday_dict['darz_salad_4']] - total_cal

#-----------------------------------------------------------------
# Friday

def proteins_5(x):
    return 8*x[friday_dict['sok_uzputenis_5']] + 2*x[friday_dict['kart_biez_5']] + 6*x[friday_dict['pankuk_med_5']] + 1*x[friday_dict['veg_salad_5']] - (0.2 * total_cal) / 4

def fats_5(x):
    return 20*x[friday_dict['sok_uzputenis_5']] + 7*x[friday_dict['kart_biez_5']] + 7*x[friday_dict['pankuk_med_5']] + 2*x[friday_dict['veg_salad_5']] - (0.3 * total_cal) / 9

def carbo_5(x):
    return 30*x[friday_dict['sok_uzputenis_5']] + 17*x[friday_dict['kart_biez_5']] + 40*x[friday_dict['pankuk_med_5']] + 4*x[friday_dict['veg_salad_5']] - (0.5 * total_cal) / 4

def calories_day_5_1(x):
    return 300*x[friday_dict['sok_uzputenis_5']] + 0*x[friday_dict['kart_biez_5']] + 0*x[friday_dict['pankuk_med_5']] + 0*x[friday_dict['veg_salad_5']] - (0.2 * total_cal)

def calories_day_5_2(x):
    return 0*x[friday_dict['sok_uzputenis_5']] + 130*x[friday_dict['kart_biez_5']] + 0*x[friday_dict['pankuk_med_5']] + 35*x[friday_dict['veg_salad_5']] - (0.45 * total_cal)

def calories_day_5_3(x):
    return 0*x[friday_dict['sok_uzputenis_5']] + 0*x[friday_dict['kart_biez_5']] + 230*x[friday_dict['pankuk_med_5']] + 0*x[friday_dict['veg_salad_5']] - (0.2 * total_cal)

def calories_day_5_total(x):
    return 300*x[friday_dict['sok_uzputenis_5']] + 130*x[friday_dict['kart_biez_5']] + 230*x[friday_dict['pankuk_med_5']] + 35*x[friday_dict['veg_salad_5']] - total_cal


#-----------------------------------------------------------------
# Saturday

def proteins_6(x):
    return 5*x[saturday_dict['aug_jog_6']] + 20*x[saturday_dict['lasanja_6']] + 8*x[saturday_dict['kebabs_6']] + 1*x[saturday_dict['veg_salad_6']] - (0.2 * total_cal) / 4

def fats_6(x):
    return 2*x[saturday_dict['aug_jog_6']] + 15*x[saturday_dict['lasanja_6']] + 10*x[saturday_dict['kebabs_6']] + 2*x[saturday_dict['veg_salad_6']] - (0.3 * total_cal) / 9

def carbo_6(x):
    return 20*x[saturday_dict['aug_jog_6']] + 30*x[saturday_dict['lasanja_6']] + 15*x[saturday_dict['kebabs_6']] + 4*x[saturday_dict['veg_salad_6']] - (0.5 * total_cal) / 4

def calories_day_6_1(x):
    return 110*x[saturday_dict['aug_jog_6']] + 0*x[saturday_dict['lasanja_6']] + 0*x[saturday_dict['kebabs_6']] + 0*x[saturday_dict['veg_salad_6']] - (0.2 * total_cal)

def calories_day_6_2(x):
    return 0*x[saturday_dict['aug_jog_6']] + 320*x[saturday_dict['lasanja_6']] + 0*x[saturday_dict['kebabs_6']] + 35*x[saturday_dict['veg_salad_6']] - (0.45 * total_cal)

def calories_day_6_3(x):
    return 0*x[saturday_dict['aug_jog_6']] + 0*x[saturday_dict['lasanja_6']] + 190*x[saturday_dict['kebabs_6']] + 0*x[saturday_dict['veg_salad_6']] - (0.2 * total_cal)

def calories_day_6_total(x):
    return 110*x[saturday_dict['aug_jog_6']] + 320*x[saturday_dict['lasanja_6']] + 190*x[saturday_dict['kebabs_6']] + 35*x[saturday_dict['veg_salad_6']] - total_cal

#-----------------------------------------------------------------
# Sunday

def proteins_7(x):
    return 7*x[sunday_dict['siera_kuka_7']] + 4*x[sunday_dict['brok_zupa_7']] + 3*x[sunday_dict['kart_pankuk_7']] + 1*x[sunday_dict['darz_salad_7']] - (0.2 * total_cal) / 4

def fats_7(x):
    return 18*x[sunday_dict['siera_kuka_7']] + 3*x[sunday_dict['brok_zupa_7']] + 6*x[sunday_dict['kart_pankuk_7']] + 2*x[sunday_dict['darz_salad_7']] - (0.3 * total_cal) / 9

def carbo_7(x):
    return 20*x[sunday_dict['siera_kuka_7']] + 15*x[sunday_dict['brok_zupa_7']] + 17*x[sunday_dict['kart_pankuk_7']] + 4*x[sunday_dict['darz_salad_7']] - (0.5 * total_cal) / 4

def calories_day_7_1(x):
    return 250*x[sunday_dict['siera_kuka_7']] + 0*x[sunday_dict['brok_zupa_7']] + 0*x[sunday_dict['kart_pankuk_7']] + 0*x[sunday_dict['darz_salad_7']] - (0.2 * total_cal)

def calories_day_7_2(x):
    return 0*x[sunday_dict['siera_kuka_7']] + 100*x[sunday_dict['brok_zupa_7']] + 0*x[sunday_dict['darz_salad_7']] + 53*x[sunday_dict['darz_salad_7']] - (0.45 * total_cal)

def calories_day_7_3(x):
    return 0*x[sunday_dict['siera_kuka_7']] + 0*x[sunday_dict['brok_zupa_7']] + 133*x[sunday_dict['kart_pankuk_7']] + 0*x[sunday_dict['darz_salad_7']] - (0.2 * total_cal)

def calories_day_7_total(x):
    return 250*x[sunday_dict['siera_kuka_7']] + 100*x[sunday_dict['brok_zupa_7']] + 133*x[sunday_dict['kart_pankuk_7']] + 53*x[sunday_dict['darz_salad_7']] - total_cal

#-----------------------------------------------------------------

# Define the constraints for Monday

def omlette_sen_1(x):
    return x[monday_dict['omlette_sen_1']] - 1

def chicken_griki_1(x):
    return x[monday_dict['chicken_griki_1']] - 1

def ceasar_1(x):
    return x[monday_dict['ceasar_1']] - 1

def veg_salad_1(x):
    return x[monday_dict['veg_salad_1']] - 1

#-----------------------------------------------------------------

# Define the constraints for Tuesday

def auzu_2(x):
    return x[tuesday_dict['auzu_2']] - 1

def lasis_2(x):
    return x[tuesday_dict['lasis_2']] - 1

def dabig_jogurt_2(x):
    return x[tuesday_dict['dabig_jogurt_2']] - 1

def veg_salad_2(x):
    return x[tuesday_dict['veg_salad_2']] - 1

#-----------------------------------------------------------------

# Define the constraints for Wednesday

def omlete_darz_3(x):
    return x[wednesday_dict['omlete_darz_3']] - 1

def vista_3(x):
    return x[wednesday_dict['vista_3']] - 1

def biezpien_3(x):
    return x[wednesday_dict['biezpien_3']] - 1

def darz_salad_3(x):
    return x[wednesday_dict['darz_salad_3']] - 1

#-----------------------------------------------------------------

# Define the constraints for Thursday

def musli_4(x):
    return x[thuersday_dict['musli_4']] - 1

def liellopu_4(x):
    return x[thuersday_dict['liellopu_4']] - 1

def siera_pankuka_4(x):
    return x[thuersday_dict['siera_pankuka_4']] - 1

def darz_salad_4(x):
    return x[thuersday_dict['darz_salad_4']] - 1

#-----------------------------------------------------------------

# Define the constraints for Friday

def sok_uzputenis_5(x):
    return x[friday_dict['sok_uzputenis_5']] - 1

def kart_biez_5(x):
    return x[friday_dict['kart_biez_5']] - 1

def pankuk_med_5(x):
    return x[friday_dict['pankuk_med_5']] - 1

def veg_salad_5(x):
    return x[friday_dict['veg_salad_5']] - 1

#-----------------------------------------------------------------

# Define the constraints for Saturday

def aug_jog_6(x):
    return x[saturday_dict['aug_jog_6']] - 1

def lasanja_6(x):
    return x[saturday_dict['lasanja_6']] - 1

def kebabs_6(x):
    return x[saturday_dict['kebabs_6']] - 1

def veg_salad_6(x):
    return x[saturday_dict['veg_salad_6']] - 1

#-----------------------------------------------------------------

# Define the constraints for Sunday

def siera_kuka_7(x):
    return x[sunday_dict['siera_kuka_7']] - 1

def brok_zupa_7(x):
    return x[sunday_dict['brok_zupa_7']] - 1

def kart_pankuk_7(x):
    return x[sunday_dict['kart_pankuk_7']] - 1

def darz_salad_7(x):
    return x[sunday_dict['darz_salad_7']] - 1

#-----------------------------------------------------------------
# Price

x01 = [1, 1, 1, 1]
x02 = [1, 1, 1, 1]
x03 = [1, 1, 1, 1]
x04 = [1, 1, 1, 1]
x05 = [1, 1, 1, 1]
x06 = [1, 1, 1, 1]
x07 = [1, 1, 1, 1]

# ---------------------------------------------------------


# Optimize
solution1 = minimize(objective, x01, method='SLSQP', 
                    constraints=[{'type':'ineq', 'fun': proteins_1},
                                {'type':'ineq', 'fun': fats_1},
                                {'type':'ineq', 'fun': carbo_1},
                                {'type':'ineq', 'fun': calories_day_1_1},
                                {'type':'ineq', 'fun': calories_day_1_2},
                                {'type':'ineq', 'fun': calories_day_1_3},
                                {'type':'ineq', 'fun': calories_day_1_total},
                                {'type':'ineq', 'fun': omlette_sen_1},
                                {'type':'ineq', 'fun': chicken_griki_1},
                                {'type':'ineq', 'fun': ceasar_1},
                                {'type':'ineq', 'fun': veg_salad_1}
                                ])

x1 = solution1.x

solution2 = minimize(objective, x02, method='SLSQP',                                
                    constraints=[{'type':'ineq', 'fun': proteins_2},
                                {'type':'ineq', 'fun': fats_2},
                                {'type':'ineq', 'fun': carbo_2},
                                {'type':'ineq', 'fun': calories_day_2_1},
                                {'type':'ineq', 'fun': calories_day_2_2},
                                {'type':'ineq', 'fun': calories_day_2_3},
                                {'type':'ineq', 'fun': calories_day_2_total},
                                {'type':'ineq', 'fun': auzu_2},
                                {'type':'ineq', 'fun': lasis_2},
                                {'type':'ineq', 'fun': dabig_jogurt_2},
                                {'type':'ineq', 'fun': veg_salad_2}
                                ])

x2 = solution2.x

solution3 = minimize(objective, x03, method='SLSQP',
                    constraints = [{'type':'ineq', 'fun': proteins_3},
                                {'type':'ineq', 'fun': fats_3},
                                {'type':'ineq', 'fun': carbo_3},
                                {'type':'ineq', 'fun': calories_day_3_1},
                                {'type':'ineq', 'fun': calories_day_3_2},
                                {'type':'ineq', 'fun': calories_day_3_3},
                                {'type':'ineq', 'fun': calories_day_3_total},
                                {'type':'ineq', 'fun': omlete_darz_3},
                                {'type':'ineq', 'fun': vista_3},
                                {'type':'ineq', 'fun': biezpien_3},
                                {'type':'ineq', 'fun': darz_salad_3}
                                ])

x3 = solution3.x
            
solution4 = minimize(objective, x04, method='SLSQP',
                    constraints = [{'type':'ineq', 'fun': proteins_4},
                                {'type':'ineq', 'fun': fats_4},
                                {'type':'ineq', 'fun': carbo_4},
                                {'type':'ineq', 'fun': calories_day_4_1},
                                {'type':'ineq', 'fun': calories_day_4_2},
                                {'type':'ineq', 'fun': calories_day_4_3},
                                {'type':'ineq', 'fun': calories_day_4_total},
                                {'type':'ineq', 'fun': musli_4},
                                {'type':'ineq', 'fun': liellopu_4},
                                {'type':'ineq', 'fun': siera_pankuka_4},
                                {'type':'ineq', 'fun': darz_salad_4}
                                ])

x4 = solution4.x
                                
solution5 = minimize(objective, x05, method='SLSQP',                           
                    constraints=[{'type':'ineq', 'fun': proteins_5},
                                {'type':'ineq', 'fun': fats_5},
                                {'type':'ineq', 'fun': carbo_5},
                                {'type':'ineq', 'fun': calories_day_5_1},
                                {'type':'ineq', 'fun': calories_day_5_2},
                                {'type':'ineq', 'fun': calories_day_5_3},
                                {'type':'ineq', 'fun': calories_day_5_total},
                                {'type':'ineq', 'fun': sok_uzputenis_5},
                                {'type':'ineq', 'fun': kart_biez_5},
                                {'type':'ineq', 'fun': pankuk_med_5},
                                {'type':'ineq', 'fun': veg_salad_5}
                            ])

x5 = solution5.x      
                
solution6 = minimize(objective, x06, method='SLSQP',
                    constraints =[{'type':'ineq', 'fun': proteins_6},
                                {'type':'ineq', 'fun': fats_6},
                                {'type':'ineq', 'fun': carbo_6},
                                {'type':'ineq', 'fun': calories_day_6_1},
                                {'type':'ineq', 'fun': calories_day_6_2},
                                {'type':'ineq', 'fun': calories_day_6_3},
                                {'type':'ineq', 'fun': aug_jog_6},
                                {'type':'ineq', 'fun': lasanja_6},
                                {'type':'ineq', 'fun': kebabs_6},
                                {'type':'ineq', 'fun': veg_salad_6}
                                ])

x6 = solution6.x
                        
solution7 = minimize(objective, x07, method='SLSQP',                                 
                    constraints=[{'type':'ineq', 'fun': calories_day_6_total},
                                {'type':'ineq', 'fun': proteins_7},
                                {'type':'ineq', 'fun': fats_7},
                                {'type':'ineq', 'fun': carbo_7},
                                {'type':'ineq', 'fun': calories_day_7_1},
                                {'type':'ineq', 'fun': calories_day_7_2},
                                {'type':'ineq', 'fun': calories_day_7_3},
                                {'type':'ineq', 'fun': calories_day_7_total},
                                {'type':'ineq', 'fun': siera_kuka_7},
                                {'type':'ineq', 'fun': brok_zupa_7},
                                {'type':'ineq', 'fun': kart_pankuk_7},
                                {'type':'ineq', 'fun': darz_salad_7},
                                {'type':'ineq', 'fun': siera_kuka_7},
                                {'type':'ineq', 'fun': brok_zupa_7},
                                {'type':'ineq', 'fun': kart_pankuk_7},
                                {'type':'ineq', 'fun': darz_salad_7}
                                ])

x7 = solution6.x

# ----------------------------------------------------------

result_omlette_sen = None
result_chicken_griki = None
result_veg_salad_1 = None
result_ceasar = None

result_auzu = None
result_lasis = None
result_dabig_jogurt = None
result_veg_salad_2 = None

result_omlete_darz = None
result_vista = None
result_biezpien = None
result_darz_salad_3 = None

result_musli = None
result_liellopu = None
result_siera_pankuka = None
result_darz_salad_4 = None

result_sok_uzputenis = None
result_kart_biez = None
result_pankuk_med = None
result_veg_salad_5 = None

result_aug_jog = None
result_lasanja = None
result_kebabs = None
result_veg_salad_6 = None

result_siera_kuka = None
result_brok_zupa = None
result_kart_pankuk = None
result_darz_salad_7 = None

# Check if the solution was successful
if solution1.success:
    result_omlette_sen_1 = round(x1[monday_dict['omlette_sen_1']] * 100)
    result_chicken_griki_1 = round(x1[monday_dict['chicken_griki_1']] * 100)
    result_ceasar_1 = round(x1[monday_dict['ceasar_1']] * 100)
    result_veg_salad_1 = round(x1[monday_dict['veg_salad_1']] * 100)
else:
    print("ERROR")

# ------------------------------------------------

if solution2.success:
    result_auzu_2 = round(x2[tuesday_dict['auzu_2']] * 100)
    result_lasis_2 = round(x2[tuesday_dict['lasis_2']] * 100)
    result_dabig_jogurt_2 = round(x2[tuesday_dict['dabig_jogurt_2']] * 100)
    result_veg_salad_2 = round(x2[tuesday_dict['veg_salad_2']] * 100)
else:
    print("ERROR")

# ------------------------------------------------

if solution3.success:
    result_omlete_darz_3 = round(x3[wednesday_dict['omlete_darz_3']] * 100)
    result_vista_3 = round(x3[wednesday_dict['vista_3']] * 100)
    result_biezpien_3 = round(x3[wednesday_dict['biezpien_3']] * 100)
    result_darz_salad_3 = round(x3[wednesday_dict['darz_salad_3']] * 100)
else:
    print("ERROR")

# ------------------------------------------------

if solution4.success:
    result_musli_4 = round(x4[thuersday_dict['musli_4']] * 100)
    result_liellopu_4 = round(x4[thuersday_dict['liellopu_4']] * 100)
    result_siera_pankuka_4 = round(x4[thuersday_dict['siera_pankuka_4']] * 100)
    result_darz_salad_4 = round(x4[thuersday_dict['darz_salad_4']] * 100)
else:
    print("ERROR")

# ------------------------------------------------

if solution5.success:
    result_sok_uzputenis_5 = round(x5[friday_dict['sok_uzputenis_5']] * 100)
    result_kart_biez_5 = round(x5[friday_dict['kart_biez_5']] * 100)
    result_pankuk_med_5 = round(x5[friday_dict['pankuk_med_5']] * 100)
    result_veg_salad_5 = round(x5[friday_dict['veg_salad_5']] * 100)
else:
    print("ERROR")

# ------------------------------------------------

if solution6.success:
    result_aug_jog_6 = round(x6[saturday_dict['aug_jog_6']] * 100)
    result_lasanja_6 = round(x6[saturday_dict['lasanja_6']] * 100)
    result_kebabs_6 = round(x6[saturday_dict['kebabs_6']] * 100)
    result_veg_salad_6 = round(x6[saturday_dict['veg_salad_6']] * 100)
else:
    print("ERROR")

# ------------------------------------------------

if solution7.success:
    result_siera_kuka_7 = round(x7[sunday_dict['siera_kuka_7']] * 100)
    result_brok_zupa_7 = round(x7[sunday_dict['brok_zupa_7']] * 100)
    result_kart_pankuk_7 = round(x7[sunday_dict['kart_pankuk_7']] * 100)
    result_darz_salad_7 = round(x7[sunday_dict['darz_salad_7']] * 100)
else:
    print("ERROR")

# ------------------------------------------------

monday_meal = {
    'Brokastis sastav no omletem ar senem': f"{result_omlette_sen_1}g cena par edienu {round((result_omlette_sen_1/100),2)} $",
    'Pusdienas sastav no grikiem ar sautetu vistas galu' : f"{result_chicken_griki_1}g cena par edienu {round((result_chicken_griki_1/100),2)} $",
    'Vakarinas sastav no cezara salati': f"{result_ceasar_1}g cena par edienu {round((result_ceasar_1/100),2)} $",
    'Obligatais papildinajums darzenu salati': f"{result_veg_salad_1}g cena par edienu {round((result_veg_salad_1/100),2)} $"
}

tuesday_meal = {
    'Brokastis sastav no auzu parslas uz piena': f"{result_auzu_2}g cena par edienu {round((result_auzu_2/100),2)} $",
    'Pusdienas sastav no griletas lasim': f"{result_lasis_2}g cena par edienu {round((result_lasis_2/100),2)} $",
    'Vakarinas sastav no Dabigais jogurts': f"{result_dabig_jogurt_2}g cena par edienu {round((result_dabig_jogurt_2/100),2)} $",
    'Obligatais papildinajums darzenu salati': f"{result_veg_salad_2}g cena par edienu {round((result_veg_salad_2/100),2)} $"
}
wednesday_meal = {
    'Brokastis sastav no omletem ar darzeniem': f"{result_omlete_darz_3}g cena par edienu {round((result_omlete_darz_3/100),2)} $",
    'Pusdienas sastav no tvaiceta vistas fileja': f"{result_vista_3}g cena par edienu {round((result_vista_3/100),2)} $",
    'Vakarinas sastav no biezpiena ar zemu tauku saturu': f"{result_biezpien_3}g cena par edienu {round((result_biezpien_3/100),2)} $",
    'Obligatais papildinajums auglu salati': f"{result_darz_salad_3}g cena par edienu {round((result_darz_salad_3/100),2)} $"
}

thursday_meal = {
    'Brokastis sastav no musliem ar pienu': f"{result_musli_4}g cena par edienu {round((result_musli_4/100),2)} $",
    'Pusdienas sastav no liellopu galas sautejumu': f"{result_liellopu_4}g cena par edienu {round((result_liellopu_4/100),2)} $",
    'Vakarinas sastav no siera pankukas': f"{result_siera_pankuka_4}g cena par edienu {round((result_siera_pankuka_4/100),2)} $",
    'Obligatais papildinajums auglu salati': f"{result_darz_salad_4}g cena par edienu {round((result_darz_salad_4/100),2)} $"
}

friday_meal = {
    'Brokastis sastav no sokolades uzputenim': f"{result_sok_uzputenis_5}g cena par edienu {round((result_sok_uzputenis_5/100),2)} $",
    'Pusdienas sastav no kartupelu biezena': f"{result_kart_biez_5}g cena par edienu {round((result_kart_biez_5/100),2)} $",
    'Vakarinas sastav no pankukas ar medu': f"{result_pankuk_med_5}g cena par edienu {round((result_pankuk_med_5/100),2)} $",
    'Obligatais papildinajums darzenu salati': f"{result_veg_salad_5}g cena par edienu {round((result_veg_salad_5/100),2)} $"
}

saturday_meal = {
    'Brokastis sastav no auglu jogurtam': f"{result_aug_jog_6}g cena par edienu {round((result_aug_jog_6/100),2)} $",
    'Pusdienas sastav no lasanja': f"{result_lasanja_6}g cena par edienu {round((result_lasanja_6/100),2)} $",
    'Vakarinas sastav no kebaba': f"{result_kebabs_6}g cena par edienu {round((result_kebabs_6/100),2)} $",
    'Obligatais papildinajums darzenu salati': f"{result_veg_salad_6}g cena par edienu {round((result_veg_salad_6/100),2)} $"
}

sunday_meal = {
    'Brokastis sastav no siera kukas': f"{result_siera_kuka_7}g cena par edienu {round((result_siera_kuka_7/100),2)} $",
    'Pusdienas sastav no brokolu biezena zupas': f"{result_brok_zupa_7}g cena par edienu {round((result_brok_zupa_7/100),2)} $",
    'Vakarinas sastav no kartupelu pankukas': f"{result_kart_pankuk_7}g cena par edienu {round((result_kart_pankuk_7/100),2)} $",
    'Obligatais papildinajums auglu salati': f"{result_darz_salad_7}g cena par edienu {round((result_darz_salad_7/100),2)} $"
}

# Convert JSON to string

monday_meal_str = json.dumps(monday_meal)
tuesday_meal_str = json.dumps(tuesday_meal)
wednesday_meal_str = json.dumps(wednesday_meal)
thursday_meal_str = json.dumps(thursday_meal)
friday_meal_str = json.dumps(friday_meal)
saturday_meal_str = json.dumps(saturday_meal)
sunday_meal_str = json.dumps(sunday_meal)

try:
    with cnx.cursor() as cursor:
        cursor.execute("SELECT MAX(user_id) FROM questionnaire")
        max_user_id = cursor.fetchone()[0]

        if max_user_id is not None:
            sql1 = "UPDATE questionnaire SET monday = %s WHERE user_id = %s"
            sql2 = "UPDATE questionnaire SET tuesday = %s WHERE user_id = %s"
            sql3 = "UPDATE questionnaire SET wednesday = %s WHERE user_id = %s"
            sql4 = "UPDATE questionnaire SET thursday = %s WHERE user_id = %s"
            sql5 = "UPDATE questionnaire SET friday = %s WHERE user_id = %s"
            sql6 = "UPDATE questionnaire SET saturday = %s WHERE user_id = %s"
            sql7 = "UPDATE questionnaire SET sunday = %s WHERE user_id = %s"

        new_value1 = monday_meal_str
        new_value2 = tuesday_meal_str
        new_value3 = wednesday_meal_str
        new_value4 = thursday_meal_str
        new_value5 = friday_meal_str
        new_value6 = saturday_meal_str
        new_value7 = sunday_meal_str

        cursor.execute(sql1, (new_value1, max_user_id))
        cursor.execute(sql2, (new_value2, max_user_id))
        cursor.execute(sql3, (new_value3, max_user_id))
        cursor.execute(sql4, (new_value4, max_user_id))
        cursor.execute(sql5, (new_value5, max_user_id))
        cursor.execute(sql6, (new_value6, max_user_id))
        cursor.execute(sql7, (new_value7, max_user_id))

    cnx.commit()

finally:
    cnx.close()
print("XYJ")