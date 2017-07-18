import random
import string

import logging
logger = logging.getLogger(__name__)

def random_string(size=8, upper=True, lower=False, digits=True ):
    space = []
    if upper:
        space += string.ascii_uppercase
    if lower:
        space += string.ascii_lowercase
    if digits:
        space += string.digits
    if  len(space) == 0:
        raise ValueError("At least one of (upper, lower, digits) should be True!")
    return ''.join(random.choice(space) for i in range(size))