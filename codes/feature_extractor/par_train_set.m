for em_rate=0.05:0.05:7
pic=1338;loc=10;
x1=zeros(pic*loc,1);x2=x1;x3=x2;x4=x3;y1=x1;
scale=sprintf('-%04d-%02d-%03d',[pic,loc,em_rate*100]);
path='F:\\ucid_gray\\';
id=sprintf('%05d',1);
parfor i=1:pic*loc
    n=floor((i-1)/loc)+1;
    id=sprintf('%05d',n);
    cover=imread([path,id,'.png']);
    [width,height]=size(cover);
    secret_length=floor((width*height*em_rate)/8)
    secret_text=randi([128,255],[1,secret_length])
    block_width=ceil(sqrt(secret_length*8));
    x=randi([1,width-block_width],1);
    y=randi([1,height-block_width],1);
    if x<24+10+10 && y == 1
            y=2;
    end
    block=cover(x:x-1+block_width,y:y-1+block_width);
    digit_block=double(block);
    stego=lsb_embed_steg(cover,secret_text,x,y,block_width);
    x1(i,1)=var(digit_block(:));
    x2(i,1)=sc_match(block,secret_text);
    x3(i,1)=local_diff(block,cover);
    x4(i,1)=image_smooth(block);
    y1(i,1)=RSAttack(stego);
    %train_set(i,1:5)=[var(digit_block(:)),sc_match(block,secret_text),local_diff(block,cover),image_smooth(block),RSAttack(stego)];
end
train_set=[x1,x2,x3,x4,y1];
time=datestr(now,30);
save(['data/',time,scale,'.mat'],'train_set');
end
