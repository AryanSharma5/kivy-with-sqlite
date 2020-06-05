from kivymd.app import MDApp
from kivy.lang.builder import Builder
from kivymd.toast.kivytoast import toast
from database import person, Database

class MyApp(MDApp):

	def on_start(self):
		self.p_obj = person()
		self.data = Database()

	def build(self):
		return Builder.load_file('main.kv')

	def signup(self):
		email = self.root.ids.email_signup.text
		password = self.root.ids.password_signup.text
		if not email and not password:
			return toast('email and password are not provided.')
		elif not email:
			return toast('email is not valid')
		elif not password:
			return toast('password is not valid')
		val = self.data.select_by_email(email = email)
		if val is None:
			self.p_obj.add_email(email)
			self.p_obj.add_password(password)
			self.data.add_entry(self.p_obj)
		else:
			return toast('already exists !!')
		return toast('registered successfully !!')

	def change_screen(self, direct = None):
		if direct is not None:
			self.root.ids.screen_manager.current = 'login'
			self.root.ids.screen_manager.transition.direction = 'right'
			self.root.ids.email.text = ''
			self.root.ids.password.text = ''
		else:
			self.root.ids.screen_manager.current = 'signup'
			self.root.ids.screen_manager.transition.direction = 'left'
			self.root.ids.email_signup.text = ''
			self.root.ids.password_signup.text = ''

	def validate(self):
		email = self.root.ids.email.text
		password = self.root.ids.password.text
		if not email and not password:
			return toast('email and password are not provided.')
		elif not email:
			return toast('email is not valid')
		elif not password:
			return toast('password is not valid')
		val = self.data.select_by_email(email = email)
		real_email, real_pass = [val, ('', '')][val is None]
		if real_email != email:
			toast('You are not registered !!')
		elif real_pass != password:
			toast('Incorrect Password !!')
		else:
			toast('login successfull !!')

MyApp().run()