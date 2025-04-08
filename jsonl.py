import json
class_str="""
{
    "一年甲班":[
    {   "number":1,
        "name":"jim",
        "chinese":65,
        "english":62,
        "math":40
    },
    {   "number":2,
        "name":"bill",
        "chinese":85,
        "english":90,
        "math":87
    },
    {   "number":3,
        "name":"marie",
        "chinese":92,
        "english":90,
        "math":95
    }
    ]
}

"""

datas=json.loads(class_str)
print(type(datas))
for data in datas ["一年甲班"]:
    print(data,data['name'])