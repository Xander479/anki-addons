from aqt import mw
from aqt.qt import *
from aqt.utils import showInfo


def remove_leeches() -> None:
    ids = mw.col.findCards("tag:leech")
    if not ids:
        showInfo("No leeches found.")
    else:
        for id in ids:
            card = mw.col.getCard(id)
            card.note().delTag("leech")
            card.note().flush()
            card.flush()
            showInfo("Finished removing leeches.")


action = QAction("Remove leeches", mw)
qconnect(action.triggered, remove_leeches)
mw.form.menuTools.addAction(action)
