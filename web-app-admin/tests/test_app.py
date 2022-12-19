from app import app as flask_app 
import app  # app.py


class Test:

	def test_user_loader_id(self):
		user = app.locate_user(user_id='639eabb4ae5a500934fe32a6')
		assert user is not None

	def test_user_loader_username(self):
		user = app.locate_user(username='nycadmin')
		assert user is not None

	def test_user_loader_none(self):
		user = app.locate_user(username='tesetsetsetsetset')
		assert user is None

	def test_user_loader(self):
		user = app.user_loader('639eabb4ae5a500934fe32a6')
		assert user is not None

	def test_add(self):
		client = flask_app.test_client()
		url = '/add'
		response = client.get(url)
		assert response.status_code == 302

	def test_home(self):
		client = flask_app.test_client()
		url = '/'
		response = client.get(url)
		assert response.status_code == 302

	def test_login(self):
		client = flask_app.test_client()
		url = '/login'
		response = client.get(url)
		assert response.status_code == 200

	def test_login_submit_wrong(self):
		url = '/login'
		response = flask_app.test_client().post(url, data = {'username':'test', 'password':'test'}, follow_redirects=True)
		assert response.status_code == 200

	def test_login_submit_exist(self):
		url = '/login'
		response = flask_app.test_client().post(url, data = {'username':'nycadmin', 'password':'nycadmin'}, follow_redirects=True)
		assert response.status_code == 200
	
	def test_login_submit_already(self):
		client = flask_app.test_client()
		self.login(client)
		url = '/login'
		response = client.get(url)
		assert response.status_code == 302
	
	def test_logout(self):
		client = flask_app.test_client()
		url = '/logout'
		response = client.get(url)
		assert response.status_code == 302
		
	def test_register(self):
		client = flask_app.test_client()
		url = '/register'
		response = client.get(url)
		assert response.status_code == 200

	def test_register_submit(self):
		url = '/register'
		response = flask_app.test_client().post(url, data = {'username':'test', 'password':'test', 'email': 'test@gmail.com'}, follow_redirects=True)
		assert response.status_code == 200
		app.db.admins.delete_one({'username':'test'})

	def test_register_submit_already(self):
		client = flask_app.test_client()
		self.login(client)
		url = '/register'
		response = client.get(url)
		assert response.status_code == 302	

	def test_register_submit_long_username(self):
		url = '/register'
		response = flask_app.test_client().post(url, data = {'username':'testtesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttesttest', 'password':'test', 'email': 'test@gmail.com'}, follow_redirects=True)
		assert response.status_code == 200

	def test_register_submit_invalid_email(self):
		url = '/register'
		response = flask_app.test_client().post(url, data = {'username':'test', 'password':'test', 'email': 'testgmail.com'}, follow_redirects=True)
		assert response.status_code == 200

	def test_register_submit_already_exist(self):
		url = '/register'
		response = flask_app.test_client().post(url, data = {'username':'nycadmin', 'password':'test', 'email': 'testgmail.com'}, follow_redirects=True)
		assert response.status_code == 200

	def login(self, client):
		return client.post(
			"/login",
			data=dict(username='testing', password='testing'), 
			follow_redirects=True
		)

	def test_add_apartment_get(self):
		client = flask_app.test_client()
		self.login(client)
		url = '/add'
		response = client.get(url)
		assert response.status_code == 200

	def test_add_apartment_post(self):
		client = flask_app.test_client()
		self.login(client)
		url = '/add'
		response = client.post(url, data = {'name':'test', 'address': 'test address', 'borough': 'Manhattan', 'photo': 'https://www.testim.io/wp-content/uploads/2019/11/Testim-What-is-a-Test-Environment_-A-Guide-to-Managing-Your-Testing-A.png', 'year_of_construction': 2000, 'price': 10000}, follow_redirects=True)
		assert response.status_code == 200

	def test_add_apartment_post_bi(self):
		client = flask_app.test_client()
		self.login(client)
		url = '/add'
		response = client.post(url, data = {'name':'test 2', 'address': 'test address 2', 'borough': 'Manhattan', 'photo': 'https://www.testim.io', 'year_of_construction': 2000,'price': 10000,'pet_friendly': 'pet_friendly','doorman':'doorman','laundry_in_building':'laundry_in_building','parking':'parking','elevator':'elevator','gym':'gym'}, follow_redirects=True)
		assert response.status_code == 200


	def test_404(self):
		client = flask_app.test_client()
		url = 'not-exist-url'
		response = client.get(url)
		assert response.status_code == 404