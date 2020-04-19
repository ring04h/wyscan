#!/usr/bin/env python
#coding=utf-8

from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.acs_exception.exceptions import ClientException
from aliyunsdkcore.acs_exception.exceptions import ServerException
from aliyunsdkecs.request.v20140526.DescribeInstancesRequest import DescribeInstancesRequest

client = AcsClient('LTAI4GGDGoTHNNXzwS7tCyMg', '4MH99PQ75l57SyPakDXC14n8Uh8RE7', 'cn-hangzhou')

request = DescribeInstancesRequest()
request.set_accept_format('json')

response = client.do_action_with_exception(request)
# python2:  print(response) 
print(str(response, encoding='utf-8'))
