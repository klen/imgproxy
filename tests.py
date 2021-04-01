def test_unsigned():
    from imgproxy import ImgProxy

    url = ImgProxy('https://picsum.photos/1000')
    assert url
    assert str(url) == '/insecure/auto/0/0/ce/0/aHR0cHM6Ly9waWNzdW0ucGhvdG9zLzEwMDA'
    assert url() == '/insecure/auto/0/0/ce/0/aHR0cHM6Ly9waWNzdW0ucGhvdG9zLzEwMDA'
    assert url(width=200) == '/insecure/auto/200/0/ce/0/aHR0cHM6Ly9waWNzdW0ucGhvdG9zLzEwMDA'


def test_signed():
    from imgproxy import ImgProxy

    url = ImgProxy(
        'https://picsum.photos/1000',
        key="aa396160c50ea766910eab53",
        salt="b3fb8f215827bda5d0e7313d")
    assert url
    assert str(url) == '/-YNDbmoa34gFOv79aRKmlXHxGNlHn0yDv111VZ5HAxo/auto/0/0/ce/0/aHR0cHM6Ly9waWNzdW0ucGhvdG9zLzEwMDA'


def test_advanced():
    from imgproxy import ImgProxy

    url = ImgProxy('https://picsum.photos/1000')
    assert url('pd:10:10:10:10', 'bg:F00') == '/insecure/pd:10:10:10:10/bg:F00/g:ce/rs:auto:0:0:0/aHR0cHM6Ly9waWNzdW0ucGhvdG9zLzEwMDA'


def test_factory():
    from imgproxy import ImgProxy

    factory = ImgProxy.factory(proxy_host='https://imgproxy.com')
    url = factory('https://picsum.photos/1000', width=600)
    assert str(url) == 'https://imgproxy.com/insecure/auto/600/0/ce/0/aHR0cHM6Ly9waWNzdW0ucGhvdG9zLzEwMDA'

    url = factory('https://picsum.photos/id/237/1000', width=200)
    assert str(url) == 'https://imgproxy.com/insecure/auto/200/0/ce/0/aHR0cHM6Ly9waWNzdW0ucGhvdG9zL2lkLzIzNy8xMDAw'


def test_readme():
    from imgproxy import ImgProxy

    url = ImgProxy(
        'https://picsum.photos/1000', proxy_host='https://imgproxy.com', width=800, height=400)
    assert str(url) == 'https://imgproxy.com/insecure/auto/800/400/ce/0/aHR0cHM6Ly9waWNzdW0ucGhvdG9zLzEwMDA'
    assert url(width=400, height=200, resizing_type='fill') == 'https://imgproxy.com/insecure/fill/400/200/ce/0/aHR0cHM6Ly9waWNzdW0ucGhvdG9zLzEwMDA'

    url = ImgProxy(
        'https://picsum.photos/1000', proxy_host='https://imgproxy.com')
    assert url('pd:10:10:10:10', 'bg:F00') == 'https://imgproxy.com/insecure/pd:10:10:10:10/bg:F00/g:ce/rs:auto:0:0:0/aHR0cHM6Ly9waWNzdW0ucGhvdG9zLzEwMDA'

    img_factory = ImgProxy.factory(proxy_host='https://imgproxy.com', key="aa396160c50ea766910eab53", salt="b3fb8f215827bda5d0e7313d")
    url = img_factory('https://picsum.photos/1000', width=600)
    assert str(url) == 'https://imgproxy.com/11ZRY6Zmms1m4O4sCiY7Km2pKH3KPTELS-YYgSGgWKA/auto/600/0/ce/0/aHR0cHM6Ly9waWNzdW0ucGhvdG9zLzEwMDA'

# pylama:ignore=E501
