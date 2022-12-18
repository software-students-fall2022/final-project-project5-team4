from app import app

class Test:
	def test_account_favorites(self):
		client = app.test_client()
		url = '/account'
		response = client.get(url)
		assert response.status_code == 200

	def test_account_reviews(self):
		client = app.test_client()
		url = '/account/reviews'
		response = client.get(url)
		assert response.status_code == 200

	def test_404(self):
		client = app.test_client()
		url = 'not-exist-url'
		response = client.get(url)
		assert response.status_code == 404