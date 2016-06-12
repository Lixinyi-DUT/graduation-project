path='F:\\data\\';
test_set=0;
acc=zeros(7,10);
th=0.05;

p=zeros(1338*5,7);
for i=1:10
    id=sprintf('%03d',i*5);
    s=load([path,id,'.mat']);
    test_set=s.train_set;
    label_t=sign(th-test_set(:,5));
    label_t=label_t-(label_t==0);
    trueclass=sum(label_t==-1);
    [p,~,~]=svmpredict(label_t,test_set(:,1:4),model1);
    acc(1,i)=sum(sign(label_t-p)==1)/sum(p==-1);
    [p,~,~]=svmpredict(label_t,test_set(:,1:4),model2);
    acc(2,i)=sum(sign(label_t-p)==1)/sum(p==-1);
    [p,~,~]=svmpredict(label_t,test_set(:,1:4),model5);
    acc(5,i)=sum(sign(label_t-p)==1)/sum(p==-1);
    [p,~,~]=svmpredict(label_t,test_set(:,1:4),model4);
    acc(4,i)=sum(sign(label_t-p)==1)/sum(p==-1);
    [p,~,~]=svmpredict(label_t,test_set(:,1:4),model6);
    acc(6,i)=sum(sign(label_t-p)==1)/sum(p==-1);
    [p,tmp,~]=svmpredict(label_t,test_set(:,1:4),model7);
   acc(7,i)=sum(sign(label_t-p)==1)/sum(p==-1);
    output=sprintf('t%d',i);
end