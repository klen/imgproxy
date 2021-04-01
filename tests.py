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
    assert str(url) == '/O0oYB8hKuQitvxu-WJuvSReEAnL-G2-fbGsb8m_Iiv4/auto/0/0/ce/0/aHR0cHM6Ly9waWNzdW0ucGhvdG9zLzEwMDA.'  # noqa


def test_advanced():
    from imgproxy import ImgProxy

    url = ImgProxy('https://picsum.photos/1000')
    assert url('pd:10:10:10:10', 'bg:F00') == '/insecure/pd:10:10:10:10/bg:F00/g:ce/rs:auto:0:0:0/aHR0cHM6Ly9waWNzdW0ucGhvdG9zLzEwMDA'  # noqa
