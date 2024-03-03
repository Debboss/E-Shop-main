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
    contact_info = [
    {
        'department': 'Sales',
        'email': 'sales@example.com',
        'phone': '+1 (555) 123-4567',
    },
    {
        'department': 'Support',
        'email': 'support@example.com',
        'phone': '+1 (555) 987-6543',
    },
    {
        'department': 'General Inquiries',
        'email': 'info@example.com',
        'phone': '+1 (555) 789-0123',
    },
    ]

    return render_template('contact_us.html', contact_info=contact_info)

@app.route('/subscription_plans')
def subscriptionPlans_page():
    plans = [
    {
        'name': 'Basic Plan',
        'price': 9.99,
        'duration': '1 month',
        'features': ['Basic features', 'Limited content access'],
    },
    {
        'name': 'Standard Plan',
        'price': 19.99,
        'duration': '3 months',
        'features': ['Standard features', 'Full content access', 'HD streaming'],
    },
    {
        'name': 'Premium Plan',
        'price': 29.99,
        'duration': '6 months',
        'features': ['Premium features', 'Ultra HD streaming', 'Offline downloads'],
    },
    {
        'name': 'Family Plan',
        'price': 39.99,
        'duration': '1 year',
        'features': ['All Premium features', 'Simultaneous streaming on multiple devices'],
    },
    ]

    return render_template('subscription_plans.html',plans=plans )

@app.route('/cart')
def cart_page():
    return render_template('cart.html')

if __name__ == '__main__':
    app.run(debug=True)
