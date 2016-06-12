cover=imread('F:\\ucid_gray\\00095.png');
x1=zeros(10,1);x2=x1;x3=x2;x4=x3;y1=x1;
p1=x1;p2=x1;
[width,height]=size(cover);
secret_length=floor((width*height*0.25)/8);
block_width=ceil(sqrt(secret_length*8));
secret_text=randi([0,255],[1,secret_length]);
for i=1:10
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
    p1(i,1)=x;
    p2(i,1)=y;
    y1(i,1)=RSAttack(stego);
end
loc_set=[p1,p2,x1,x2,x3,x4,y1];
[detection,tmp,~]=svmpredict(sign(-th-loc_set(:,7)),loc_set(:,3:6),model2);
save('F:\\graduation-project\\codes\\feature_extractor\\data\\pos.mat','loc_set','detection','block_width');