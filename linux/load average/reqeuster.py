#!/usr/bin/python

import urllib2
import time

def send_http_get_request(url):
    start_time = time.time()
    response = urllib2.urlopen(url)
    elapsed_time = time.time() - start_time

    content = response.read()
    print("Status code: {}".format(response.getcode()))
    print("Response content: {}".format(content))
    return elapsed_time

def measure_average_response_time(url, num_requests):
    total_time = 0
    for i in range(num_requests):
        elapsed_time = send_http_get_request(url)
        total_time += elapsed_time
        time.sleep(1)

    average_time = total_time / num_requests
    return average_time

if __name__ == "__main__":
    url = "http://localhost:8080"
    num_requests = 10

    average_response_time = measure_average_response_time(url, num_requests)
    print("\nAverage response time for {} requests: {:.4f} seconds".format(num_requests, average_response_time))
