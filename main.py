from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')  # Serve the HTML form

@app.route('/submit', methods=['POST'])
def submit():
    # Get email value from the form
    email = request.form.get('email')
    
    # Get selected button values (if any)
    selected_option_1 = request.form.get('selectedOption1')
    selected_option_2 = request.form.get('selectedOption2')

    # Display the results
    return f"Email: {email}<br>Selected Options: {selected_option_1}, {selected_option_2}"

if __name__ == '__main__':
    app.run(debug=True)
