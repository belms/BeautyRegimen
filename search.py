from scipy.stats.mstats import spearmanr
from whoosh import index, scoring
from whoosh.qparser import QueryParser


def search(query):
    my_index = index.open_dir("my_index")
    qp = QueryParser("content", schema=my_index.schema)
    result = {}
    q = qp.parse(query)
    with my_index.searcher(weighting=scoring.BM25F()) as s:
        results = s.search(q, terms=True, limit=20)
        for r in results:
            result[r.values()[0]] = round(r.score)
    return result


def write_results(search_query, file_destination, input_query):
    search_result_1 = {}
    search_result_2 = {}
    correlation = 0

    # If there are more than one search term in a query then separate them for individual search If they produce
    # uneven number of documents, remove documents with the lowest scores, in a rank with more documents
    # until both rankings are the same length
    if len(search_query) > 1:
        search_result_1 = search(search_query[0])
        search_result_2 = search(search_query[1])
        if len(search_result_1) > len(search_result_2):
            for i in range(len(search_result_1) - len(search_result_2)):
                search_result_1.popitem()
        else:
            for i in range(len(search_result_2) - len(search_result_1)):
                search_result_2.popitem()
        # check correlation between queries
        correlation = spearmanr(list(search_result_1.values()), list(search_result_2.values())).correlation
    else:
        search_result_1 = search(search_query[0])

    # greater correlation means that these two products are similar enough,
    # so combine the results and pick the most relevant products from the same pool
    if correlation > 0.8:
        final_list = dict(search_result_1)
        final_list.update(search_result_2)
        final_list_sorted = sorted(final_list, key=final_list.get, reverse=True)[:6]
        for k in final_list_sorted:
            file = open(file_destination + "/" + input_query + '.txt', "a")
            file.write(k + "\n\n")
    # If they aren't similar, pick the top products from each rank
    elif correlation == 0 and len(search_result_2) > 0:
        for k in list(search_result_1)[:3]:
            file = open(file_destination + "/" + input_query + '.txt', "a")
            file.write(k + "\n\n")
        for k in list(search_result_2)[:3]:
            file = open(file_destination + "/" + input_query + '.txt', "a")
            file.write(k + "\n\n")
    # If only one term is being searched, provide the user with the complete rank
    else:
        for k in search_result_1:
            file = open(file_destination + "/" + input_query + '.txt', "a")
            file.write(k + "\n\n")
