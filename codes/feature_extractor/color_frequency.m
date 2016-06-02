function fre=color_frequency(im)
[r,c]=size(im);
idensity=0:255;
[fre,~]=hist(im(:),idensity);
fre=fre/(r*c);
end