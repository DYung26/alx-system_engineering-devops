#!/usr/bin/env python3

import requests

def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0',
        # 'Accept-Encoding': 'gzip, deflate, br, zstd',
        # 'Accept-Language': 'en-GB,en;q=0.9,en-US;q=0.8',
        'Cookie': 'csv=2; edgebucket=LHyhJcnLkGmflz77Z1; pc=io; g_state={"i_l":0}; reddit_session=96100442474529%2C2024-08-13T12%3A52%3A14%2C95aed0b100d8f8619b5e866f117b4441a4913943; loid=000000000y2bxm7jfl.2.1712813079639.Z0FBQUFBQm11MWNDM2lyajRDaC1Xa1hoLUdncDVLV19obDZ2QlJiN1ltdTd5M0hxYzNiRENIUUJBcUZGQzE4cGZuUTh1UGJPcTRZR2d2NkFHQm5KVWozV1lqRjF2TlB0MGJvT0IzcVdRTnhTdVlOVFVjZjFnNGtRN3RZUWVuNXhBd2NrTk1tMi1CWmg; session=32fc514471f4b2a6bce3eb426c23a0265ab3b094gAWVSQAAAAAAAABKfV27ZkdB2a7XX2tCtn2UjAdfY3NyZnRflIwoZDNiODIzMzFmMGM2YjM2MDU1YTU3ZjY3ZmE1MTkzM2YwOGU2MTM1ZJRzh5Qu; token_v2=eyJhbGciOiJSUzI1NiIsImtpZCI6IlNIQTI1NjpzS3dsMnlsV0VtMjVmcXhwTU40cWY4MXE2OWFFdWFyMnpLMUdhVGxjdWNZIiwidHlwIjoiSldUIn0.eyJzdWIiOiJ1c2VyIiwiZXhwIjoxNzIzNjQxNjI2LjY1NDk3MiwiaWF0IjoxNzIzNTU1MjI2LjY1NDk3MiwianRpIjoidE43aVpDVV9rbGNwTUNna29EcWpsZXNfblB1R3BRIiwiY2lkIjoiMFItV0FNaHVvby1NeVEiLCJsaWQiOiJ0Ml95MmJ4bTdqZmwiLCJhaWQiOiJ0Ml95MmJ4bTdqZmwiLCJsY2EiOjE3MTI4MTMwNzk2MzksInNjcCI6ImVKeGtrZEdPdERBSWhkLWwxejdCX3lwX05odHNjWWFzTFFhb2szbjdEVm9jazcwN2NMNGlIUDhuS0lxRkxFMnVCS0drS1dFRld0T1VOaUx2NTh5OU9aRUZTeUZUUjg0M3l3b2thVXBQVW1ONXB5bFJ3V1prTGxmYXNVS0RCNllwVlM2WjIwS1BTNXZRM0kxRnowNk1xbHhXSHRUWW8zSnBiR01LMnhQanpjWnFReXF1eTZsTVlGa29uOFdMZnZ5Ry10WS1mN2JmaEhZd3JLZ0tEX1RPdUZ4d1lfSERGSGJfbnByMGJGMndxTDNYZzlRLTEtTjI3Yk5tb2RtNV9WelB2emFTY1RtRzVpZll2N3QtQ1IxNDVIbVpVUWN3WWcwX3lyQWo2X0N2T29ES0JRV01KWWhQSTVBcmwyX19KZGl1VGY4YXR5ZC0tR2JFVFdfNHJSbW81eExFb1VfajZ6Y0FBUF9fWERfZTR3IiwicmNpZCI6IlhTRjBpaGNadmtVd1VLRGhzVmhiX3BsZEVOQ01kZEg1cjA4S0JPendpeDAiLCJmbG8iOjJ9.PUBbci6-ZgzK5SsfjXLg1LtGvC4KELlv7T-beRVVQwyTXWsN6XGl2u_U8MBoJ5eKsQ6yGciXpjhR1vaynQS4vwY2uO-G3M-MZVhdcUqT5uK6cpUe7EGe4CV0OzcH3_ljiNdAgmyRWpgYjKh4M2nvB0zNgvvG8yulF1MXO5zKmz1uKrKXzSC9Fh7F251qIdl0CbPGFIP6nhHnsFgvfRS3UvDD_x_oiVd42nZDM0myah4T3eFE5iMcyie_rWaqilzpjD6NjGJpyA6F7zVts3uSt4sRanIAt0rI9zkEUmC-LtQGPUasBZ6VJHSz2u6m4rui1HUGz4CBtgH76GHFtbZ-2Q; theme=2; csrf_token=1ce24a2fa641d12d609d97b1ea6aff0b; session_tracker=lraebqdknipmglmjmq.0.1723555567642.Z0FBQUFBQm11MTd2V193WDRYQkUxMVVFR3VKdHhtMGFsaElkS0NwN1R4UXVXbTRfNER2bDNxZHpvU1FTdmdWRVJ2cnBTdUdDU2g3MXFNN2dzTGRvZmktNHREZXhRcEdHa09PNVBZaFhCZmxYU1VKWDFuYklCNUVFQ2VyYlEtYk1JeVBJZklhNFRPXzE',
    }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        return (response.json()["data"]["subscribers"])
    else:
        return (0)

