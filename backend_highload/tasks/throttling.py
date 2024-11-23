from rest_framework.throttling import UserRateThrottle

class AdminRateThrottle(UserRateThrottle):
    rate = '20/min'
