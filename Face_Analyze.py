import requests
import Face_Core as fc

Key = "Nlpg1nGz3f07878kwY0z93LGkVHYu3ME"  # 此处填写你在Face++上申请的API_Key
Secret = "JLINS4V2KX6oNlD01RYSyUR3OvhoODry"  # 此处填写你在Face++上申请的API_Secret
URL = "https://api-cn.faceplusplus.com/facepp/v3/face/analyze"


def face_analyze(picpath):
    facetoken = fc.GetFaceToken(picpath)
    info = {"api_key": Key, "api_secret": Secret, "face_tokens": facetoken,
            "return_attributes": "gender,age,smiling,eyestatus,emotion,ethnicity,beauty,mouthstatus,skinstatus"}
    response = requests.post(url=URL, data=info)
    return response.json()["faces"][0]["attributes"]


def detail_format(analyzestr):
    emotion = analyzestr["emotion"]
    beauty = analyzestr["beauty"]
    gender = analyzestr["gender"]
    age = analyzestr["age"]
    mouthstatus = analyzestr["mouthstatus"]
    glass = analyzestr["glass"]
    skinstatus = analyzestr["skinstatus"]
    smile = analyzestr["smile"]
    eyestatus_left = analyzestr["eyestatus"]["left_eye_status"]
    eyestatus_right = analyzestr["eyestatus"]["right_eye_status"]
    ethnicity = analyzestr["ethnicity"]
    print("性别分析结果:", end="")
    if gender["value"] == "Male":
        print("男性")
    else:
        print("女性")
    print("--------------------")
    print("年龄分析结果:" + str(age["value"]))
    print("--------------------")
    print("人种分析结果:", end="")
    if ethnicity['value'] == "ASIAN":
        print("黄种人")
    elif ethnicity["value"] == "WHITE":
        print("白种人")
    else:
        print("黑种人")
    print("--------------------")
    print("情绪分析结果")
    print("悲伤成分:" + str(emotion["sadness"]))
    print("厌恶成分:" + str(emotion["disgust"]))
    print("平静成分:" + str(emotion["neutral"]))
    print("愤怒成分:" + str(emotion["anger"]))
    print("惊讶成分:" + str(emotion["surprise"]))
    print("害怕成分:" + str(emotion["fear"]))
    print("高兴成分:" + str(emotion["happiness"]))
    print("--------------------")
    print("颜值分析结果")
    print("男性角度认为的此人颜值分数:" + str(beauty["male_score"]))
    print("女性角度认为的此人颜值分数:" + str(beauty["female_score"]))
    print("--------------------")
    print("嘴部状态分析结果")
    print("嘴部没有遮蔽且闭上的置信度:" + str(mouthstatus["close"]))
    print("嘴部没有遮蔽且张开的置信度:" + str(mouthstatus["open"]))
    print("嘴部被口罩遮挡的置信度:" + str(mouthstatus["surgical_mask_or_respirator"]))
    print("嘴部被其他物体遮挡的置信度:" + str(mouthstatus["other_occlusion"]))
    print("--------------------")
    print("左眼状态分析结果")
    print("被遮挡的置信度:" + str(eyestatus_left["occlusion"]))
    print("不戴眼镜且睁眼的置信度:" + str(eyestatus_left["no_glass_eye_open"]))
    print("佩戴普通眼镜且闭眼的置信度:" + str(eyestatus_left["normal_glass_eye_close"]))
    print("佩戴普通眼镜且睁眼的置信度:" + str(eyestatus_left["normal_glass_eye_open"]))
    print("佩戴墨镜的置信度:" + str(eyestatus_left["dark_glasses"]))
    print("不戴眼镜且闭眼的置信度:" + str(eyestatus_left["no_glass_eye_close"]))
    print("--------------------")
    print("右眼状态分析结果")
    print("被遮挡的置信度:" + str(eyestatus_right["occlusion"]))
    print("不戴眼镜且睁眼的置信度:" + str(eyestatus_right["no_glass_eye_open"]))
    print("佩戴普通眼镜且闭眼的置信度:" + str(eyestatus_right["normal_glass_eye_close"]))
    print("佩戴普通眼镜且睁眼的置信度:" + str(eyestatus_right["normal_glass_eye_open"]))
    print("佩戴墨镜的置信度:" + str(eyestatus_right["dark_glasses"]))
    print("不戴眼镜且闭眼的置信度:" + str(eyestatus_right["no_glass_eye_close"]))
    print("--------------------")
    print("笑容分析结果")
    print("笑容成分:" + str(smile["value"]))
    print("当笑容成分高于" + str(smile["threshold"]) + "时,可认为有笑容!")
    print("--------------------")
    print("面部特征分析结果")
    print("健康置信度:" + str(skinstatus["health"]))
    print("色斑置信度:" + str(skinstatus["stain"]))
    print("青春痘置信度:" + str(skinstatus["acne"]))
    print("黑眼圈置信度:" + str(skinstatus["dark_circle"]))


