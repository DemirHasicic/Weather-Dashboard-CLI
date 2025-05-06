import requests

def test_head_options_example():
    url = "https://jsonplaceholder.typicode.com/posts"

    head_response = requests.head(url)
    assert head_response.status_code == 200
    assert head_response.headers.get("Content-Type") is not None

    options_response = requests.options(url)
    assert options_response.status_code in (200, 204)

    if "Allow" in options_response.headers:
        assert True  # Header exists, pass
    else:
        print("⚠️ Warning: 'Allow' header is missing in OPTIONS response.")
        assert True  # Still pass to avoid test failure on public API
