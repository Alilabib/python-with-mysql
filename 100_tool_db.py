import mysql.connector
# DB_HOST=127.0.0.1
# DB_PORT=3306
# DB_DATABASE=marsol
# DB_USERNAME=root
# DB_PASSWORD=root
# DB_SOCKET=/Applications/MAMP/tmp/mysql/mysql.sock

conn = mysql.connector.connect(
    host ="78.46.56.170",
    user ="lbaaitd_sas_user",
    passwd="yFMoxm)@WhGZ",
    database="lbaaitd_sas",
    unix_socket="/Applications/MAMP/tmp/mysql/mysql.sock"
)

cursor = conn.cursor()


#employee
#cursor.execute("SELECT id,email,password,remember_token,active,first_name,last_name,mobile,birth_date FROM users where role =2")
#admin
#cursor.execute("SELECT id,email,password,remember_token,active,first_name,last_name,mobile,birth_date FROM users where role =1")
#users
#cursor.execute("SELECT id,email,password,remember_token,active,first_name,last_name,mobile,birth_date FROM users where role =4")

#products 
cursor.execute("SELECT id,FileNo,Count,JSON_OBJECT('ar',StoryAr,'en',StoryEn) as story, JSON_OBJECT('ar',NeedsAr,'en',NeedsEn) as need,Amount,Paid,Hide FROM family")

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
    host ="207.180.241.106",
    user ="demo",
    passwd="Dhi5wW89N7cdTNPB",
    database="demo",
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

#trahom
sql ="INSERT INTO families(id,code,num,story,needs,money,paid,is_active) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"


cursor2.executemany(sql,data)

conn2.commit()

print("done added")