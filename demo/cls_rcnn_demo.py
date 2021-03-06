from smartnlp.classfication.dl.base_classifier import TextRCNNClassifier

if __name__ == '__main__':
    base_classifier = TextRCNNClassifier(model_path='./model/rcnn/',
                                         config_path='./model/base/config.pkl',
                                         train=True,
                                         vector_path='../tutorials/03.poem_generation/data/GoogleNews-vectors-negative300.bin.gz')
    out = base_classifier.predict(
        ['this is very good movie , i want to watch it again!', 'this is very bad movie , i hate it!'])
    out2 = base_classifier.predict('this is very good movie , i want to watch it again!')
    print(out)
    print(out2)
