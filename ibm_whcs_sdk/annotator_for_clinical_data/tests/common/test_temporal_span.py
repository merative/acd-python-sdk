# coding: utf-8

# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

class TestTemporalSpanAnnotation(object):

    @staticmethod
    def test_temporal_span(annotation_list=None):
        if annotation_list is not None:
            for annotation in annotation_list:
                assert annotation.begin is not None
                assert annotation.end is not None
                assert annotation.covered_text is not None
                assert annotation.temporal_type is not None
