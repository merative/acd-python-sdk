# coding: utf-8

# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

class TestSuggestion(object):

    @staticmethod
    def test_spelling_suggestions(suggestion=None):
        if suggestion is not None:
            assert suggestion.text is not None
            assert suggestion.confidence > 0
            if suggestion.semtypes is not None:
                for semtype in suggestion.semtypes:
                    assert semtype is not None
