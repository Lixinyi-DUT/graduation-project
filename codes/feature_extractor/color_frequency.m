function fre=color_frequency(im)
fre=zeros(1,256);
[r,c]=size(im);
   for i =0:255
       fre(1,i+1)=sum(sum(im==i));
   end
fre=fre/(r*c);
end