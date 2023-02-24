# coding: utf-8

# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

class TestSpellCorrectedText(object):

    @staticmethod
    def test_spell_corrected_text(annotation_list=None):
        if annotation_list is not None:
            for annotation in annotation_list:
                assert annotation.corrected_text is not None
                if annotation.debug_text is not None:
                    assert len(annotation.debug_text) > 0
