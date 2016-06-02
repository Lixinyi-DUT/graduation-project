function dif=f_smooth(im,x,y,G_x_length,G_y_length)
dif_x=sum(abs(im(x:x-1+G_x_length,y:y-2+G_y_length)-im(x:x-1+G_x_length,y+1:y-1+G_y_length)));
dif_y=sum(abs(im(x:x-2+G_x_length,y:y-1+G_y_length)-im(x+1:x-1+G_x_length,y+1:y+G_y_length)));
dif=sum(dif_x)+sum(dif_y);
end