import mysql.connector
# DB_HOST=127.0.0.1
# DB_PORT=3306
# DB_DATABASE=marsol
# DB_USERNAME=root
# DB_PASSWORD=root
# DB_SOCKET=/Applications/MAMP/tmp/mysql/mysql.sock

conn = mysql.connector.connect(
    host ="127.0.0.1",
    user ="root",
    passwd="1",
    database="sasjobs",
    auth_plugin='mysql_native_password'
    # unix_socket="/Applications/MAMP/tmp/mysql/mysql.sock"
)

cursor = conn.cursor()


#employee
#cursor.execute("SELECT id,email,password,remember_token,active,first_name,last_name,mobile,birth_date FROM users where role =2")
#admin
#cursor.execute("SELECT id,email,password,remember_token,active,first_name,last_name,mobile,birth_date FROM users where role =1")
#users
#cursor.execute("SELECT id,email,password,remember_token,active,first_name,last_name,mobile,birth_date FROM users where role =4")

#products =====  sas
# cursor.execute("SELECT id, DISTINCT FROM cat")
#users
# cursor.execute("SELECT id, FirstName, FamilyName, MainJobType, SubJobType,PhoneNumber, File, SmallMsg, email, profile_pic, CertfiedYears FROM cvtables")
#company
cursor.execute("SELECT  Name, CompanyName, PhoneNumber, email, profile_pic FROM jobowner")


#images
#cursor.execute("SELECT id,img FROM product_images")

#setting
#cursor.execute("SELECT keyword,value FROM  site_settings")
#cursor.execute("SELECT site,value FROM  social_links")
#sliders
#cursor.execute("SELECT title1,title3,img FROM  slideshows")

data = cursor.fetchall()

print(data)

conn2 = mysql.connector.connect(
    host ="127.0.0.1",
    user ="root",
    passwd="1",
    database="new_sas",
    auth_plugin='mysql_native_password'
    # unix_socket="/Applications/MAMP/tmp/mysql/mysql.sock"

)



cursor2 = conn2.cursor()
#Add Country Command
#sql ="INSERT INTO zood_countries(country_id,country_code,country_name_ar,country_name_en) VALUES (%s,%s,%s,%s)"

#Add Cities Command
#sql ="INSERT INTO zood_cities(city_id,city_name_ar) VALUES (%s,%s)"

#Add  employess
#sql ="INSERT INTO users(admin,id,email,password,remember_token,status,first_name,last_name,mobile,birth_date) VALUES (3,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

#Add Products

# sql ="INSERT INTO news(title,content) VALUES (%s,%s)"

#Add Articles 
#sql ="INSERT INTO zood_pages(page_id,page_photo,page_name_ar,page_desc_ar) VALUES (%s,%s,%s,%s)"

#setting
#sql ="INSERT INTO  zood_settings(setting_name,setting_value,created_by) VALUES (%s,%s,1)"

#sliders 

#sql ="INSERT INTO  zood_sliders(slider_name_ar,slider_desc_ar,slider_photo,created_by) VALUES (%s,%s,%s,1)"

#sas

# for x in range(0, 2):
#     if x  == 0:
#         sql ="INSERT INTO category_translations(category_id,name,locale) VALUES (%s,%s,'ar')"
#         cursor2.executemany(sql,data)
#         conn2.commit()

#     else:
#         sql ="INSERT INTO category_translations(category_id,name,locale) VALUES (%s,%s,'en')"
#         cursor2.executemany(sql,data)
#         conn2.commit()
#users
#sql ="INSERT INTO users(id, first_name,last_name,categories_id,sub_categories_id,phone,cv,bio,email,image,experience_years,user_type) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,'user')"
sql ="INSERT INTO users( first_name,fullname,phone,email,image,user_type) VALUES (%s,%s,%s,%s,%s,'company')"
cursor2.executemany(sql,data)
conn2.commit()


print("done added")
