import os
from flask import render_template, Blueprint, request, flash, redirect, url_for, current_app
from flask_login import login_user, logout_user, login_required
from server import db, models, bcrypt
from server.demo.forms import Upload
import sys, random
from PIL import Image, ImageFilter, ImageDraw


basedir = os.path.abspath(os.path.dirname(__file__))
demo_blueprint = Blueprint('demo', __name__,)

def watermark(image):
    im = Image.open(image)
    im = im.convert("RGBA")
    watermark = Image.open(basedir+'/simpleG.png')

    widthIM, heightIM = im.size
    widthW, heightW = watermark.size

    print(widthIM, heightIM)

    if(heightIM>widthIM):
    	numY = 20
    	numX = ((20*int(widthIM)/int(heightIM)))
    	watermarkNewSize = int(heightIM/20)

    if (heightIM<=widthIM):
    	numX = 20
    	numY = (int(20*heightIM)/int(widthIM))
    	watermarkNewSize = int(widthIM/20)

    watermarkResize = watermark.resize((watermarkNewSize, watermarkNewSize))

    positionOffsetToIncrementY = heightIM/numY
    positinoOffsetToIncrementX = widthIM/numX

    transparent = Image.new('RGBA', (widthIM, heightIM), (0,0,0,0))

    transparent.paste(im, (0,0))
    for i in range (0, int(numX+2)):
    	for y in range(0, int(numY+2)):
    		watermark2 = watermark.rotate(random.randint(0,360))
    		transparent.paste(watermarkResize,
    			((int(positinoOffsetToIncrementX*i)+random.randint(0,0)),
    				(int(positionOffsetToIncrementY*y)+random.randint(0,0))), mask=watermarkResize)


    transparent.save(current_app.config.get('WATERMARK_BUCKET_PATH')+'/'+image.filename,'png', quality=95)



@demo_blueprint.route("/demo", methods=['GET', 'POST'])
def demo():
    form = Upload()
    images = os.listdir(current_app.config.get('WATERMARK_BUCKET_PATH'))
    if '.DS_Store' in images:
        images.remove('.DS_Store')
    print(images)
    if form.validate_on_submit():
        photo = request.files['crypto_painting']
        photo.save(current_app.config.get('IMAGE_BUCKET_PATH') + '/' +photo.filename)
        watermark(photo)
        return render_template('demo/demo.html', form=form, images=images)

    return render_template('demo/demo.html', form=form, images=images)
