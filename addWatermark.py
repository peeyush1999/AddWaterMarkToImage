from PIL import Image
import shutil, os, glob
import xlrd
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True

def remove_transparency(im, bg_colour=(255, 255, 255)):

    
    if im.mode in ('RGBA', 'LA') or (im.mode == 'P' and 'transparency' in im.info):

        # Need to convert to RGBA if LA format due to a bug in PIL (http://stackoverflow.com/a/1963146)
        alpha = im.convert('RGBA').split()[-1]

        # Create a new background image of our matt color.
        # Must be RGBA because paste requires both images have the same format
        # (http://stackoverflow.com/a/8720632  and  http://stackoverflow.com/a/9459208)
        bg = Image.new("RGBA", im.size, bg_colour + (255,))
        bg.paste(im, mask=alpha)
        return bg

    else:
        return im
    
def create_watermark(image_path, final_image_path, watermark):
    main = Image.open(image_path)
    mark = Image.open(watermark)

    mask = mark.convert('L').point(lambda x: min(x, 25))
    mark.putalpha(mask)

    mark_width, mark_height = mark.size
    main_width, main_height = main.size
    aspect_ratio = mark_width / mark_height
    new_mark_width = main_width * 0.25
    mark.thumbnail((new_mark_width, new_mark_width / aspect_ratio), Image.ANTIALIAS)

    tmp_img = Image.new('RGB', main.size)

    for i in range(0, tmp_img.size[0], mark.size[0]):
        for j in range(0, tmp_img.size[1], mark.size[1]):
            main.paste(mark, (i, j), mark)
            main.thumbnail((8000, 8000), Image.ANTIALIAS)
            main = remove_transparency(main)
            try:
                main.save(final_image_path, quality=100)
            except:
                main = main.convert("RGB")
                main.save(final_image_path, quality=100)


'''if __name__ == '__main__':
    create_watermark('1696560552.jpg',
                     'Water1234.jpg',
                     'WaterMarkImage.png')
'''

def moveAllFilesinDir(srcDir):
    # Check if both the are directories
    #print(os.path.isdir(srcDir))
    count = 0
    if os.path.isdir(srcDir):
        # Iterate over all the files in source directory
        for filePath in glob.glob(srcDir + '\*'):
            
            print(filePath)
        # Move each file to destination Directory
            #shutil.move(filePath, dstDir);
            
            if(os.path.isdir(filePath)):
                for filePath1 in glob.glob(filePath + '\*'):
                    

                    Iname = filePath1.split('\\')
                    Iname = Iname[-1]
                    Iname = Iname.split('.')
                    ext = Iname[-1]
                    Iname = Iname[0]
                    print('Name Of Image :'+ Iname   + "     Name of Ext: " + ext)
                    filePath1 = filePath1.split(Iname+'.'+ext)

                    filePath1 = filePath1[0]
                    
                    dest = filePath1 +  Iname+'.'+ext
                    print(dest)
                    
                    create_watermark(dest,dest,'WaterMarkImage.png')
                    if count==0:
                        input("Check Every THing")
                    count +=1
            else:
                pass
            
                
                
    else:
        print("srcDir & dstDir should be Directories")

    print('completed')    
    print(count)


sourceDir = r'image_data'
moveAllFilesinDir(sourceDir)
