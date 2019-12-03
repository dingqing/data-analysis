import requests
import json
import time

# 异常处理
# 避免请求频繁

oldAcount = {
    'csrftoken':'',
    'cookie':''
}
newAcount = {
    'csrftoken':'',
    'cookie':''
}
submitCnt=0

def getAcProblems():
    headers={
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0',
        'content-type': 'application/json',
        'referer':'https://leetcode-cn.com/problemset/all/',
        'cookie':oldAcount['cookie']}
    r=requests.get('https://leetcode-cn.com/api/problems/all/',headers=headers)
    data=r.json()
    problems=set()
    # 题目发生改变，导致旧的已经成功的提交会发生错误的题目
    exclude_ids=set((56,986,435,1028))
    for i,v in enumerate(data['stat_status_pairs']):
        if v['status']=='ac' and v['stat']['question_id'] not in exclude_ids:
            problems.add(str(v['stat']['question_id'])+':'+v['stat']['question__title_slug'])

    headers={
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0',
        'content-type': 'application/json',
        'referer':'https://leetcode-cn.com/problemset/all/',
        'cookie':newAcount['cookie']}
    r=requests.get('https://leetcode-cn.com/api/problems/all/',headers=headers)
    data=r.json()
    new_problems=set()
    for i,v in enumerate(data['stat_status_pairs']):
        if v['status']!='ac':
            new_problems.add(str(v['stat']['question_id'])+':'+v['stat']['question__title_slug'])
    problems=problems & new_problems
    # print(problems)

    with open('problems.txt', "w") as f:
        f.write('\n'.join(problems))

def submit():
    # 读取-去重-写入
    with open('problems.txt') as f:
        problems = set(f.read().splitlines())
    with open('problems.txt', 'w') as f:
        for x in problems:
            f.write("%s\n" % x)
    # print(len(problems),problems)

    for i in problems:
        s=i.split(':')
        # print(s)
        getAndSubmit(s[0],s[1])

def getAndSubmit(pid,pTitle):
    submissions=getsubmissions(pTitle)
    for i in submissions:
        if i['statusDisplay']=='Accepted':
            lang=i['lang']
            myCode=getMyCode(pTitle,pid,lang)
            submitNew(pTitle, pid, lang, myCode)
            break

# 1.获取提交记录
def getsubmissions(pTitle):
    payload={"operationName":"Submissions","variables":{"offset":0,"limit":20,"lastKey":None,"questionSlug":pTitle},"query":"query Submissions($offset: Int!, $limit: Int!, $lastKey: String, $questionSlug: String!) {\n  submissionList(offset: $offset, limit: $limit, lastKey: $lastKey, questionSlug: $questionSlug) {\n    lastKey\n    hasNext\n    submissions {\n      id\n      statusDisplay\n      lang\n      runtime\n      timestamp\n      url\n      isPending\n      memory\n      __typename\n    }\n    __typename\n  }\n}\n"}
    url="https://leetcode-cn.com/graphql"
    headers={
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0',
        'content-type': 'application/json',
        'referer':'https://leetcode-cn.com/problems/'+pTitle+'/submissions/',
        'x-csrftoken':oldAcount['csrftoken'],
        'cookie':oldAcount['cookie']}
    r=requests.post(url,headers=headers,data=json.dumps(payload))
    data=r.json()
    # print("submissions:",data)
    return data['data']['submissionList']['submissions']
# 2.获取最近的提交
def getMyCode(pTitle,pid,lang):
    url='https://leetcode-cn.com/submissions/latest/?qid='+pid+'&lang='+lang
    headers={
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0',
        'content-type': 'application/json',
        'referer':'https://leetcode-cn.com/problems/'+pTitle+'/submissions/',
        'x-csrftoken':oldAcount['csrftoken'],
        'cookie':oldAcount['cookie']}
    r=requests.get(url,headers=headers)
    data=r.json()
    return data['code']

# 3.（新帐号）提交代码
def submitNew(pTitle, pid, lang, myCode):
    url='https://leetcode-cn.com/problems/'+pTitle+'/submit/'
    payload={
        "lang": lang,
        "question_id": pid,
        "typed_code": myCode
    }
    headers={
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:67.0) Gecko/20100101 Firefox/67.0',
        'content-type': 'application/json',
        'referer':'https://leetcode-cn.com/problems/'+pTitle+'/submissions/',
        'x-csrftoken':newAcount['csrftoken'],
        'cookie':newAcount['cookie']}
    r=requests.post(url,headers=headers,json=payload)
    print('pid:',pid,' status_code:',r.status_code)
    if r.status_code==200:
        data=r.json()
        if data['submission_id']>0:
            global submitCnt
            submitCnt+=1
            print(data,' pid:',pid,' submit cnt:',submitCnt)
            time.sleep(2)
    else:
        with open('problems.txt', "a") as out_file:
            out_file.write(pid+":"+pTitle+"\n")
        print(r.raw)

# 从新旧帐号分别获取ac过的题目和没有提交过的题目，取交集，结果写入文件
getAcProblems()

# 从文件读取需要提交到新帐号的题目。
# 从旧帐号获取ac的代码，提交到新帐号。
# submit()