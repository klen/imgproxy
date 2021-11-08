def test_unsigned():
    from imgproxy import ImgProxy

    img_url = ImgProxy('https://picsum.photos/1000')
    assert img_url
    assert str(img_url) == '/insecure/g:ce/rs:auto:0:0:0/aHR0cHM6Ly9waWNzdW0ucGhvdG9zLzEwMDA'
    assert img_url() == '/insecure/g:ce/rs:auto:0:0:0/aHR0cHM6Ly9waWNzdW0ucGhvdG9zLzEwMDA'
    assert img_url(width=200) == '/insecure/g:ce/rs:auto:200:0:0/aHR0cHM6Ly9waWNzdW0ucGhvdG9zLzEwMDA'


def test_signed():
    from imgproxy import ImgProxy

    img_url = ImgProxy(
        'https://picsum.photos/1000',
        key="aa396160c50ea766910eab53",
        salt="b3fb8f215827bda5d0e7313d")
    assert img_url
    assert str(img_url) == '/Da25ef1zWhx4P9hhPWGdFRU8_dYcGvloGHvEZ1c3_0o/g:ce/rs:auto:0:0:0/aHR0cHM6Ly9waWNzdW0ucGhvdG9zLzEwMDA'


def test_advanced():
    from imgproxy import ImgProxy

    img_url = ImgProxy('https://picsum.photos/1000')
    assert img_url('pd:10:10:10:10', 'bg:F00') == '/insecure/pd:10:10:10:10/bg:F00/g:ce/rs:auto:0:0:0/aHR0cHM6Ly9waWNzdW0ucGhvdG9zLzEwMDA'

    assert img_url('bl:0.5') == '/insecure/bl:0.5/g:ce/rs:auto:0:0:0/aHR0cHM6Ly9waWNzdW0ucGhvdG9zLzEwMDA'


def test_factory():
    from imgproxy import ImgProxy

    factory = ImgProxy.factory(proxy_host='https://imgproxy.com')
    url = factory('https://picsum.photos/1000', width=600)
    assert str(url) == 'https://imgproxy.com/insecure/g:ce/rs:auto:600:0:0/aHR0cHM6Ly9waWNzdW0ucGhvdG9zLzEwMDA'

    url = factory('https://picsum.photos/id/237/1000', width=200)
    assert str(url) == 'https://imgproxy.com/insecure/g:ce/rs:auto:200:0:0/aHR0cHM6Ly9waWNzdW0ucGhvdG9zL2lkLzIzNy8xMDAw'

    assert url('bl:0.5') == 'https://imgproxy.com/insecure/bl:0.5/g:ce/rs:auto:200:0:0/aHR0cHM6Ly9waWNzdW0ucGhvdG9zL2lkLzIzNy8xMDAw'


def test_factory_advanced():
    from imgproxy import ImgProxy

    factory = ImgProxy.factory('bg:F00', 'pd:10:10:10:10', proxy_host='https://imgproxy.com')
    url = factory('https://picsum.photos/id/237/1000')
    assert str(url) == 'https://imgproxy.com/insecure/bg:F00/pd:10:10:10:10/g:ce/rs:auto:0:0:0/aHR0cHM6Ly9waWNzdW0ucGhvdG9zL2lkLzIzNy8xMDAw'

    factory = ImgProxy.factory(proxy_host='https://imgproxy.com', advanced=['bg:F00', 'pd:10:10:10:10'])

    url = factory('https://picsum.photos/id/237/1000', width=200)
    assert str(url) == 'https://imgproxy.com/insecure/bg:F00/pd:10:10:10:10/g:ce/rs:auto:200:0:0/aHR0cHM6Ly9waWNzdW0ucGhvdG9zL2lkLzIzNy8xMDAw'

    url = factory('https://picsum.photos/id/237/1000', 'bl:0.5')
    assert str(url) == 'https://imgproxy.com/insecure/bg:F00/pd:10:10:10:10/bl:0.5/g:ce/rs:auto:0:0:0/aHR0cHM6Ly9waWNzdW0ucGhvdG9zL2lkLzIzNy8xMDAw'


def test_readme():
    from imgproxy import ImgProxy

    url = ImgProxy(
        'https://picsum.photos/1000', proxy_host='https://imgproxy.com', width=800, height=400)
    assert str(url) == 'https://imgproxy.com/insecure/g:ce/rs:auto:800:400:0/aHR0cHM6Ly9waWNzdW0ucGhvdG9zLzEwMDA'
    assert url(width=400, height=200, resizing_type='fill') == 'https://imgproxy.com/insecure/g:ce/rs:fill:400:200:0/aHR0cHM6Ly9waWNzdW0ucGhvdG9zLzEwMDA'

    url = ImgProxy(
        'https://picsum.photos/1000', proxy_host='https://imgproxy.com')
    assert url('pd:10:10:10:10', 'bg:F00') == 'https://imgproxy.com/insecure/pd:10:10:10:10/bg:F00/g:ce/rs:auto:0:0:0/aHR0cHM6Ly9waWNzdW0ucGhvdG9zLzEwMDA'

    img_factory = ImgProxy.factory(proxy_host='https://imgproxy.com', key="aa396160c50ea766910eab53", salt="b3fb8f215827bda5d0e7313d")
    url = img_factory('https://picsum.photos/1000', width=600)
    assert str(url) == 'https://imgproxy.com/qcKAFfBJwpiKZ6xt-NT6GXGOGizkeq4sgyfoQ4h-080/g:ce/rs:auto:600:0:0/aHR0cHM6Ly9waWNzdW0ucGhvdG9zLzEwMDA'

# pylama:ignore=E501
