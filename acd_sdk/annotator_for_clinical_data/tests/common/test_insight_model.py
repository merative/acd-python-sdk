# coding: utf-8

# ***************************************************************** 
#                                                                   
# (C) Copyright Merative US L.P. and others 2018, 2023               
#                                                                   
# SPDX-License-Identifier: Apache-2.0                               
#                                                                   
# ***************************************************************** 

class TestInsightModel(object):

    @staticmethod
    def test_insight_model_data(data=None):
        if data is not None:
            assert data is not None
            if data.diagnosis is not None:
                assert len(data.diagnosis._to_dict()) > 0
                if data.diagnosis.usage is not None:
                    assert len(data.diagnosis.usage._to_dict()) > 0
                if data.diagnosis.modifiers is not None:
                    assert len(data.diagnosis.modifiers._to_dict()) > 0
            if data.procedure is not None:
                assert len(data.procedure._to_dict()) > 0
                if data.procedure.usage is not None:
                    assert len(data.procedure.usage._to_dict()) > 0
                if data.procedure.task is not None:
                    assert len(data.procedure.task._to_dict()) > 0
                if data.procedure.type is not None:
                    assert len(data.procedure.type._to_dict()) > 0
                if data.procedure.modifiers is not None:
                    assert len(data.procedure.modifiers._to_dict()) > 0
            if data.medication is not None:
                assert len(data.medication._to_dict()) > 0
                if data.medication.usage is not None:
                    assert len(data.medication.usage._to_dict()) > 0
                if data.medication.started is not None:
                    assert len(data.medication.started._to_dict()) > 0
                if data.medication.stopped is not None:
                    assert len(data.medication.stopped._to_dict()) > 0
                if data.medication.dose_changed is not None:
                    assert len(data.medication.dose_changed._to_dict()) > 0
                if data.medication.adverse is not None:
                    assert len(data.medication.adverse._to_dict()) > 0
            if data.normality is not None:
                assert len(data.normality._to_dict()) > 0
                if data.normality.usage is not None:
                    assert len(data.normality.usage._to_dict()) > 0
                if data.normality.evidence is not None:
                    for entry in data.normality.evidence:
                        assert entry is not None
            if data.tobacco is not None:
                assert len(data.tobacco._to_dict()) > 0
                if data.tobacco.usage is not None:
                    assert len(data.tobacco.usage._to_dict()) > 0
                if data.tobacco.use_status is not None:
                    assert len(data.tobacco.use_status._to_dict()) > 0
            if data.alcohol is not None:
                assert len(data.alcohol._to_dict()) > 0
                if data.alcohol.usage is not None:
                    assert len(data.alcohol.usage._to_dict()) > 0
                if data.alcohol.use_status is not None:
                    assert len(data.alcohol.use_status._to_dict()) > 0
                if data.alcohol.use_qualifier is not None:
                    assert len(data.alcohol.use_qualifier._to_dict()) > 0
            if data.illicit_drug is not None:
                assert len(data.illicit_drug._to_dict()) > 0
                if data.illicit_drug.usage is not None:
                    assert len(data.illicit_drug.usage._to_dict()) > 0
                if data.illicit_drug.use_status is not None:
                    assert len(data.illicit_drug.use_status._to_dict()) > 0
                if data.illicit_drug.use_dimension is not None:
                    assert len(data.illicit_drug.use_dimension._to_dict()) > 0
            if data.substance is not None:
                assert len(data.substance._to_dict()) > 0
                if data.substance.treatment is not None:
                    assert len(data.substance.treatment._to_dict()) > 0
