# DEPENDENCIES
import DiscoveryMethod
import UsualDiscoveryMethod
import Ease
import EaseRationale
import Safety
import SafetyRationale
import Improvements

class Respondent:
    def __init__(self):
        self.disc = DiscoveryMethod.DiscoveryMethod()
        self.udisc = UsualDiscoveryMethod.UsualDiscoveryMethod()
        self.ease = Ease.Ease()
        self.easeRat = EaseRationale.EaseRationale()
        self.safe = Safety.Safety()
        self.safeRat = SafetyRationale.SafetyRationale()
        self.improv = Improvements.Improvements()
