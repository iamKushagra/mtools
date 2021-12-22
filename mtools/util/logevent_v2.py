import json
from datetime import datetime

class LogEventv2(object):
    def __init__(self, doc_or_str):
        self._profile_doc = doc_or_str
        self._parse_logv2()

    def _parse_logv2(self):

        """Parse logv2 format"""
        
        log = json.dumps(self._profile_doc)
        log_dict = json.loads(log)
        self._datetime_calculated = True    # no need to parse datetime
        self._datetime = log_dict['t']['$date']

        self._component_calculated = True
        self._component = log_dict['c']

        self._split_tokens_calculated = True
        self._split_tokens = None

        self._duration_calculated = True
        self._duration = log_dict['attr']['durationMillis']

        self._thread_calculated = True
        self._thread = log_dict['ctx']

        self._counters_calculated = True
        if(log_dict['attr']['planSummary']):
            self._planSummary = log_dict['attr']['planSummary']
        print(self._planSummary)
        self._cursorid = log_dict['attr']['cursorid']
        self._keysExamined = log_dict['attr']['keysExamined']
        self._docsExamined = log_dict['attr']['docsExamined']
        self._hasSortStage = log_dict['attr']['hasSortStage']
        self._usedDisk = log_dict['attr']['usedDisk']
        self._numYields = log_dict['attr']['numYields']
        self._nreturned = log_dict['attr']['nreturned']
        self._reslen = log_dict['attr']['reslen']
        self._readConcern = log_dict[u'level'] if 'level' in log_dict else None
        self._timeActiveMicros = log_dict[u'timeActiveMicros'] if 'timeActiveMicros' in log_dict else None
        self._timeInactiveMicros = log_dict[u'timeInactiveMicros'] if 'timeInactiveMicros' in log_dict else None
        self._operation_calculated = True
        try:
            self._operation = log_dict['attr']['CRUD']['op']
            self._namespace = log_dict['attr']['CRUD']['ns']
        except:
            self._operation = None
            self._namespace = None

        new_log = list(log_dict['attr'].keys())
        self._command = new_log[0]
        
        return self
