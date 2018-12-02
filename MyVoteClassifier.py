import numpy as np

class MyClassifier():
    def __init__(self,model):
        self.model=model
    def fit(self,**kwargs):
        print kwargs
        self.model.fit(**kwargs)
        return self.model
# 加载训练后的模型
class MyStacking():
    models = []
    results=[]
    votting="hard"
    def __init__(self,models):
        self.models=models
        if len(models)<1:
            raise RuntimeError('no model add .....')
    #预测，votting为hard或者soft，is_show_item_result为布尔值，是否输出每个模型的预测结果
    # 保存每个模型的结果
    def predict(self,test_data,votting,is_show_item_result=False):
        self.votting=votting
        for item in self.models:
            result = item.predict(test_data)
            if is_show_item_result:
                print result
            self.results.append(result)


    # 计算模型的个数，预测的样本个数
        models_len = len(self.results)
        single_model_labels_len = len(self.results[0])

    # 记录预测的最终结果
        soft_result=[]
        hard_result = []

    # soft stacking
        if self.votting=="soft":
            for i in range(single_model_labels_len):
                for j in range(models_len):
                    l=[]
                    l.append(self.results[j][i])
                    r = np.mean(l,axis=0)
                    index = r.tolist().index(max(r))
                    soft_result.append(index)
            return soft_result

   # hard stacking
        for i in range(single_model_labels_len):
            for j in range(models_len):
                l = []
                l.append(self.results[j][i])
                r = list(map(lambda x : x.tolist().index(max(x)),l))
                r = max(r,r.count)
                hard_result.append(r)
        return hard_result











