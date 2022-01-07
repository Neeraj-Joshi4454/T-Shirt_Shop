from instamojo_wrapper import Instamojo
API_KEY = "test_2aadf38941223e11c79fd93cf2e"
AUTH_TOKEN = "test_d27c04f75ef95268cc77f96b92c"
api = Instamojo(api_key=API_KEY, auth_token=AUTH_TOKEN, endpoint='https://test.instamojo.com/api/1.1/');


response = api.payment_request_create(
    amount='11',
    purpose='Testing',
    send_email=True,
    email="neerajmjoshi1@gmail.com",
    redirect_url="http://localhost:8000/handle_redirect.py"
    )

print( response['payment_request']['longurl'] )