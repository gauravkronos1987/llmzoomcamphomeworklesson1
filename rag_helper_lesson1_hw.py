from rag_helper import RAGBase

class RAGWithLessonSearch(RAGBase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def search(self, query, num_results=5):
        boost_dict = {"question": 1.0, "answer": 2.0, "section": 0.1}
        filter_dict = {"course": self.course}

        return self.index.search(
            query,
            num_results=num_results,
            boost_dict=boost_dict,
            filter_dict=filter_dict
        )