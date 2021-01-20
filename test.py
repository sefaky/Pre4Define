import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r"C:\Users\Gokturk\PycharmProjects\ColorProject\googleId\MIS Ders-0d176df9ed9d.json"

def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    import io
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    for text in texts:
        print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        print('bounds: {}'.format(','.join(vertices)))

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))


def detect_text_uri(uri):
    """Detects text in the file located in Google Cloud Storage or on the Web.
    """
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = uri

    response = client.text_detection(image=image)
    texts = response.text_annotations
    i = 0
    l = []
    for text in texts:
        if (i > 0):
            l.append(text.description)
        i+=1
    print(l)

    if response.error.message:
        return []

    return l

#detect_text_uri("https://lh3.googleusercontent.com/-50Bgt2JNtqCBWOY5u-LKwfEJsbfTzSp0gLV3cVsxeV18lXeNIujvEccrWvtzYWhnj8OF6vn3UGugSogcuesaUQ")
#detect_text(r"C:\Users\Gokturk\PycharmProjects\ColorProject\images\aaa.jpeg")