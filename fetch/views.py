from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime, timedelta
import requests
import json


def home(request):

        return render(
        request,
        'fetch/index.html',
        {
            'title': 'Home Page',
            'year': datetime.now().year,
        }
    )


def group(request):
    TOKEN = "DQVJ0LW9vc1BRYlJ1TU5heEtyVEVLbnE1ZAHdLQnZAfUFJjblhRQUdZANDhHYnZAwdU53RVI0UndFZAlJMV2ttczlRai1yZAGZAVQUNmTHQ4YXVjT3pGREtIWi1JdEZAibUlxWFBCc3FQSFBfd2dlS0RTVE81SHBSX2lobnc2UEFNcXJJZA2laRHpCaGRCZAlBkWXhvNW1LT1FMTHFHZAFFmdzR3T19WY2kyTGdoeFY3Sy1ZAOE1jb1hkT2x5cktwQjlGcGl2YlRxX0dQSWY0dmN2U1B2b0NoQQZDZD"
    DAYS = 1000

    GRAPH_URL_PREFIX = "https://graph.facebook.com/"
    GROUPS_SUFFIX = "/groups"
    MEMBERS_SUFFIX = "/members"

    DEFAULT_LIMIT = "500"
    VERBOSE = True
    SINCE = datetime.now() - timedelta(days=DAYS)

    headers = {'Authorization': 'Bearer ' + TOKEN}
    params = "?fields=feed.since(" + SINCE.strftime(
        "%S") + ").limit(500),name,privacy,members{name,id,email,administrator},updated_time&amp"

    # params += "&amp;limit=" + DEFAULT_LIMIT

    graph_url = GRAPH_URL_PREFIX + "community" + GROUPS_SUFFIX + params

    result = requests.get(graph_url, headers=headers)
    result_json = json.loads(result.text)
    groups = []
    members = []
    name = []

    def mem(grp):
        print("***group_members***")

        paramss = "?fields=feed.since(" + SINCE.strftime(
            "%S") + ").limit(500),name,email,id,administrator,updated_time&amp"
        # paramss += "&amp;limit=" + DEFAULT_LIMIT

        # print("1")
        grp_url = GRAPH_URL_PREFIX + grp + MEMBERS_SUFFIX + paramss
        # print("2")
        res = requests.get(grp_url, headers=headers)
        # print("3")
        res_json = json.loads(res.text)
        # print("4")
        if "data" in res_json:
            # print("5")
            for member_obj in res_json["data"]:
                # print("6")
                if "feed" in member_obj:
                    # print("7")
                    members.append(member_obj)
                    # print("8")
                    for i in range(len(members)):
                        # print("9")
                        adm = members[i]['administrator']
                        # print(adm)
                        if (adm is True):
                            print(members[i]['name'])
                            print(members[i]['email'])
                            #  print(members[i]['administrator'])
                            print(members[i]['id'])
                            print("******")
                        # print("11")
                    members.clear()
    print("groups")
    if "data" in result_json:
        for group_obj in result_json["data"]:
            if "feed" in group_obj:
                groups.append(group_obj)

        for i in range(len(groups)):
            print(groups[i]['name'])
            print(groups[i]['id'])
            grp = groups[i]['id']
            mem(grp)
            print(groups[i]['privacy'])
            print(" ")

    return render(
        request,
        'fetch/group.html',
        {
            'title': 'Group Page',
            'year': datetime.now().year,
        },

    )


def members(request):
    TOKEN = "DQVJ0LW9vc1BRYlJ1TU5heEtyVEVLbnE1ZAHdLQnZAfUFJjblhRQUdZANDhHYnZAwdU53RVI0UndFZAlJMV2ttczlRai1yZAGZAVQUNmTHQ4YXVjT3pGREtIWi1JdEZAibUlxWFBCc3FQSFBfd2dlS0RTVE81SHBSX2lobnc2UEFNcXJJZA2laRHpCaGRCZAlBkWXhvNW1LT1FMTHFHZAFFmdzR3T19WY2kyTGdoeFY3Sy1ZAOE1jb1hkT2x5cktwQjlGcGl2YlRxX0dQSWY0dmN2U1B2b0NoQQZDZD"
    DAYS = 1000

    GRAPH_URL_PREFIX = "https://graph.facebook.com/"
    GROUPS_SUFFIX = "/groups"
    MEMBERS_SUFFIX = "/members"

    DEFAULT_LIMIT = "500"
    VERBOSE = True
    SINCE = datetime.now() - timedelta(days=DAYS)

    headers = {'Authorization': 'Bearer ' + TOKEN}
    params = "?fields=feed.since(" + SINCE.strftime(
        "%S") + ").limit(500),name,privacy,members{name,id,email,administrator},updated_time&amp"

    # params += "&amp;limit=" + DEFAULT_LIMIT

    graph_url = GRAPH_URL_PREFIX + "community" + GROUPS_SUFFIX + params

    result = requests.get(graph_url, headers=headers)
    result_json = json.loads(result.text)
    groups = []
    members = []
    name = []

    def mem(grp):
        print("***group_members***")

        paramss = "?fields=feed.since(" + SINCE.strftime(
            "%S") + ").limit(500),name,email,id,administrator,updated_time&amp"
        # paramss += "&amp;limit=" + DEFAULT_LIMIT

        # print("1")
        grp_url = GRAPH_URL_PREFIX + grp + MEMBERS_SUFFIX + paramss
        # print("2")
        res = requests.get(grp_url, headers=headers)
        # print("3")
        res_json = json.loads(res.text)
        # print("4")
        if "data" in res_json:
            # print("5")
            for member_obj in res_json["data"]:
                # print("6")
                if "feed" in member_obj:
                    # print("7")
                    members.append(member_obj)
                    # print("8")
                    for i in range(len(members)):
                        print(members[i]['name'])
                        print(members[i]['email'])
                        print(members[i]['administrator'])
                        print(members[i]['id'])
                        print("******")
                        # print("11")
                    members.clear()
    print("groups")
    if "data" in result_json:
        for group_obj in result_json["data"]:
            if "feed" in group_obj:
                groups.append(group_obj)

        for i in range(len(groups)):
            print(groups[i]['name'])
            print(groups[i]['id'])
            grp = groups[i]['id']
            mem(grp)
            print(groups[i]['privacy'])
            print(" ")

    return render(
            request,
            'fetch/members.html',
            {
                'title': 'Members',
                'year': datetime.now().year,
            }
        )