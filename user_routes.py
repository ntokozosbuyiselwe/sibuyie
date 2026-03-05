
from app import app,render_template

@app.user_routers('/')
def about():
    return render_template('about.html')
    



