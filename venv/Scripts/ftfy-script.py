#!C:\Users\user\PycharmProjects\Requests\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'ftfy==4.4.3','console_scripts','ftfy'
__requires__ = 'ftfy==4.4.3'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('ftfy==4.4.3', 'console_scripts', 'ftfy')()
    )
