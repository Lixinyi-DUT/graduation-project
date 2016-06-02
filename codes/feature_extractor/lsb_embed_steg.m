function stego=lsb_embed_steg(cover,secret_text,x,y,block_width)
stego=cover;
block=cover(x:x-1+block_width,y:y-1+block_width);
block_byte=reshape(block,1,[]);
protext=dec2bin(length(secret_text),24)-'0';
x_pos=dec2bin(x,10)-'0';
y_pos=dec2bin(y,10)-'0';
stego(1,1:24)=bitand(stego(1,1:24),254)+uint8(protext);
stego(1,25:34)=bitand(stego(1,25:34),254)+uint8(x_pos);
stego(1,35:44)=bitand(stego(1,35:44),254)+uint8(y_pos);
secret_byte=uint8(reshape(dec2bin(secret_text,8),1,[]))-'0';
block_byte(1,1:length(secret_text)*8)=bitand(block_byte(1,1:length(secret_text)*8),254)+secret_byte;
stego(x:x-1+block_width,y:y-1+block_width)=reshape(block_byte,size(block));
end