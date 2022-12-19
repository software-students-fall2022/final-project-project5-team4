from app import app as flask_app 
import app  # app.py
import pymongo
import flask_login

class Test:
	def test_account_favorites(self):
		client = flask_app.test_client()
		url = '/account'
		response = client.get(url)
		assert response.status_code == 200
  
	def test_account_reviews(self):
		client = flask_app.test_client()
		url = '/account/reviews'
		response = client.get(url)
		assert response.status_code == 200

	def test_404(self):
		client = flask_app.test_client()
		url = 'not-exist-url'
		response = client.get(url)
		assert response.status_code == 404
  
	def test_user_loader_id(self):
		user = app.locate_user(user_id='639e7fee2982074884ec55c6')
		assert user is not None

	def test_user_loader_username(self):
		user = app.locate_user(username='admin')
		assert user is not None

	def test_user_loader_none(self):
		user = app.locate_user(username='tesetsetsetsetset')
		assert user is None

	def test_user_loader(self):
		user = app.user_loader('639e7fee2982074884ec55c6')
		assert user is not None
  
	def test_home(self):
		client = flask_app.test_client()
		url = '/'
		response = client.get(url)
		assert response.status_code == 302
  
	def login(self, client):
		return client.post(
		"/login",
		data=dict(username='testing', password='testing'), 
		follow_redirects=True
		)
  
	def test_home_login(self):
		client = flask_app.test_client()
		self.login(client)
		url = '/'
		response = client.get(url)
		assert response.status_code == 302
  
	def test_filter_basic(self):
		client = flask_app.test_client()
		url = '/filter'
		response = client.get(url)
		assert response.status_code == 200
  
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
		response = flask_app.test_client().post(url, data = {'username':'admin', 'password':'password'}, follow_redirects=True)
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
  
	def test_apartment(self):
		client = flask_app.test_client()
		url = '/apartments/639e81b2f05783bc5e25824f'
		response = client.get(url)
		assert response.status_code == 200
  
	def test_apartment_no_review(self):
		client = flask_app.test_client()
		url = '/apartments/639ff69374667ef41729ac53'
		response = client.get(url)
		assert response.status_code == 200
  
	def test_apartment_login(self):
		client = flask_app.test_client()
		self.login(client)
		url = '/apartments/639e81b2f05783bc5e25824f'
		response = client.get(url)
		assert response.status_code == 200
  
	def test_apartment_not_exist(self):
		client = flask_app.test_client()
		url = '/apartments/639e81b2f05783bc5e25823f'
		response = client.get(url)
		assert response.status_code == 302

	def test_apartment_like(self):
		client = flask_app.test_client()
		self.login(client)
		url = '/apartments/639e81b2f05783bc5e25824f'
		response = client.post(url, data = {}, follow_redirects=True)
		assert response.status_code == 200
		response = client.post(url, data = {}, follow_redirects=True)
		assert response.status_code == 200
  
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
		response = flask_app.test_client().post(url, data = {'username':'admin', 'password':'password', 'email': 'testgmail.com'}, follow_redirects=True)
		assert response.status_code == 200
	
	def test_register_already_log_in(self):     
		client = flask_app.test_client()
		self.login(client)
		url = '/register'
		response = client.get(url)
		assert response.status_code == 302
  
	def test_register_get(self):     
		client = flask_app.test_client()
		url = '/register'
		response = client.get(url)
		assert response.status_code == 200
  
	def test_register_submit(self):
		url = '/register'
		response = flask_app.test_client().post(url, data = {'username':'test', 'password':'test', 'email': 'test@gmail.com'}, follow_redirects=True)
		assert response.status_code == 200
		app.db.admins.delete_one({'username':'test'})

	def test_add_review_not_login(self):     
		client = flask_app.test_client()
		url = '/add_review/639ff1a074667ef41729ac52'
		response = client.get(url)
		assert response.status_code == 302
  
	def test_add_review_login(self):          
		client = flask_app.test_client()
		self.login(client)
		url = '/add_review/639ff1a074667ef41729ac52'
		response = client.get(url)
		assert response.status_code == 200  
  
	def test_add_review_post(self):
		client = flask_app.test_client()
		self.login(client)
		url = '/add_review/639ff1a074667ef41729ac52'
		response = client.post(url, data = {'comments':'test', 'rating':1, 'price': 1}, follow_redirects=True)
		assert response.status_code == 200
		app.db.admins.delete_one({"address_id": "639ff1a074667ef41729ac52"})
  
	def test_account_login(self):
		client = flask_app.test_client()
		self.login(client)
		url = '/account'
		response = client.get(url)
		assert response.status_code == 200  
	
	def test_account_review_login(self):
		client = flask_app.test_client()
		self.login(client)
		url = '/account/reviews'
		response = client.get(url)
		assert response.status_code == 200  
