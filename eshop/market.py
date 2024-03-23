from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/products')
def products_page():
    products = [
    {
        'name': "Men's Shoes DN 23XX",
        'image': 'https://via.placeholder.com/200x200?text=Shoe',
        'price': 150.00,
        'discount_price': 133.00,
        'discount': '25% off',
        'category': "Men's Shoes",
        'description': 'New product for men with advanced features.',
    },
    {
        'name': "Women's Shoes DN 23XX",
        'image': 'https://via.placeholder.com/200x200?text=Shoe2',
        'price': 100.00,
        'discount_price': 50.00,
        'discount': '50% off',
        'category': "Women's Shoes",
        'description': 'New product for women with stylish design.',
    },
]
    

    return render_template('products.html', products=products)

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

subscription_plans = [
    {
        'name': 'Basic Plan',
        'price': 'Free',
        'duration': '1 month',
        'features': ['1 Account', 'Limited content access', 'Limited amount of items in wishlist', 'No discount on shipment fees',
                     'Limited eligibility for giveaways'],
    },
    {
        'name': 'Standard Plan',
        'price': 19.99,
        'duration': '3 months',
        'features': ['Multiple Accounts', 'Full content access', 'Unlimited items in wishlist', '50% discount on shipment fees',
                     'Eligibility for a majority of giveaways'],
    },
    {
        'name': 'Premium Plan',
        'price': 29.99,
        'duration': '6 months',
        'features': ['Unlimited Accounts', 'Full content access', 'Unlimited items in wishlist', 'No shipment fees',
                     'Eligibility for exclusive giveaways'],
    },
]

@app.route('/subscription_plans')
def subscriptionPlans_page():
    return render_template('Subscription Plans/subscription_plans.html', plans=subscription_plans)

@app.route('/cart')
def cart_page():
    return render_template('cart.html')

@app.route('/Login')
def login_page():
    return render_template('Login/login.html')

@app.route('/Sign Up')
def signUp_page():
    return render_template('Sign Up/signUp.html')



if __name__ == '__main__':
    app.run(debug=True)