def generateHTML(analyzestr):
    emotion = analyzestr["emotion"]
    beauty = analyzestr["beauty"]
    gender = analyzestr["gender"]
    age = analyzestr["age"]
    mouthstatus = analyzestr["mouthstatus"]
    glass = analyzestr["glass"]
    skinstatus = analyzestr["skinstatus"]
    smile = analyzestr["smile"]
    eyestatus_left = analyzestr["eyestatus"]["left_eye_status"]
    eyestatus_right = analyzestr["eyestatus"]["right_eye_status"]
    ethnicity = analyzestr["ethnicity"]
    if gender["value"] == "Male":
        sex = "男性"
    else:
        sex = "女性"
    if ethnicity['value'] == "ASIAN":
        color = "黄种人"
    elif ethnicity["value"] == "WHITE":
        color = "白种人"
    else:
        color = "黑种人"
    file = open("FaceAnalyzeReport.html", mode="w", encoding="utf-8")
    try:
        file.write('''
            <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">

        </head>
        <body>
        <img src="test.jpg"  alt="人脸分析目标图片" />
        <p>性别分析结果:{}</p>
        <p>年龄分析结果:{}</p>
        <p>人种分析结果:{}</p>
        <hr>
        <h1>情绪分析结果</h1>
        <p>{}</p>
        <p>{}</p>
        <p>{}</p>
        <p>{}</p>
        <p>{}</p>
        <p>{}</p>
        <p>{}</p>
        <hr>
        <h1>颜值分析结果</h1>
        <p>{}</p>
        <p>{}</p>
        <hr>
        <h1>嘴部状态分析结果</h1>
        <p>{}</p>
        <p>{}</p>
        <p>{}</p>
        <p>{}</p>
        <hr>
        <h1>左眼状态分析结果</h1>
        <p>{}</p>
        <p>{}</p>
        <p>{}</p>
        <p>{}</p>
        <p>{}</p>
        <p>{}</p>
        <hr>
        <h1>右眼状态分析结果</h1>
        <p>{}</p>
        <p>{}</p>
        <p>{}</p>
        <p>{}</p>
        <p>{}</p>
        <p>{}</p>
        <hr>
        <h1>笑容分析结果</h1>
        <p>{}</p>
        <p>{}</p>
        <hr>
        <h1>面部特征分析结果</h1>
        <p>{}</p>
        <p>{}</p>
        <p>{}</p>
        <p>{}</p>
        </body>
        </html>'''.format(sex,
                          str(age["value"]), color, "悲伤成分:" + str(emotion["sadness"]),
                          "厌恶成分:" + str(emotion["disgust"]),
                          "平静成分:" + str(emotion["neutral"]), "愤怒成分:" + str(emotion["anger"]),
                          "惊讶成分:" + str(emotion["surprise"]), "害怕成分:" + str(emotion["fear"]),
                          "高兴成分:" + str(emotion["happiness"]), "男性角度认为的此人颜值分数:" + str(beauty["male_score"]),
                          "女性角度认为的此人颜值分数:" + str(beauty["female_score"]),
                          "嘴部没有遮蔽且闭上的置信度:" + str(mouthstatus["close"]), "嘴部没有遮蔽且张开的置信度:" + str(mouthstatus["open"]),
                          "嘴部被口罩遮挡的置信度:" + str(mouthstatus["surgical_mask_or_respirator"]),
                          "嘴部被其他物体遮挡的置信度:" + str(mouthstatus["other_occlusion"]),
                          "被遮挡的置信度:" + str(eyestatus_left["occlusion"]),
                          "不戴眼镜且睁眼的置信度:" + str(eyestatus_left["no_glass_eye_open"]),
                          "佩戴普通眼镜且闭眼的置信度:" + str(eyestatus_left["normal_glass_eye_close"]),
                          "佩戴普通眼镜且睁眼的置信度:" + str(eyestatus_left["normal_glass_eye_open"]),
                          "佩戴墨镜的置信度:" + str(eyestatus_left["dark_glasses"]),
                          "不戴眼镜且闭眼的置信度:" + str(eyestatus_left["no_glass_eye_close"]),
                          "被遮挡的置信度:" + str(eyestatus_right["occlusion"]),
                          "不戴眼镜且睁眼的置信度:" + str(eyestatus_right["no_glass_eye_open"]),
                          "佩戴普通眼镜且闭眼的置信度:" + str(eyestatus_right["normal_glass_eye_close"]),
                          "佩戴普通眼镜且睁眼的置信度:" + str(eyestatus_right["normal_glass_eye_open"]),
                          "佩戴墨镜的置信度:" + str(eyestatus_right["dark_glasses"]),
                          "不戴眼镜且闭眼的置信度:" + str(eyestatus_right["no_glass_eye_close"]),
                          "笑容成分:" + str(smile["value"]), "当笑容成分高于" + str(smile["threshold"]) + "时,可认为有笑容!",
                          "健康置信度:" + str(skinstatus["health"]), "色斑置信度:" + str(skinstatus["stain"]),
                          "青春痘置信度:" + str(skinstatus["acne"]), "黑眼圈置信度:" + str(skinstatus["dark_circle"])))
    except BaseException:
        return 0
    finally:
        file.close()
