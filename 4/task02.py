from urllib.request import urlopen


def count_dots_on_i(url: str) -> int:
    try:
        with urlopen(url) as response:
            html = response.read().decode()
        count = html.count('i')
        return count
    except:
        raise ValueError(f"Unreachable {url}")
