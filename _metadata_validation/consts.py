FIELD_ID = 'id'
FIELD_TITLE = 'title'
FIELD_OVERVIEW = 'overview'
FIELD_PRODUCT = 'product'
FIELD_OS = 'os'
FIELD_FILTERS = 'filters'
FIELD_LOGO = 'logo'
FIELD_LOGS_DASHBOARD = 'logs_dashboards'
FIELD_LOGS_ALERTS = 'logs_alerts'
FIELD_LOGS_2_METRICS = 'logs2metrics'
FIELD_METRICS_DASHBOARDS = 'metrics_dashboards'
FIELD_METRICS_ALERTS = 'metrics_alerts'
FIELD_DROP_FILTER = 'drop_filter'

REQUIRED_FIELDS = [FIELD_ID, FIELD_TITLE, FIELD_OVERVIEW, FIELD_PRODUCT, FIELD_OS, FIELD_FILTERS, FIELD_LOGO,
                   FIELD_LOGS_DASHBOARD, FIELD_LOGS_ALERTS, FIELD_LOGS_2_METRICS, FIELD_METRICS_DASHBOARDS,
                   FIELD_METRICS_ALERTS, FIELD_DROP_FILTER]

PRODUCT_LOGS = 'logs'
PRODUCT_METRICS = 'metrics'
PRODUCT_TRACES = 'tracing'
PRODUCT_SIEM = 'siem'

PRODUCTS = [PRODUCT_LOGS, PRODUCT_METRICS, PRODUCT_TRACES, PRODUCT_SIEM]

OS_LINUX = 'linux'
OS_WINDOWS = 'windows'
OS_MAC = 'mac'

OS = [OS_LINUX, OS_WINDOWS, OS_MAC]

ENV_FILES_TO_TRACK = 'FILES_TO_TRACK'
ENV_DOCS_PREFIX = 'DOCS_PREFIX'

DOCS_PATH = 'docs/shipping/'

OBJ_ID = 'id'
OBJ_FILE = 'file'
OBJ_TITLE = 'title'

MAX_FIELDS_TO_COVER = 20
