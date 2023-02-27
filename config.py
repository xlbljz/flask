# 里面放着相关的秘钥等信息
import os
OPENAI_KEY='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'
WECOM_AESKEY='kwdm58Mxh2izId3zhxkLAbTqKoz43B0EQwKwuEaRyLG'
WECOM_APP_SECRET='Qg-Xw_2wqCBrbhFl3h-MWaSavPUpD_krBeOS7kofq6g'
WECOM_COMID='wwff0560f161514799'
WECOM_TOKEN='kyfYSug6PrnlhX5wp3jvtvVhuLwQM6q'
globals().update(os.environ)
# openaikey
openaikey = OPENAI_KEY
# 企业微信的接口回调token
sToken = WECOM_TOKEN
# 企业微信的接口回调AESKEY
sEncodingAESKey = WECOM_AESKEY
# 企业微信的企业ID
sCorpID = WECOM_COMID
#  腾讯云的函数公网访问域名
# 应用secret
corpsecret = WECOM_APP_SECRET

# [Speechsdk]
Key = '05d77b4c92014362bcb9c682c279480c'
Region = 'japaneast'
#  use_default_speaker
Audio_config = True
# The language and the voice that speaks.
Voice = 'ja-JP-MayuNeural'

# [ChatGPT]
Email = 'xlbljz.com'
Password = 'xiaolongbao123'
