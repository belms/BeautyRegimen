# BeautyRegimen
Recommendation system of beauty products, using whoosh search engine and python.  
This project demonstrates information retrieval and web scraping.


# Technologies Used
 - Python
 - Whoosh search engine
 - Selenium
 
 Although here there is no code tied to Selenium library, I have used it to scrape several beauty shop pages to scrape around 70 products that are used. 
 It is very specific to a concrete web page, so I saw no point of posting that code here. 
 How selenium works, you can find -> [here](https://selenium-python.readthedocs.io/)
 After I have collected enough products to work with, I have used -> [Woosh](https://whoosh.readthedocs.io/en/latest/intro.html) search engine library
 to index these text files, for a collection. 
 Search engine, with its algorithms, is used to search through my product collection and find products the users asked for. 
 
 # How it works
 The user will be prompted to type their skin concernes. For example: dry skin, anti age, vitamin c serum, cream, etc.
 The application will search for the products addresing these skin concerns from the product collection. 
 If the user asks for products addressing more than one skin concern, application breaks it into two separate queries.
 I have decided to do it with two separate queries, because woosh search engine doesn't work well with queries containing more than two words.
 With this approach, I have better results for each user concern. 
 
 I have used BM25 algorithm for my searches, and here you can find more about it -> [here](http://ethen8181.github.io/machine-learning/search/bm25_intro.html)
 
 In the case, that the user wants to address more skin concernes, knowing the subject, I realized that you can actually use the same product for both of those needs. To determine whether two rank results provided the list of products that can be for each skin concerne, I have used Spearman rank correlation. 
 
 In the code there is a if block of code, checking whether the correlation is greater than 80%. If it is, combine the results and give the user final list of products. If not, pick the best ranking products from both rank result lists. 
