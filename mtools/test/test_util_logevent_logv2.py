from mtools.util.logevent_v2 import LogEventv2

log_line = {"t":{"$date":"2021-08-23T03:11:09.288+00:00"},"s":"I","c":"REPL","id":51801,"ctx":"ReplWriterWorker-413","msg":"Applied op","attr":{"CRUD":{"op":"u","ns":"test.moar_collection","ui":{"$uuid":"80c04208-8fb4-46d7-a1ec-1b862eefcf52"},"o":"c5b4127017a56ee6a594e061ad6cf69e"},"planSummary":"COLLSCAN","cursorid":1912190691485054700,"keysExamined":0,"docsExamined":1000001,"hasSortStage":True,"usedDisk":True,"numYields":1002,"nreturned":101,"reslen":17738,"durationMillis":146},"truncated":{"CRUD":{"o":{"$set":{"some_field":{"15":{"startTime":{"type":"date","size":8}}}}}}},"size":{"CRUD":13120300}}
log_line_2 = {"t":{"$date":"2020-05-20T20:10:08.731+00:00"},"s":"I",  "c":"COMMAND",  "id":51803,   "ctx":"conn281","msg":"Slow query","attr":{"type":"command","ns":"stocks.trades","appName":"MongoDB Shell","command":{"aggregate":"trades","pipeline":[{"$project":{"ticker":1.0,"price":1.0,"priceGTE110":{"$gte":["$price",110.0]},"_id":0.0}},{"$sort":{"price":-1.0}}],"allowDiskUse":True,"cursor":{},"lsid":{"id":{"$uuid":"fa658f9e-9cd6-42d4-b1c8-c9160fabf2a2"}},"$clusterTime":{"clusterTime":{"$timestamp":{"t":1590005405,"i":1}},"signature":{"hash":{"$binary":{"base64":"AAAAAAAAAAAAAAAAAAAAAAAAAAA=","subType":"0"}},"keyId":0}},"$db":"test"},"planSummary":"COLLSCAN","cursorid":1912190691485054730,"keysExamined":0,"docsExamined":1000001,"hasSortStage":True,"usedDisk":True,"numYields":1002,"nreturned":101,"reslen":17738,"locks":{"ReplicationStateTransition":{"acquireCount":{"w":1119}},"Global":{"acquireCount":{"r":1119}},"Database":{"acquireCount":{"r":1119}},"Collection":{"acquireCount":{"r":1119}},"Mutex":{"acquireCount":{"r":117}}},"storage":{"data":{"bytesRead":232899899,"timeReadingMicros":186017},"timeWaitingMicros":{"cache":849}},"remote": "192.168.14.15:37666","protocol":"op_msg","durationMillis":22427}}

line_empty = {}


def test_logevent_datetime_parsing():
    """Check the timestamp formats are correctly parsed."""

    le = LogEventv2(log_line)
    assert(str(le._datetime) == '2021-08-23T03:11:09.288+00:00')

def test_logevent_component_parsing():
    """Check the component formats are correctly parsed."""

    le = LogEventv2(log_line)
    assert(le._component) == 'REPL'


def test_logevent_duration_parsing():
    """Check the duration formats are correctly parsed."""

    le = LogEventv2(log_line)
    assert(le._duration) == 146

def test_logevent_operation_parsing():
    """Check the operation formats are correctly parsed."""

    le = LogEventv2(log_line)
    assert(le._operation) == 'u'


def test_logevent_namespace_parsing():
    """Check the namespace formats are correctly parsed."""

    le = LogEventv2(log_line)
    assert(le._namespace) == 'test.moar_collection'


def test_logevent_command_parsing():
    """Check the command formats are correctly parsed."""

    le = LogEventv2(log_line)
    assert(le._command) == 'CRUD'

def test_logevent_planSummary_line():
    """ Check that planSummary formats are correctly parsed."""
    le = LogEventv2(log_line_2)
    assert(le._planSummary == 'COLLSCAN')


def test_logevent_cursorid_line():
    """ Check that cursorid formats are correctly parsed."""
    le = LogEventv2(log_line_2)
    assert(le._cursorid == 1912190691485054730)

def test_logevent_keysExamined_line():
    """ Check that keysExamined formats are correctly parsed."""
    le = LogEventv2(log_line_2)
    assert(le._keysExamined == 0)


def test_logevent_docsExamined_line():
    """ Check that docsExamined formats are correctly parsed."""
    le = LogEventv2(log_line_2)
    assert(le._docsExamined == 1000001)


def test_logevent_numYields_line():
    """ Check that numYields formats are correctly parsed."""
    le = LogEventv2(log_line_2)
    assert(le._numYields == 1002)

def test_logevent_nreturned_line():
    """ Check that nreturned formats are correctly parsed."""
    le = LogEventv2(log_line_2)
    assert(le._nreturned == 101)


def test_logevent_reslen_line():
    """ Check that reslen formats are correctly parsed."""
    le = LogEventv2(log_line_2)
    assert(le._reslen == 17738)