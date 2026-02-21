import logging
import os
import sys

# Ensure src/ is on the path so tests can import modules directly
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import pytest


@pytest.fixture(autouse=True)
def enable_log_propagation():
    """Re-enable log propagation on our module loggers so pytest caplog can capture records.

    logger.py sets propagate=False to avoid duplicate lines in Lambda (where the root
    logger also has a handler). In tests we want caplog to see the records, so we
    temporarily restore propagation.
    """
    names = ["csv_parser", "handler", "cloudzero_client"]
    for name in names:
        logging.getLogger(name).propagate = True
    yield
    for name in names:
        logging.getLogger(name).propagate = False
