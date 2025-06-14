from mteb import AbsTaskClassification

class Vietnamese_Student_Sentiment(AbsTaskClassification):
    @property
    def description(self):
        return {
            'name': 'Vietnamese_Student_Sentiment',
            'hf_hub_name': 'another-symato/VMTEB-vietnamese_students_feedback_sentiment',
            'description': 'Sentiment Analysis of student reviews',
            'category': 's2s',
            'type': 'Classification',
            'eval_splits': ['validation', 'test'],
            'eval_langs': ['vie'],
            'main_score': 'accuracy',
            "n_experiments": 10,
            'samples_per_label': 32,
        }
    
class Vietnamese_Student_Topic(AbsTaskClassification):
    @property
    def description(self):
        return {
            'name': 'Vietnamese_Student_Topic',
            'hf_hub_name': 'another-symato/VMTEB-vietnamese_students_feedback_topic',
            'description': 'Sentiment Analysis of student reviews',
            'category': 's2s',
            'type': 'Classification',
            'eval_splits': ['validation', 'test'],
            'eval_langs': ['vie'],
            'main_score': 'accuracy',
            "n_experiments": 10,
            'samples_per_label': 32,
        }

class Vietnamese_Student_Sentiment_Wseg(AbsTaskClassification):
    @property
    def description(self):
        return {
            'name': 'Vietnamese_Student_Sentiment_Wseg',
            'hf_hub_name': 'another-symato/VMTEB-vietnamese_students_feedback_sentiment_word_segment',
            'description': 'Sentiment Analysis of student reviews',
            'category': 's2s',
            'type': 'Classification',
            'eval_splits': ['validation', 'test'],
            'eval_langs': ['vie'],
            'main_score': 'accuracy',
            "n_experiments": 10,
            'samples_per_label': 24,
        }   
     
class Vietnamese_Student_Topic_Wseg(AbsTaskClassification):
    @property
    def description(self):
        return {
            'name': 'Vietnamese_Student_Topic_Wseg',
            'hf_hub_name': 'another-symato/VMTEB-vietnamese_students_feedback_topic_word_segment',
            'description': 'Sentiment Analysis of student reviews',
            'category': 's2s',
            'type': 'Classification',
            'eval_splits': ['validation', 'test'],
            'eval_langs': ['vie'],
            'main_score': 'accuracy',
            "n_experiments": 10,
            'samples_per_label': 24,
        }

class VMTEB_ViOCD(AbsTaskClassification):
    @property
    def description(self):
        return {
            'name': 'VMTEB_ViOCD',
            'hf_hub_name': 'another-symato/VMTEB-ViOCD',
            'description': 'Sentiment Analysis of student reviews',
            'category': 's2s',
            'type': 'Classification',
            'eval_splits': ['dev', 'test'],
            'eval_langs': ['vie'],
            'main_score': 'accuracy',
            "n_experiments": 10,
            'samples_per_label': 32,
        }

class VMTEB_ViOCD_Wseg(AbsTaskClassification):
    @property
    def description(self):
        return {
            'name': 'VMTEB_ViOCD_Wseg',
            'hf_hub_name': 'another-symato/VMTEB-ViOCD_word_segment',
            'description': 'Sentiment Analysis of student reviews',
            'category': 's2s',
            'type': 'Classification',
            'eval_splits': ['dev', 'test'],
            'eval_langs': ['vie'],
            'main_score': 'accuracy',
            "n_experiments": 10,
            'samples_per_label': 32,
        }
