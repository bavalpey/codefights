"""
You've been actively exchanging email with one of your colleagues and noticed that you can't open his attachments. Unfortunately, he's
just went on a vacation and you need these attached files right now.

You've spent some time studying his emails and discovered that your colleague used the buggy email client which instead of using proper
MIME Base64 encoding for the attachments used other variants differing in characters that represent values 62 and 63.
Furthermore, different versions of this email client used different variations of the encoding!

Given the encoding of the email client which was used to send attachment,
decode it.
Example

For encoding = "-_" and message = "Q29kZUZpZ2h0cw==", the output should be
  weirdEncoding(encoding, message) = "CodeFights".
"""
import base64 as b64
def weirdEncoding(encoding, message):
    return b64.b64decode(message,encoding).decode()
