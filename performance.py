# performance.py

import requests
import threading

def make_request():
    requests.get('http://localhost:5000/wait')




def run_requests(make_request):
    t = threading.Thread(target=make_request)
    t.start()
    return t

if __name__ == "__main__":

    # [make_request() for i in range(4)]    
    threads = [run_requests(make_request) for i in range(10)]
    
    for thread in threads:
        thread.join()
