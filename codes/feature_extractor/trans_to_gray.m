path='E:\\BaiduYunDownload\\ucid.v2\\ucid';
for n=1:1338
    imgname='E:\\BaiduYunDownload\\ucid.v2\\ucid';
    id=sprintf('%05d',n);
    raw_img=imread([p,id,'.tif']);
    trans=rgb2gray(raw_img);
    imwrite(trans,['F:\\ucid_gray\\',id,'.png']);
end