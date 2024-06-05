import http.client, urllib
import time


def make_request_with_retry(retries=3, delay=5):
    for attempt in range(retries):
        try:
            conn = http.client.HTTPSConnection("api.pushover.net:443")
            conn.request("POST", "/1/messages.json",
                         urllib.parse.urlencode({
                             "token": "ajgks2momeurhgxaq1in4x4k5i1dbm",
                             "user": "u47xaumfiy9zrbh3yw9ejf5hg5d7pq",
                             "message": "Wake up!!! ",
                             "sound": "Alien Alarm",
                             "priority": 1
                         }),
                         {"Content-type": "application/x-www-form-urlencoded"})

            response = conn.getresponse()
            data = response.read()
            # print(data)
            conn.close()
            break  # If successful, exit the loop

        except http.client.ResponseNotReady as e:
            # print(f"Attempt {attempt + 1} failed: {e}")
            time.sleep(delay)

        except Exception as e:
            # print(f"An error occurred: {e}")
            break
