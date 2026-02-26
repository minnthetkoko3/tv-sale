from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    # Running on port 5000 with debug mode on for easy development
    app.run(debug=True, port=5000)

# // this is testing for only auto email submit staill error


# from flask import Flask, render_template, request, redirect, url_for
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/submit-feedback', methods=['POST'])
# def submit_feedback():
#     # 1. Capture the data from the form
#     name = request.form.get('name')
#     rating = request.form.get('rating')
#     comments = request.form.get('comments')

#     # 2. Email Configuration
#     sender_email = "shwevisiontvhouse@gmail.com"  
#     sender_password = "shwevisiontvhouseEWA"     
#     receiver_email = "shwevisiontvhouse@gmail.com" 

#     # 3. Create the email message
#     msg = MIMEMultipart()
#     msg['From'] = sender_email
#     msg['To'] = receiver_email
#     msg['Subject'] = f"New TV Store Feedback from {name}"

#     # Format the body of the email
#     body = f"Name: {name}\nRating: {rating} Stars\n\nComments:\n{comments}"
#     msg.attach(MIMEText(body, 'plain'))

#     # 4. Connect to Gmail's server and send the email
#     try:
#         # Connect to the SMTP server
#         server = smtplib.SMTP('smtp.gmail.com', 587)
#         server.starttls()  # Secure the connection
        
#         # Login using the sender email and password
#         server.login(sender_email, sender_password)
        
#         # Send the email
#         server.send_message(msg)
#         server.quit()
#         print("Feedback email sent successfully!")
#     except Exception as e:
#         print(f"Error sending email: {e}")
    
#     # 5. Redirect the user back to the home page after submitting
#     return redirect(url_for('home'))

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)