import os
from collections.abc import Iterable

from wepipe_python_sdk import Card, auth


def login():
    wepipe_domain = os.getenv("WEPIPE_DOMAIN")
    wepipe_email = os.getenv("WEPIPE_EMAIL")
    wepipe_password = os.getenv("WEPIPE_PASSWORD")
    auth.login(wepipe_domain, wepipe_email, wepipe_password)


def approval_compliance_to_approval_accountability(card: Card):
    login()
    if isinstance(card.contacts, Iterable):
        for contact in card.contacts:
            if contact.email == 'felipe.cabral@bluehealthcorporate.com':
                card.pipeline_stage_id = 15766  # Approval - Accountability (VD)
                card.update()
                break


def approval_accountability_to_approval_financial(card: Card):
    login()
    if isinstance(card.contacts, Iterable):
        for contact in card.contacts:
            if contact.email == 'vinicius.dezotti@bluehealthcorporate.com':
                card.pipeline_stage_id = 15767  # Approval - Financial (GV)
                card.update()
                break
