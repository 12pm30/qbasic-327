import pytest
import pexpect
import os
import macros

@pytest.fixture
def setup():
   macros.removeTempDirs()

def test_transfer1(setup):
    rc = 0

    combined = macros.getIoList(macros.testDataDir() + '/frontend/transfer/transfer1_input.txt',
                                macros.testDataDir() + '/frontend/transfer/transfer1_output.txt')

    child = macros.spawnFrontend()

    for i,o in combined:
        rc |= macros.run_test(child,i,o)

    child.close()

    assert(rc == 0)

def test_transfer1_txSummary_0():
    assert(macros.compare_files(macros.testTempDir() + "/txSummary_0.txt",
                                macros.testDataDir() + "/frontend/transfer/transfer1_transaction_0.txt"))

def test_transfer1_txSummary_1():
    assert(macros.compare_files(macros.testTempDir() + "/txSummary_1.txt",
                                macros.testDataDir() + "/frontend/transfer/transfer1_transaction_1.txt"))

def test_transfer2(setup):
    rc = 0

    combined = macros.getIoList(macros.testDataDir() + '/frontend/transfer/transfer2_input.txt',
                                macros.testDataDir() + '/frontend/transfer/transfer2_output.txt')

    child = macros.spawnFrontend()

    for i,o in combined:
        rc |= macros.run_test(child,i,o)

    child.close()

    assert(rc == 0)

def test_transfer2_txSummary_0():
    assert(macros.compare_files(macros.testTempDir() + "/txSummary_0.txt",
                                macros.testDataDir() + "/frontend/common/transactionsummary_blank.txt"))

def test_transfer2_txSummary_1():
    assert(macros.compare_files(macros.testTempDir() + "/txSummary_1.txt",
                                macros.testDataDir() + "/frontend/common/transactionsummary_blank.txt"))
