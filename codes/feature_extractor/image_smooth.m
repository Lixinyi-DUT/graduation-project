function smo=image_smooth(block)
[r,c]=size(block);
diff_x2=sum(sum(abs(block(1:end-1,:)-block(2:end,:))));
diff_x1=sum(sum(abs(block(:,1:end-1)-block(:,2:end))));
diff_x3=sum(sum(abs(block(1:end-1,1:end-1)-block(2:end,2:end))));
diff_x4=sum(sum(abs(block(2:end,1:end-1)-block(1:end-1,2:end))));
smo=(diff_x1+diff_x2+diff_x3+diff_x4)/(r*c);
end