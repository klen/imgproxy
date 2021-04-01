# ImgProxy

**ImgProxy** -- Python library to build [ImgProxy](https://docs.imgproxy.net/) URLs

[![Tests Status](https://github.com/klen/imgproxy/workflows/tests/badge.svg)](https://github.com/klen/imgproxy/actions) [![PYPI Version](https://img.shields.io/pypi/v/imgproxy)](https://pypi.org/project/imgproxy/) [![Python Versions](https://img.shields.io/pypi/pyversions/imgproxy)](https://pypi.org/project/imgproxy/)

---

## Features

* Support for [basic](https://docs.imgproxy.net/#/generating_the_url_basic) urls
* Support for [advanced](https://docs.imgproxy.net/#/generating_the_url_advanced) urls
* Support for [signing](https://docs.imgproxy.net/#/signing_the_url) urls


## Requirements

* python >= 3.8


## Installation

**imgproxy** should be installed using pip:

    pip install imgproxy


## Usage

[Simple](https://docs.imgproxy.net/#/generating_the_url_basic) URL format that
is easy to use but doesn’t support the whole range of imgproxy features:

```python
    from imgproxy import ImgProxy

    # Create ImgProxy object with required params
    url = ImgProxy('https://picsum.photos/1000', proxy_host='https://imgproxy.com', width=800, height=400)

    # Convert the obj to string to get imgproxy URL
    cover: str = str(url)

    # or just call it to get imgproxy URL
    cover: str = url()

    assert cover == 'https://imgproxy.com/insecure/auto/800/400/ce/0/aHR0cHM6Ly9waWNzdW0ucGhvdG9zLzEwMDA.'

    # Call the object with different params to customize the url
    cover_small: str = url(width=400, height=200, resizing_type='fill')

    assert cover_small == 'https://imgproxy.com/insecure/fill/400/200/ce/0/aHR0cHM6Ly9waWNzdW0ucGhvdG9zLzEwMDA.'

```

### Advanced options

[Advanced](https://docs.imgproxy.net/#/generating_the_url_advanced) URL format
allows the use of all the imgproxy features ():

```python
    from imgproxy import ImgProxy

    # Create ImgProxy object with required params
    url = ImgProxy('https://picsum.photos/1000', proxy_host='https://imgproxy.com')

    # Call it with advanced params to get an URL
    cover_with_border = url('pd:10:10:10:10', 'bg:F00')
    assert cover_with_border == 'https://imgproxy.com/insecure/pd:10:10:10:10/bg:F00/g:ce/rs:auto:0:0:0/aHR0cHM6Ly9waWNzdW0ucGhvdG9zLzEwMDA'

```

### Signed URLs

Imgproxy allows you to sign your URLs with key and salt, so an attacker won’t
be able to cause a denial-of-service attack by requesting multiple different
image resizes.

```python
    from imgproxy import ImgProxy

    url = ImgProxy('https://picsum.photos/1000', proxy_host='https://imgproxy.com', key="aa396160c50ea766910eab53", salt="b3fb8f215827bda5d0e7313d")

    assert str(url) == 'https://imgproxy.com/O0oYB8hKuQitvxu-WJuvSReEAnL-G2-fbGsb8m_Iiv4/auto/0/0/ce/0/aHR0cHM6Ly9waWNzdW0ucGhvdG9zLzEwMDA.'
```

If you need a random key/salt pair real fast, you can quickly generate it
using, for example, the following snippet:

```shell
    echo $(xxd -g 2 -l 64 -p /dev/random | tr -d '\n')
```



## Bug tracker

If you have any suggestions, bug reports or annoyances please report them to
the issue tracker at https://github.com/klen/imgproxy/issues


## Contributing

Development of the project happens at: https://github.com/klen/imgproxy


## License

Licensed under a [MIT License](http://opensource.org/licenses/MIT)
