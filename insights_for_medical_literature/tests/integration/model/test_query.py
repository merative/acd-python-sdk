# coding: utf-8

# Copyright 2018 IBM All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import watson_health_cognitive_services.insights_for_medical_literature as wh

def test_query():
    concepts = []
    date_range = {}
    regexps = []
    regexp = {}
    regexps.append(regexp)
    title = wh.Title()
    cursor_id = 'test'
    operand = {}
    operands = []
    operands.append(operand)

    query = wh.Query(boolExpression='tast', concepts=concepts, boolTerm='test', boolRegexp='test', regexp=regexps,
                     date_range=date_range, title=title, cursorId=cursor_id, operands=operands, rankedSearch=False)
    query_diff = wh.Query(boolExpression='tast', concepts=concepts, boolTerm='test', boolRegexp='test', regexp=regexps,
                          date_range=date_range, title=title, cursorId=cursor_id, operands=operands, rankedSearch=True)
    query_same = wh.Query(boolExpression='tast', concepts=concepts, boolTerm='test', boolRegexp='test', regexp=regexps,
                          date_range=date_range, title=title, cursorId=cursor_id, operands=operands,
                          rankedSearch=False)

    query_obj = {}
    query_obj['boolExpression'] = 'test'
    query_obj['date_range'] = date_range
    query_obj['concepts'] = concepts
    query_obj['boolTerm'] = 'test'
    query_obj['boolRegexp'] = 'test'
    query_obj['regexp'] = regexps
    query_obj['title'] = {}
    query_obj['cursorId'] = 'test'
    query_obj['operands'] = operands
    query_obj['rankedSearch'] = False
    query_dict = query._from_dict(query_obj)
    assert query_dict is not None
    assert query.__str__() is not None
    assert query.__eq__(query_same)
    assert query.__ne__(query_diff)
