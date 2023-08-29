# app.py

import logging
import time
from functools import wraps

from flask import Flask, jsonify

from utility import write_to_file

app = Flask(__name__)

logging.basicConfig(level=logging.DEBUG)
def timer(func):
    @wraps(func)
    def inner(*args, **kwargs):
        start_time = time.time()
        ret_val = func(*args, **kwargs)
        end_time = time.time()
        perf_record = {'start_time': start_time, 'end_time': end_time, 'func_name': func.__name__}
        write_to_file(perf_record)
        logging.debug('wrote perf record')
        return ret_val
    return inner


@app.route('/wait')
@timer
def wait():
    """Waits for 1 second and returns
    """
    logging.debug("Wait Called.")
    time.sleep(1)
    return jsonify({})

if __name__ == "__main__":
    app.run(debug=True)