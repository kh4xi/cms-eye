import base64


def banner():
    title = b'CiAgICAgICAgICAgX19fX18gX18gIF9fICBfX19fXyAgICAgICBfX19fX19fXyAgICAgX19fX19fX18gCiAgICAgICAgICAvIF9fX198ICBcLyAgfC8gX19fX3wgICAgIHwgIF9fX19cIFwgICAvIC8gIF9fX198CiAgICAgICAgIHwgfCAgICB8IFwgIC8gfCAoX19fIF9fX19fX3wgfF9fICAgXCBcXy8gL3wgfF9fICAgCiAgICAgICAgIHwgfCAgICB8IHxcL3wgfFxfX18gXF9fX19fX3wgIF9ffCAgIFwgICAvIHwgIF9ffCAgCiAgICAgICAgIHwgfF9fX198IHwgIHwgfF9fX18pIHwgICAgIHwgfF9fX18gICB8IHwgIHwgfF9fX18gCiAgICAgICAgICBcX19fX198X3wgIHxffF9fX19fLyAgICAgIHxfX19fX198ICB8X3wgIHxfX19fX198ICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgZ2l0aHViLmNvbS9raDR4aS9jbXNleWUgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAo='
    decoded_tit = base64.b64decode(title).decode('utf-8')
    return decoded_tit


