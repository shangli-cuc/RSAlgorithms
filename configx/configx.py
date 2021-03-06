# encoding:utf-8
class ConfigX(object):
    """
    docstring for ConfigX

    configurate the global parameters and hyper parameters

    """

    def __init__(self, dataset_name=None):
        super(ConfigX, self).__init__()

        # Dataset Parameters
        if dataset_name: # 从类初始化读取, 用于 prepare 数据预处理
            self.dataset_name = dataset_name
        else:
            self.dataset_name = "ft"  # short name of datasets ["ft":"filmtrust","db":"douban","ca":"ciao"]
            self.dataset_name = "dbm"  # HIN douban movie 裁减后 的数据集， 需提前运行 prepare/ 下的 notebook 生成
            # self.dataset_name = "dbd"  # HIN douban movie 裁减后 更小的 debug 数据集, 便于快速调试程序, 需提前运行 prepare/ 下的 notebook 生成
            # self.dataset_name = "dbb"  # HIN douban book 数据集 
            # self.dataset_name = "lastfm"  # HIN lastfm 数据集
            # self.dataset_name = "ml" #  HIN movielens  数据集

        self.k_fold_num = 5  # the num of cross validation
        self.rating_path = "../data/%s_ratings.txt" % self.dataset_name  # the raw ratings data file
        self.rating_cv_path = "../data/cv/"  # the cross validation file of ratings data
        self.trust_path = '../data/%s_trust.txt' % self.dataset_name  # the raw trust data file
        self.meta_path = '../data/%s_meta.txt' % self.dataset_name  # the raw metadata file
        self.sep = ' '  # the separator of rating and trust data in triple tuple
        self.random_state = 123  # the seed of random number # 固定随机数种子
        self.size = 0.8  # the ratio of train set
        self.min_val = 0.5  # the minimum rating value
        self.max_val = 4.0  # the maximum rating value

        # Model HyperParameter
        self.coldUserRating = 5  # the number of ratings a cold start user rated on items
        self.factor = 10  # the size of latent dimension for user and item.
        self.threshold = 10 # the threshold value of model training 
        self.lr = 0.01  # the learning rate
        self.maxIter = 50  # the maximum number of iterations
        self.lambdaP = 0.0001  # the parameter of user regularizer
        self.lambdaQ = 0.0001  # the parameter of item regularizer
        self.gamma = 0  # momentum coefficient
        self.isEarlyStopping = False  # early stopping flag

        # Output Parameters
        self.result_path = "../results/"  # the directory of results
        self.model_path = "model/"  # the directory of well-trained variables
        self.result_log_path = "log/"  # the directory of logs when training models
