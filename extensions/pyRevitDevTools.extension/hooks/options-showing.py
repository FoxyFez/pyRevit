# pylint: skip-file
import os.path as op
from pyrevit import revit, USER_DESKTOP

count = 0
if revit.doc:
    count = len(revit.query.get_all_elements(doc=revit.doc))

with open(op.join(USER_DESKTOP, 'hooks.txt'), 'a') as f:
    f.write('\n'.join([
        'Displaying Options Dialog '.ljust(80, '-'),
        'PagesCount: ' + str(__eventargs__.PagesCount),
        'Element Count: ' + str(count)]) + '\n')