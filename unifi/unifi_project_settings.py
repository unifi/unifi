# UNIFI specific settings

MAX_GROUP_SIZE = 2
MIN_SCORE = 0.5 # (less == high likeness, more = low likeness)
MAX_NUMBER_OF_TAGS = 5

WHITESPACE_IN_TAG = True # [+] not integrated


MIN_GROUP_MEMBER_COUNT_TO_CALL_ORACLE = 2 # [+] not integrated


STUDENT_OPTIONS = {
    "tags_per_wish": 5,
}

MATCHER_OPTIONS = {
    "max_group_size": 3,
    "min_distance": 0.3,
}

GENERATOR_OPTIONS = {
    "wish_tag_separator": " ",
    "tag_separator": ",",
}