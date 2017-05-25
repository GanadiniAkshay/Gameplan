from flask import Flask
from flask_wizard import response

def hi(session):
    # gen_temp = response.template(
    #     type="generic",
    #     elements=[
    #         response.template_element(
    #             title="Welcome to Peter's hats",
    #             image_url="https://petersfancybrownhats.com/company_image.png",
    #             subtitle="We got the right hat for everyone",
    #             action=response.actions(type="web_url",url="http://google.com",webview_height_ratio="tall"),
    #             buttons=[
    #                 response.button(
    #                     type="web_url",
    #                     url="https://google.com",
    #                     title="show website"
    #                 ),
    #                 response.button(
    #                     type="postback",
    #                     title="Start Chatting",
    #                     payload="Try chatt"
    #                 )
    #             ]
    #         )
    #     ]
    # )   
    # response.send(session, gen_temp)
    temp = response.template(
        type="button",
        text="Ozzy the bozzy",
        buttons=[
                    response.button(
                        type="web_url",
                        url="https://google.com",
                        title="show website"
                    ),
                    response.button(
                        type="postback",
                        title="Start Chatting",
                        payload="Try chatt"
                    ),
                    response.button(
                        type="account_unlink"
                    )
                    # response.button(
                    #     type="account_link",
                    #     url="https://example.com/authorize"
                    # )
                    # response.button(
                    #     type="phone_number",
                    #     title="Call Reprsentative",
                    #     payload="+919505147139"
                    # ),
                    # response.button(
                    #     type="element_share"
                    # )
                ]
    )
    response.send(session,temp)
    # video = response.attachement(
    #     type="video",
    #     url="http://dev.exiv2.org/attachments/341/video-2012-07-05-02-29-27.mp4"
    # )
    # response.sendTyping(session)
    # response.send(session,video)
    # img = response.attachement(
    #     type="image",
    #     url="https://ozz.ai/img/robot.jpg"
    # )
    # response.send(session, img)
    # file_att = response.attachement(
    #     type="file",
    #     url="http://www.pdf995.com/samples/pdf.pdf"
    # )
    # response.send(session,file_att)
    # audio = response.attachement(
    #     type="audio",
    #     url="http://www.hubharp.com/web_sound/BachGavotteShort.mp3"
    # )
    # response.send(session,audio)
    # quick_reply = response.quick_reply(
    #     text = "Pick a color",
    #     replies = [ 
    #                     response.replies(
    #                         type = "text",
    #                         title = "Yes",
    #                         payload = "yes" 
    #                     ),
    #                     response.replies(
    #                         type = "text",
    #                         title = "No",
    #                         payload = "no"
    #                     )
    #               ]
    # )
    # response.send(session,quick_reply)

def whatUp(session):
    response.send(session,"Nothing much...sup with you?")
    