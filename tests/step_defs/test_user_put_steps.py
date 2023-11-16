import json

import pytest
from pytest_bdd import scenarios, given, parsers, then, when

from tests.step_defs.conftest import request

scenarios('../features/user_put.feature')

