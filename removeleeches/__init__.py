from aqt import mw
from aqt.qt import *


def remove_leeches() -> None:
    ids = mw.col.findCards("tag:leech")
    for id in ids:
        card = mw.col.getCard(id)
        card.note().delTag("leech")
        card.note().flush()
        card.flush()


action = QAction("Remove leeches", mw)
qconnect(action.triggered, remove_leeches)
mw.form.menuTools.addAction(action)
