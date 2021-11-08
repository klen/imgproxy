# ImgProxy

**ImgProxy** -- Python library to build [ImgProxy](https://docs.imgproxy.net/) URLs

[![Tests Status](https://github.com/klen/imgproxy/workflows/tests/badge.svg)](https://github.com/klen/imgproxy/actions)
[![PYPI Version](https://img.shields.io/pypi/v/imgproxy)](https://pypi.org/project/imgproxy/)
[![Python Versions](https://img.shields.io/pypi/pyversions/imgproxy)](https://pypi.org/project/imgproxy/)

---

## Features

* Support for [advanced](https://docs.imgproxy.net/#/generating_the_url_advanced) urls
* Support for [signing](https://docs.imgproxy.net/#/signing_the_url) urls
* URL's Factories with predefined params

# Table of Contents

  * [Requirements](#requirements)
  * [Installation](#installation)
  * [Usage](#usage)
    * [Options](#options)
    * [Signed URLs](#signed-urls)
    * [Image factories](#image-factories)
  * [Changelog](#changelog)
  * [Bug tracker](#bug-tracker)
  * [Contributing](#contributing)
  * [License](#license)


## Requirements

* python >= 3.7


## Installation

**imgproxy** should be installed using pip:

    $ pip install imgproxy


## Usage

```python
    from imgproxy import ImgProxy

    # Create ImgProxy object with required params
    img_url = ImgProxy('https://picsum.photos/1000', proxy_host='https://imgproxy.com', width=800, height=400)

    # Convert the obj to string to get imgproxy URL
    cover: str = str(img_url)

    # or just call it to get imgproxy URL
    cover: str = img_url()

    assert cover == 'https://imgproxy.com/insecure/g:ce/rs:auto:800:400:0/aHR0cHM6Ly9waWNzdW0ucGhvdG9zLzEwMDA'

    # Call the object with different params to customize the url
    cover_small: str = img_url(width=400, height=200, resizing_type='fill')

    assert cover_small == 'https://imgproxy.com/insecure/g:ce/rs:fill:400:200:0/aHR0cHM6Ly9waWNzdW0ucGhvdG9zLzEwMDA'

    # Call it with advanced params to get an URL
    cover_with_border = img_url('pd:10:10:10:10', 'bg:F00')
    assert cover_with_border == 'https://imgproxy.com/insecure/pd:10:10:10:10/bg:F00/g:ce/rs:auto:0:0:0/aHR0cHM6Ly9waWNzdW0ucGhvdG9zLzEwMDA'

```

### Options

Basic options (default values):

* `width: int = 0` - images width
* `height: int = 0` - images height
* `gravity: str = 'ce'` - images gravity
* `enlarge: bool = False` - enlarge an image
* `extension: str = ''` - images extension
* `resizing_type: str = 'auto'` - resizing type

```python
    from imgproxy import ImgProxy

    img_url = ImgProxy('https://picsum.photos/1000', proxy_host='https://imgproxy.com')
    thumbmail = img_url(width=100, height=100, gravity='no', extension='jpg', enlarge=True, resizing_type='fit')
```

Any other options are also supported when you call an imageproxy instance:

```python
    from imgproxy import ImgProxy

    img_url = ImgProxy('https://picsum.photos/1000', proxy_host='https://imgproxy.com')

    # Get rotated and blured image
    blured_rotated = img_url('blur:0.5', 'rotate:30')
```

### Signed URLs

Imgproxy allows you to sign your URLs with key and salt, so an attacker won’t
be able to cause a denial-of-service attack by requesting multiple different
image resizes.

```python
    from imgproxy import ImgProxy

    url = ImgProxy('https://picsum.photos/1000', proxy_host='https://imgproxy.com', key="aa396160c50ea766910eab53", salt="b3fb8f215827bda5d0e7313d")

    assert str(url) == 'https://imgproxy.com/FrH21u_5bXmv-OJ0APMayxZ0F3982xx437gCpqcQ0BM/g:ce/rs:auto:600:0:0/aHR0cHM6Ly9waWNzdW0ucGhvdG9zLzEwMDA'
```

If you need a random key/salt pair real fast, you can quickly generate it
using, for example, the following snippet:

```shell
    echo $(xxd -g 2 -l 64 -p /dev/random | tr -d '\n')
```

### Image factories

Usually imgproxy host and signature params are common for a project.
The library supports a method to generate a factory with predefined params:

```python
    from imgproxy import ImgProxy

    img_factory = ImgProxy.factory(proxy_host='https://imgproxy.com', key="aa396160c50ea766910eab53", salt="b3fb8f215827bda5d0e7313d")

    # ...

    # Generate image URL
    url = img_factory('https://picsum.photos/1000', width=600)
    assert str(url) == 'https://imgproxy.com/qcKAFfBJwpiKZ6xt-NT6GXGOGizkeq4sgyfoQ4h-080/g:ce/rs:auto:600:0:0/aHR0cHM6Ly9waWNzdW0ucGhvdG9zLzEwMDA'
```

Users able to predifine any basic params:
```python

    thumbnail_factory = ImgProxy.factory(proxy_host='https://imgproxy.com', width=300, height=200)
    preview_factory = ImgProxy.factory(proxy_host='https://imgproxy.com', width=500, resizing_type='fit')

    # and etc
```

Advanced params are also supported:

```python
    thumbnail_factory = ImgProxy.factory('bg:F00', 'pd:10:10:10:10', proxy_host='https://imgproxy.com', width=300, height=200)
```

## Changelog

* 2021-11-08: **[1.0.0]**
    - Support python 3.10
    - Support advanced options in factories

* 2021-09-14: **[0.4.0]**
    - Support python 3.7
    - Basic format has been removed (it's depricated in ImgProxy)

* 2021-04-02: **[0.2.3]** Stable release


## Bug tracker

If you have any suggestions, bug reports or annoyances please report them to
the issue tracker at https://github.com/klen/imgproxy/issues


## Contributing

Development of the project happens at: https://github.com/klen/imgproxy


## License

Licensed under a [MIT License](http://opensource.org/licenses/MIT)
