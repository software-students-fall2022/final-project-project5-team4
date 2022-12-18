from app import app

class Test:
	def test_sentiment_list_view(self):
		client = app.test_client()
		url = 'sentiment-list-view'
		response = client.get(url)
		assert response.status_code == 200

	def test_sentiment_result_view(self):
		client = app.test_client()
		url = 'sentiment-result-view'
		response = client.get(url)
		assert response.status_code == 200

	def test_404(self):
		client = app.test_client()
		url = 'not-exist-url'
		response = client.get(url)
		assert response.status_code == 404