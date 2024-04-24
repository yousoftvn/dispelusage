import json
from dispel.data.collections import MeasureSet
from dispel.processing import process
from dispel.providers.ads.io import (read_ads,parse_ads_raw_json)
from dispel.providers.generic.tasks.gait.steps import (
    GaitSteps
)
def gait_calculation(data,selectedKeys):
    
    reading = parse_ads_raw_json(data)
    task = GaitSteps()
    process(reading,task)
    measure_set = reading.get_merged_measure_set()
    assert isinstance(measure_set, MeasureSet)
    result = dict()
  
    for key,value in measure_set.items():
        if(key.id in selectedKeys):
            result[key.id]=value.raw_value
    return result
