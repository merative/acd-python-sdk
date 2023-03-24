# coding: utf-8

# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

from acd_sdk.annotator_for_clinical_data.tests.common import test_suggestion as ts

class TestSpellingCorrection(object):

    @staticmethod
    def test_spelling_correction(annotation_list=None):
        if annotation_list is not None:
            for annotation in annotation_list:
                assert annotation.begin > 0
                assert annotation.end > annotation.begin
                assert annotation.covered_text is not None
                for suggestion in annotation.suggestions:
                    ts.TestSuggestion.test_spelling_suggestions(suggestion)
