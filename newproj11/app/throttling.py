from rest_framework.throttling import UserRateThrottle
class AreebaRateThrottle(UserRateThrottle):
    scope='Areeba'
