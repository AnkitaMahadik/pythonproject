from flask import Flask,render_template
import pymysql 
   
    
app = Flask(__name__)   
   
connection = pymysql.connect( 
		host='localhost', 
		user='root', 
		password = "root", 
		db='project', 
		) 
	
cursor = connection.cursor()    
cursor.execute("SELECT * from movie_details")    
s = "<table style='border:1px solid red'cellspacing:2px><tr> <th>Name</th><th>Image</th><th>Summary</th></tr>"    
for row in cursor:    
    s = s +"<tr>"    
    for x in row:
        s = s + "<td>" + str(x) + "</td>"
    s = s +"</tr>"
    
connection.close()

   
@app.route('/')       
def details():
    return "<html><h1>Movie Details</h1><body>" + s + "</body></html>"    

if __name__ == "__main__":
    app.run()
