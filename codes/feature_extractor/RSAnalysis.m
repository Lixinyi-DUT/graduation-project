function  [RSU_FM,RSU_M]=RSAnalysis(img,G_x_length,G_y_length)
[r,c]=size(img);
digit_img=double( img(:,:,1) );
img_M=digit_img;
img_FM=digit_img;
for  x= 1 : r
    for y= 1 :c
        if rem(digit_img(x,y), 2 )==0            
            img_M(x,y)=img_M(x,y) + 1;
            img_FM(x,y)=img_FM(x,y)-1;            
        else           
            img_M(x,y) =img_M(x,y) - 1;
            img_FM(x,y)=img_FM(x,y) + 1;
        end
    end    
end
 
RSU_FM=zeros(1,3);
RSU_M=zeros(1,3);

for x= 1 :G_x_length:r-G_x_length
    for y=1 :G_y_length:c-G_y_length
        f_G=f_smooth(digit_img,x,y,G_x_length,G_y_length);
        f_FMG=f_smooth(img_FM,x,y,G_x_length,G_y_length);
        f_MG=f_smooth(img_M,x,y,G_x_length,G_y_length); 
        RSU_FM=RSU_FM+[f_FMG>f_G,f_FMG<f_G,f_FMG==f_G];
        RSU_M=RSU_M+[f_MG>f_G,f_MG<f_G,f_MG==f_G];
    end    
end
end