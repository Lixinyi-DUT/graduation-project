path='F:\\graduation-project\\codes\\feature_extractor\\data\\';
acc=zeros(7,10);
th=0.1;
p=zeros(20*10,7);
for i=1:10
    id=sprintf('sp020sp010sp%03d',i*5);
    s=load([path,id,'.mat']);
    test_set=s.sptest_set;
    label_t=sign(th-test_set(:,5));
    label_t=label_t-(label_t==0);
    [p(:,1),tmp,~]=svmpredict(label_t,test_set(:,1:4),model1);
    acc(1,i)=tmp(1,1);
    [p(:,2),tmp,~]=svmpredict(label_t,test_set(:,1:4),model2);
    acc(2,i)=tmp(1,1);
   % [p(:,3),tmp,~]=svmpredict(label_t,test_set(:,1:4),model3);
   % acc(3,i)=tmp(1,1);
    [p(:,4),tmp,~]=svmpredict(label_t,test_set(:,1:4),model4);
    acc(4,i)=tmp(1,1);
    [p(:,5),tmp,~]=svmpredict(label_t,test_set(:,1:4),model5);
    acc(5,i)=tmp(1,1);
    [p(:,6),tmp,~]=svmpredict(label_t,test_set(:,1:4),model6);
    acc(6,i)=tmp(1,1);
    [p(:,7),tmp,~]=svmpredict(label_t,test_set(:,1:4),model7);
    acc(7,i)=tmp(1,1);
    for j=1:7
        p(:,j)=ones(20*10,1)-abs(p(:,j)-label_t);
    end
end;
test_set=0;
acc=zeros(7,10);
th=0.1;
p=zeros(20*10,7);
for i=1:10
    id=sprintf('sp020sp010sp%03d',i*5);
    s=load([path,id,'.mat']);
    test_set=s.sptest_set;
    label_t=sign(th-test_set(:,5));
    label_t=label_t-(label_t==0);
    [p(:,1),tmp,~]=svmpredict(label_t,test_set(:,1:4),model1);
    acc(1,i)=tmp(1,1);
    [p(:,2),tmp,~]=svmpredict(label_t,test_set(:,1:4),model2);
    acc(2,i)=tmp(1,1);
   % [p(:,3),tmp,~]=svmpredict(label_t,test_set(:,1:4),model3);
   % acc(3,i)=tmp(1,1);
    [p(:,4),tmp,~]=svmpredict(label_t,test_set(:,1:4),model4);
    acc(4,i)=tmp(1,1);
    [p(:,5),tmp,~]=svmpredict(label_t,test_set(:,1:4),model5);
    acc(5,i)=tmp(1,1);
    [p(:,6),tmp,~]=svmpredict(label_t,test_set(:,1:4),model6);
    acc(6,i)=tmp(1,1);
    [p(:,7),tmp,~]=svmpredict(label_t,test_set(:,1:4),model7);
    acc(7,i)=tmp(1,1);
    for j=1:7
        p(:,j)=ones(20*10,1)-abs(p(:,j)-label_t);
    end
end
acc(3,:)=[];
save