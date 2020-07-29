from django.contrib.auth.models import User
from .models import Profile, Jobs




class Accounting(Profile):
	"""docstring for Accounting"""
	user = Profile.user

	def __init__(self, arg):
		super(Accounting, self).__init__()
		self.arg = arg
		
	def newMission(self, **kwargs):

		if user.is_staff():
			currentMission =
		pass