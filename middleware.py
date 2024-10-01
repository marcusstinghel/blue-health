from wepipe_python_sdk import Card


def approval_compliance_to_approval_accountability(request):
    card = Card(request=request)
    for contact in card.contacts:
        if contact.email == 'felipe.cabral@bluehealthcorporate.com':
            card.pipeline_stage_id = 15766  # Approval - Accountability (VD)
            card.update()
            break


def approval_accountability_to_approval_financial(request):
    card = Card(request=request)
    for contact in card.contacts:
        if contact.email == 'vinicius.dezotti@bluehealthcorporate.com':
            card.pipeline_stage_id = 15767  # Approval - Financial (GV)
            card.update()
            break
