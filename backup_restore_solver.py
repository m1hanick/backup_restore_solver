import json, requests, re, gzip, base64, argparse

def Solver(token: str) -> dict:

    req_url=f"https://hackattic.com/challenges/backup_restore/problem?access_token={token}"

    req = requests.get(req_url)

    j = json.loads(req.text)
    o = base64.b64decode(j['dump'], validate=True)
    g = gzip.decompress(o)
    text = g.decode("utf-8")

    regex = r"^\d+.*\t(\d{3}-\d{2}-\d{4}).*\t(alive)$"
    matches = re.findall(regex, text, re.MULTILINE | re.IGNORECASE)

    x = []
    for val in matches: 
        x.append(val[0])

    out_body = {'alive_ssns': list(x)}

    answ_url = f"https://hackattic.com/challenges/backup_restore/solve?access_token={token}"

    headers = {'Content-Type': 'application/json'}

    answ_resp = requests.request("POST", answ_url, headers=headers, data=json.dumps(out_body))

    return {'response': answ_resp.text, 'body': out_body}


def main():
    args_parser = argparse.ArgumentParser(description='https://hackattic.com/challenges/backup_restore solver')
    args_parser.add_argument("--token", "-t",
                            metavar="token",
                            required=True,
							help="Enter the auth token")
    
    args = args_parser.parse_args()
    
    resp = Solver(args.token)
    print(f'List of alive SSNs:\n {resp["body"]}\n\n')
    print(f'Response from the `hackattic.com`:\n {resp["response"]}')
    

if __name__ == "__main__":
    main()