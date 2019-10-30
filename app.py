from flask import Flask,render_template,redirect,request,url_for,session,flash
import csv
import smtplib
import os
import postsDB as pd
import msgDB as md
import cmntDB as cd

app = Flask(__name__, static_url_path='')
app.secret_key = 'this is a secret key'

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    post = pd.getPosts()
    if 'username' in session:
        return render_template('index2.html', post=post)
    else:
        return render_template('index1.html', post=post)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/getin', methods=['POST'])
def getin():
    username = request.form.get("username")
    password = request.form.get("password")

    if(username=='Soumen Bajpayee' and password=='maathakur60@'):
        session['username'] = username
        return redirect(url_for('index'))
    else:
        flash('Invalid \"Admin\" Login credentials')
        return redirect(url_for('login'))

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/sendmsg', methods=["POST"])
def sendmsg():
    name = request.form.get("name")
    email = request.form.get("email")
    msg = request.form.get("msg")
    msg1 = "Sender => "+name+"\nSender Email => "+email+"\nMessage =>\n"+msg
    msg2 = "Thank You "+name+"\nfor connecting with us.\nWe appreciate your message or suggestion for us.\nWe will surely get back to you in future if needed regarding your suggestion."

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.login('soumenbajpayee.showcase@gmail.com', 'maathakur60@')
    server.sendmail('soumenbajpayee.showcase@gmail.com', email, msg2)
    server.sendmail('soumenbajpayee.showcase@gmail.com', 'bajpayeeshouvik@gmail.com', msg1)
    server.close()

    md.enterMsg(name,email,msg)

    flash('Your message is sent !')
    return redirect(url_for('contact'))

@app.route('/comment')
def comment():
    cmnt = cd.getCmnt()
    return render_template('comment.html', cmnt=cmnt)

@app.route("/sendComment", methods=["POST"])
def sendcmnt():
    name = request.form.get("name")
    cmnt = request.form.get("comment")
    cd.sendCmnt(name,cmnt)
    return redirect(url_for('comment'))

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/upload')
def upload():
    if 'username' in session:
        return render_template('upload.html')
    else:
        return redirect(url_for('login'))

@app.route('/post', methods=['POST'])
def post():
    if 'username' in session:
        target = APP_ROOT + '/static/images'
        cat = request.form.get("cat")
        #short = request.form.get("short")
        short = ''
        long = request.form.get("long")
        specs = request.form.get("specs")
        imgfile = request.files.get("imgfile")
        vdofile = request.files.get("vdofile")
        imgfilename = ''
        vdofilename = ''

        if(imgfile):
            imgfilename = imgfile.filename
            destination = "/".join([target,imgfilename])
            imgfile.save(destination)
        if(vdofile):
            vdofilename = vdofile.filename
            destination = "/".join([target,vdofilename])
            vdofile.save(destination)

        pd.createPost(cat,short,long,specs,imgfilename,vdofilename)

        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))



@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, debug=True)


