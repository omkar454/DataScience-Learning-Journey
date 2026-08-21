from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def feedback():
    return render_template("feedback.html")

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    age = request.form['age']
    rating = request.form['rating']
    suggestion = request.form['suggestion']
    return f"""
        <!DOCTYPE html>
        <html>
        <head>
            <title>Feedback Submitted</title>
            <style>
                * {{
                    box-sizing: border-box;
                    margin: 0;
                    padding: 0;
                }}

                body {{
                    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                    background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    min-height: 100vh;
                    padding: 20px;
                }}

                .box {{
                    width: 100%;
                    max-width: 450px;
                    background: #ffffff;
                    padding: 40px 30px;
                    border-radius: 12px;
                    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
                    text-align: center;
                }}

                h2 {{
                    color: #4CAF50;
                    margin-bottom: 25px;
                    font-weight: 600;
                    font-size: 24px;
                }}

                /* Modern summary card for the submitted data */
                .details-card {{
                    background: #f9f9f9;
                    padding: 20px;
                    border-radius: 8px;
                    margin-bottom: 25px;
                    text-align: left;
                    border: 1px solid #eee;
                }}

                .detail-row {{
                    display: flex;
                    justify-content: space-between;
                    margin-bottom: 12px;
                    padding-bottom: 12px;
                    border-bottom: 1px solid #eaeaea;
                    font-size: 15px;
                }}

                .detail-row:last-child {{
                    border-bottom: none;
                    margin-bottom: 0;
                    padding-bottom: 0;
                }}

                .detail-label {{
                    font-weight: 600;
                    color: #555;
                }}

                .detail-value {{
                    color: #333;
                    text-align: right;
                    max-width: 60%;
                    word-wrap: break-word;
                }}

                .btn {{
                    display: block;
                    width: 100%;
                    padding: 14px;
                    background: #4CAF50;
                    color: white;
                    text-decoration: none;
                    border-radius: 8px;
                    font-size: 16px;
                    font-weight: bold;
                    transition: background 0.3s ease, transform 0.1s ease;
                }}

                .btn:hover {{
                    background: #45a049;
                }}

                .btn:active {{
                    transform: scale(0.98);
                }}
            </style>
        </head>

        <body>

            <div class="box">
                <h2>🎉 Thank You!</h2>
                
                <div class="details-card">
                    <div class="detail-row">
                        <span class="detail-label">Name</span>
                        <span class="detail-value">{name}</span>
                    </div>
                    <div class="detail-row">
                        <span class="detail-label">Email</span>
                        <span class="detail-value">{email}</span>
                    </div>
                    <div class="detail-row">
                        <span class="detail-label">Age</span>
                        <span class="detail-value">{age}</span>
                    </div>
                    <div class="detail-row">
                        <span class="detail-label">Rating</span>
                        <span class="detail-value">{rating}</span>
                    </div>
                    <div class="detail-row">
                        <span class="detail-label">Suggestion</span>
                        <span class="detail-value">{suggestion}</span>
                    </div>
                </div>

                <a href="/" class="btn">Submit Another Feedback</a>
            </div>

        </body>
        </html>
        """

if __name__ == '__main__':
    app.run(debug=True)


    