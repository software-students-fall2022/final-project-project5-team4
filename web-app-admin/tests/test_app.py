from app import app

class Test:
	# def user_loader(self, user_id):
	# 	user = app.locate_user(user_id=user_id)
	# 	return user

	# def test_user_loader(self):
	# 	user = self.user_loader('639eabb4ae5a500934fe32a6')
	# 	assert user['email'] == 'nycadmin@nyu.edu'

	def test_add(self):
		client = app.test_client()
		url = '/add'
		response = client.get(url)
		assert response.status_code == 302

	def test_login(self):
		client = app.test_client()
		url = '/login'
		response = client.get(url)
		assert response.status_code == 200
		
	def test_register(self):
		client = app.test_client()
		url = '/register'
		response = client.get(url)
		assert response.status_code == 200

	def test_404(self):
		client = app.test_client()
		url = 'not-exist-url'
		response = client.get(url)
		assert response.status_code == 404