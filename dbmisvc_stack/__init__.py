"""
DBMISVC Stack
"""
from datetime import datetime

year = datetime.now().strftime("%Y")

__title__ = "dbmisvc-stack"
__description = "A command line program to facilitate development " "on a stack of containerized services"
__version__ = "1.0.1"
__url__ = "https://github.com/hms-dbmi/dbmisvc-stack.git"
__author__ = "HMS DBMI Technology Core"
__author_email__ = "bryan_larson@hms.harvard.edu"
__license__ = "BSD 2-Clause"
__copyright__ = "Copyright 2011-{} Harvard Medical School" " Department of Biomedical Informatics".format(year)

# Version synonym
VERSION = __version__

# Header encoding (see RFC5987)
HTTP_HEADER_ENCODING = "iso-8859-1"

# Default datetime input and output formats
ISO_8601 = "iso-8601"
