function stego=lsb_embed_simple(cover,em)
stego=cover;
if em>0
[h,w]=size(cover);
secret_length=floor((w*h*em)/8);
secret_text=randi([0,255],[1,secret_length]);
cover_byte=reshape(cover,1,[]);
secret_byte=uint8(reshape(dec2bin(secret_text,8),1,[]))-'0';
cover_byte(1,1:length(secret_text)*8)=bitand(cover_byte(1,1:length(secret_text)*8),254)+secret_byte;
stego=reshape(cover_byte,size(cover));
end
end