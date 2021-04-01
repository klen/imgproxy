def test_unsigned():
    from imgproxy import ImgProxy

    url = ImgProxy('https://picsum.photos/1000')
    assert url
    assert str(url) == '/insecure/auto/0/0/ce/0/aHR0cHM6Ly9waWNzdW0ucGhvdG9zLzEwMDA.'
    assert url() == '/insecure/auto/0/0/ce/0/aHR0cHM6Ly9waWNzdW0ucGhvdG9zLzEwMDA.'
    assert url(width=200) == '/insecure/auto/200/0/ce/0/aHR0cHM6Ly9waWNzdW0ucGhvdG9zLzEwMDA.'


def test_signed():
    from imgproxy import ImgProxy

    url = ImgProxy(
        'https://picsum.photos/1000',
        key="aa396160c50ea766910eab53",
        salt="b3fb8f215827bda5d0e7313d")
    assert url
    assert str(url) == '/O0oYB8hKuQitvxu-WJuvSReEAnL-G2-fbGsb8m_Iiv4/auto/0/0/ce/0/aHR0cHM6Ly9waWNzdW0ucGhvdG9zLzEwMDA.'


def test_advanced():
    from imgproxy import ImgProxy

    url = ImgProxy('https://picsum.photos/1000')
    assert url('pd:10:10:10:10', 'bg:F00') == '/insecure/pd:10:10:10:10/bg:F00/g:ce/rs:auto:0:0:0/aHR0cHM6Ly9waWNzdW0ucGhvdG9zLzEwMDA'


def test_readme():
    from imgproxy import ImgProxy

    url = ImgProxy(
        'https://picsum.photos/1000', proxy_host='https://imgproxy.com', width=800, height=400)
    assert str(url) == 'https://imgproxy.com/insecure/auto/800/400/ce/0/aHR0cHM6Ly9waWNzdW0ucGhvdG9zLzEwMDA.'
    assert url(width=400, height=200, resizing_type='fill') == 'https://imgproxy.com/insecure/fill/400/200/ce/0/aHR0cHM6Ly9waWNzdW0ucGhvdG9zLzEwMDA.'

    url = ImgProxy(
        'https://picsum.photos/1000', proxy_host='https://imgproxy.com')
    assert url('pd:10:10:10:10', 'bg:F00') == 'https://imgproxy.com/insecure/pd:10:10:10:10/bg:F00/g:ce/rs:auto:0:0:0/aHR0cHM6Ly9waWNzdW0ucGhvdG9zLzEwMDA'

# pylama:ignore=E501
