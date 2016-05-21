# Helper functions for interacting with login


def logged_in(request):
    if 'email_address' in request.session:
        return True
    else:
        return False
