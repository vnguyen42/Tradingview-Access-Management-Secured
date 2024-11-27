import server
import os
from dotenv import load_dotenv

load_dotenv()

# Verify if env API_KEY, tvusername and tvpassword are set
def verify_env():
    if not os.environ.get('API_KEY'):
        print("[X] API_KEY is not set")
        exit(1)

    if not os.environ.get('tvusername'):
        print("[X] TV_USERNAME is not set")
        exit(1)

    if not os.environ.get('tvpassword'):
        print("[X] TV_PASSWORD is not set")
        exit(1)

if __name__ == '__main__':
    verify_env()
    server.start_server()