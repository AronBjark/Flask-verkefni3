from flask import Flask, render_template
app = Flask(__name__)

names = [ [0,"Fyrirsögn 1","Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sed porttitor nulla. Nam faucibus risus at cursus imperdiet. Curabitur nec turpis massa. Donec sollicitudin molestie scelerisque. Suspendisse placerat pretium metus, eu laoreet neque pellentesque ut. Mauris bibendum, nibh eget imperdiet consequat, sem neque dapibus diam, ac euismod nibh libero in tortor. Quisque sed libero leo.","aron@tskoli.is"],
		  [1,"Fyrirsögn 2","Cras quam dui, vestibulum quis lacinia tristique, feugiat vitae nisl. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Interdum et malesuada fames ac ante ipsum primis in faucibus. Vestibulum gravida, dui nec vestibulum maximus, elit neque dapibus diam, eu tincidunt quam risus quis eros.","aron@tskoli.is"],
		  [2,"Fyrirsögn 3","Nullam a turpis eget lectus ultrices consectetur. Vestibulum sed lorem gravida, lobortis ipsum et, eleifend nisl. Interdum et malesuada fames ac ante ipsum primis in faucibus. Cras eu lacus dignissim, varius augue vel, blandit ipsum. Fusce mollis dui vitae ante condimentum, eget efficitur erat sodales.","aron@tskoli.is"],
		  [3,"Fyrirsögn 4","Suspendisse vehicula diam a nisl dapibus molestie. Donec blandit egestas nisl, a dictum lacus euismod eget. Nulla at molestie risus. Donec mi orci, sodales sit amet libero eget, consectetur vehicula sem. Mauris sit amet ullamcorper nisi. Suspendisse vel nulla non neque sollicitudin porta et vulputate diam.","aron@tskoli.is"]
		 ]

@app.route("/")
def index():
	return render_template("layout.html", frett=names)

@app.route('/frett/<int:nr>')
def sida1(nr):
    return render_template("frett.html", frettir=names[nr])

if __name__ == "__main__":
	app.run(debug=True)
