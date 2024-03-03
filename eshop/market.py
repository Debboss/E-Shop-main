from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/products')
def products_page():
    return render_template('products.html', item_name = 'Phone')

@app.route('/contact_us')
def contactUs_page():
    return render_template('contact_us.html')

@app.route('/subscription_plans')
def subscriptionPlans_page():
    return render_template('subscription_plans.html')

@app.route('/cart')
def cart_page():
    return render_template('cart.html')

if __name__ == '__main__':
    app.run(debug=True)
