import server
import os

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
    print("[*] Environment Variables are set")
    print("API_KEY:", os.environ.get('API_KEY'))
    print("tvusername:", os.environ.get('tvusername'))
    print("tvpassword:", os.environ.get('tvpassword'))
    print("Another method:", os.environ['tvusername'])

if __name__ == '__main__':
    verify_env()
    server.start_server()