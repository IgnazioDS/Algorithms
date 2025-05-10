from text_indexer import SuffixArray
def test_simple():
    sa=SuffixArray("banana")
    assert sa.find("ana")==[1,3]
    assert sa.find("nana")==[2]
    assert sa.find("xyz")==[]
