from flask import Flask, render_template

app = Flask(__name__)
projects=[
  {'id':1,
  'projects':'web scrapping',
  'skills':'urllib python,python ,Reguests,selenium'},
  {'id':2,
  'projects':'Ai model for flare mointoring',
  'skills':'python padas,matblotlib,microsoft azure,pychatgpt'}

  
]


@app.route('/')
def hello_world():
  return render_template('home.html',myskills= projects,
                       myname='Remas saud' )
  
  


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
