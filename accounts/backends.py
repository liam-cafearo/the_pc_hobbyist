from models import User


class EmailAuth(object):

    def authenticate(self, email=None, password=None):
        # grab user via supplied email and password
        try:
            user = User.objects.get(email=email)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        # Django auth system uses this to get an instance of the user
        try:
            user = User.objects.get(pk=user_id)
            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None
