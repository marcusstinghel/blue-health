import os

from wepipe_python_sdk import Card, auth


def login():
    wepipe_domain = os.getenv("WEPIPE_DOMAIN")
    wepipe_email = os.getenv("WEPIPE_EMAIL")
    wepipe_password = os.getenv("WEPIPE_PASSWORD")
    auth.login(wepipe_domain, wepipe_email, wepipe_password)


def approval_compliance_to_approval_accountability(request):
    login()
    card = Card(request=request)
    for contact in card.contacts:
        if contact.email == 'felipe.cabral@bluehealthcorporate.com':
            card.pipeline_stage_id = 15766  # Approval - Accountability (VD)
            card.update()
            break


def approval_accountability_to_approval_financial(request):
    login()
    card = Card(request=request)
    for contact in card.contacts:
        if contact.email == 'vinicius.dezotti@bluehealthcorporate.com':
            card.pipeline_stage_id = 15767  # Approval - Financial (GV)
            card.update()
            break
