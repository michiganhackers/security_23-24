import requests
import time

# URL of the target server
url = 'https://madeharder-okntin33tq-ul.a.run.app/'

# Special characters to test
special_characters = ['$', '<', '>', '@', '!', '#', '%', '^', '&', '*', '(', ')', '{', '}']

# Function to send POST request with different combinations of special characters
def test_special_characters():
    for character in special_characters:
        print(f"testing with {character}")
        data = {
            'name': 'test',
            'code': f'print("{character}")'
        }
        response = requests.post(url, data=data)
        if 'wctf{' in response.text:
            print("Found the flag!")
            print(response.text)
            break
        else:
            print(f"Tested with {character}, didn't find the flag")
        time.sleep(5)

def main():
    print("Testing special characters")
    test_special_characters()

if __name__ == "__main__":
    main()