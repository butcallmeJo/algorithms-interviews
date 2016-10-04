# 3) By using this puma log (gunicorn for Ruby): https://s3.amazonaws.com/holbertonintranet/files/sandbox/puma_small.log
# Please provide those datas:
# - how many DELETE SQL commands
# - how many UPDATE SQL commands
# - how many requests successed (status code 200)
# - how many requests forbidden (status code 403)

import requests

def puma_log():
    log_resp = requests.get(
        "https://s3.amazonaws.com/holbertonintranet/files/sandbox/puma_small.log"
    )
    sql_cmds = {}
    for line in log_resp.iter_lines():
        # print line
        if "DELETE" in line:
            if "DELETE" in sql_cmds:
                sql_cmds["DELETE"] += 1
            else:
                sql_cmds["DELETE"] = 1
        if "UPDATE" in line:
            if "UPDATE" in sql_cmds:
                sql_cmds["UPDATE"] += 1
            else:
                sql_cmds["UPDATE"] = 1
        if "Completed 200 OK" in line:
            if "requests successed" in sql_cmds:
                sql_cmds["requests successed"] += 1
            else:
                sql_cmds["requests successed"] = 1
        if "Completed 403 Forbidden" in line:
            if "requests forbidden" in sql_cmds:
                sql_cmds["requests forbidden"] += 1
            else:
                sql_cmds["requests forbidden"] = 1
            
    print sql_cmds

puma_log()