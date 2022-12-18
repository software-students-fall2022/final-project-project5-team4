from app import app

class Test:
	def test_404(self):
		client = app.test_client()
		url = 'not-exist-url'
		response = client.get(url)
		assert response.status_code == 404