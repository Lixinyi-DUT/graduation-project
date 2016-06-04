cover=imread('F:\\ucid_gray\\00345.png');
RSU_FM=zeros(11,3);
RSU_M=zeros(11,3);
for i=0:10
    stego=lsb_embed_simple(cover,i*0.1);
    [RSU_FM(i+1,:),RSU_M(i+1,:)]=RSAnalysis(stego,5,5);
end
save('data/RSdata.mat','RSU_FM','RSU_M')
