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
	
	def test_filter(self):
		client = app.test_client()
		url = '/filter'
		response = client.get(url)
		assert response.status_code == 200

	def test_filter_post_borough(client):
		response = client.post("/filter", data={
			"fborough": "Bronx",
			"flower": "",
			"fupper": ""
		})
		assert response.status_code == 200

	def test_filter_post_lower(client):
		response = client.post("/filter", data={
			"fborough": "",
			"flower": 1000,
			"fupper": ""
		})
		assert response.status_code == 200

	def test_filter_post_upper(client):
		response = client.post("/filter", data={
			"fborough": "",
			"flower": "",
			"fupper": 50000
		})
		assert response.status_code == 200
