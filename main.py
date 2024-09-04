from atproto import Client

client = Client(base_url='https://bsky.social')
client.login('soniclavouope.bsky.social', 'p4s2-g625-cyc4-td2r')

with open('sonic.jpg', 'rb') as f:
    img_data = f.read()

client.send_image(text='não.', image=img_data)