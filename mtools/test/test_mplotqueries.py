import sys
from datetime import datetime, timedelta
from random import randrange

from dateutil import parser

import pytest

import os

import mtools
from mtools.mplotqueries.mplotqueries import MPlotQueriesTool
from mtools.util.logevent import LogEvent
from mtools.util.logfile import LogFile

class TestMPlotQueries(object):

    @pytest.fixture(autouse=True)
    def setup_class(self):
        """Startup method to create mplotqueries tool."""
        #self.tool = MPlotQueriesTool()
        #self._test_init()

    def test_dns(self, filename='mongod_4.0.10_slowdns.log'):
        pytest.skip('Skipping interactive test')
        self.logfile_path = os.path.join(os.path.dirname(mtools.__file__),'test/logfiles/', filename)
        self.tool.run('%s --dns' % self.logfile_path)
        output = sys.stdout.getvalue()
        lines = output.splitlines()
        assert any(map(lambda line: 'SCATTER plot' in line, lines))

    def test_checkpoints(self, filename='mongod_4.0.10_slowcheckpoints.log'):
        pytest.skip('Skipping interactive test')
        self.logfile_path = os.path.join(os.path.dirname(mtools.__file__), 'test/logfiles/', filename)
        self.tool.run('%s --checkpoints' % self.logfile_path)
        output = sys.stdout.getvalue()
        lines = output.splitlines()
        assert any(map(lambda line: 'SCATTER plot' in line, lines))

    def test_oplog(self, filename='mongod_4.0.10_slowoplogs.log'):
        pytest.skip('Skipping interactive test')
        self.logfile_path = os.path.join(os.path.dirname(mtools.__file__), 'test/logfiles/', filename)
        self.tool.run('%s --oplog --group operation' % self.logfile_path)
        output = sys.stdout.getvalue()
        lines = output.splitlines()
        assert any('SCATTER plot' in line for line in lines)

    def test_storagestats(self, filename='mongod_4.0.10_storagestats.log'):
        pytest.skip('Skipping interactive test')
        self.logfile_path = os.path.join(os.path.dirname(mtools.__file__),'test/logfiles/', filename)
        self.tool.run('%s --storagestats --yaxis bytesRead' % self.logfile_path)
        output = sys.stdout.getvalue()
        lines = output.splitlines()
        assert any(map(lambda line: 'SCATTER plot' in line, lines))