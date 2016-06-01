function similarity=sc_match(block,secret)
secret_bit=uint8(reshape(dec2bin(secret,8),1,[]))-'0';
lsb=reshape(bitand(block,1),1,[]);
lsb_embed=lsb(1,1:length(secret_bit));
difference=lsb_embed-secret_bit;
similarity=sum(difference==0)/length(secret_bit);
end