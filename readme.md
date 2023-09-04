# **STILL IN PRODUCTION**

*for manual work

# Usage:
Create a python or preferably a conda environment with the version set to `3.10.11`. Once done activate it and execute `pip install -r requirements.txt`
1. clone repository with `git clone https://github.com/08Aristodemus24/LaRJ-Corpus.git`
2. navigate to directory with `readme.md` and `requirements.txt` file
3. run command; `conda create -n <name of env e.g. larj-corpus> python=3.10.11`. Note that 3.10.11 must be the python version otherwise packages to be installed would not be compatible with a different python version
4. once environment is created activate it by running command `conda activate`
5. then run `conda activate larj-corpus`
6. check if pip is installed by running `conda list -e` and checking list
7. if it is there then move to step 8, if not then install `pip` by typing `conda install pip`
8. if `pip` exists or install is done run `pip install -r requirements.txt` in the directory you are currently in

# Extraction tasks:
## Labor Corpus Juris
### Web Scraping
- *identify all leaf links (links that lead directly to a page)
e.g. sublink 1 leads to page <X1> with content <Y1>, sublink 2 leads to page <X2> with sublink 1, 2, 3, 4, 5 and when each are visited manually leads to a page with content. Therefore leaf nodes are therefore
- *identify element holding most of the important leaf links or identify links with common xpath/css path
- *get this elements xpath/css path by inspecting element
- extract element using xpath/css path, driver.find_element(By.CSS_SELECTOR, link_selector)
- use the element to find all link elements content.find_elements(By.TAG_NAME, "a")
- extract links href attribute using link.get_attribute('href')
- extract links text attribute using link.text
- arrange all extracted link hrefs and link text in dataframe
- save dataframe

- *extract all link text that have commonality
- *paste and enclose in triple quotes """ """
- *by using ctrl-D delete all tabs and whitespaces in order to separate each link text

- *open a leaf link of this dataframe
- *identify element holding most of the content
- *get this elements xpath/css path by inspecting element
- *assume that this xpath/css path of this pages element containing the content is the same for all pages
- iteratively open all link hrefs in dataframe
- iteratively feed xpath/css path to a function to extract the element, driver.find_element(By.CSS_SELECTOR, text_content_selector)
- iteratively use the element extracted to extract all text from it, page_text_content.append(text_content.text)
- arrange all extracted page headers and page contents in a dataframe
- save dataframe

- if a page's content has no common xpath/css path with other pages get the contents full xpaht/css path 
- *extract content manually using library methods/functions e.g. get_content("<xpath string>")
- *manually append to dataframe

- open the data newly saved dataframe
- extract the page_contents column of hte dataframe and write to a text file
- save to its respective category e.g. if its text about "batas pambansa..." then save under major_philippine_labor_law_resources folder
- since some texts will be manually compressed into one line e.g. 

LABOR CIRCULAR ON-LINE No. 61 Series of 1998 TOPIC At a Glance PETITIONS FOR CERTIORARI UNDER RULE 65 OF THE RULES OF COURT FROM DECISIONS OF THE NLRC NOW TO BE INITIALLY FILED WITH THE COURT OF APPEALS AND NO LONGER DIRECTLY WITH THE SUPREME COURT [en banc] [New Interpretation of "Appeals" from NLRC Decisions] Case Title: ST. MARTIN FUNERAL HOME VS. NATIONAL LABOR RELATIONS COMMISSION, ET AL. [G. R. No. 130866, September 16, 1998] [en banc] FACTS & RULING OF THE COURT: The Supreme Court [en banc] did not rule on the factual issues of the case but instead re-examined, inter alia, Section 9 of Batas Pambansa Bilang 129, as amended by Republic Act No. 7902 [effective March 18, 1995] on the issue of where to elevate on appeal the decisions of the National Labor Relations Commission [NLRC]. The High Court remanded the case to the Court of Appeals consistent with the new ruling enunciated therein that the "appeals" contemplated under the law from the decisions of the National Labor Relations Commission to the Supreme Court should be interpreted to mean "petitions for certiorari under Rule 65" and consequently, should no longer be brought directly to the Supreme Court but initially to the Court of Appeals. Before this new en banc ruling, the Supreme Court has consistently held that decisions of the NLRC may be elevated directly to the Supreme Court only by way of a special civil action for certiorari under Rule 65. There was no ruling allowing resort to the Court of Appeals. In support of this new view, the Supreme Court ratiocinated,  insofar as pertinent, as follows: "While we do not wish to intrude into the Congressional sphere on the matter of the wisdom of a law, on this score we add the further observations that there is a growing number of labor cases being elevated to this Court which, not being a trier of fact, has at times been constrained to remand the case to the NLRC for resolution of unclear or ambiguous factual findings; that the Court of Appeals is procedurally equipped for that purpose, aside from the increased number of its competent divisions; and that there is undeniably an imperative need for expeditious action on labor cases as a major aspect of constitutional protection to labor. "Therefore, all references in the amended Section 9 of B. P. No. 129 to supposed appeals from the NLRC to the Supreme Court are interpreted and hereby declared to mean and refer to petitions for certiorari under Rule 65. Consequently, all such petitions should henceforth be initially filed in the Court of Appeals in strict observance of the doctrine on the hierarchy of courts as the appropriate forum for the relief desired. xxx"

we decided to manually divide the content appropriately into new lines...

LABOR CIRCULAR ON-LINE No. 61 Series of 1998 TOPIC At a Glance PETITIONS FOR CERTIORARI UNDER RULE 65 OF THE RULES OF COURT
FROM DECISIONS OF THE NLRC NOW TO BE INITIALLY FILED WITH THE COURT OF APPEALS AND NO LONGER DIRECTLY WITH THE SUPREME COURT
[en banc] [New Interpretation of "Appeals" from NLRC Decisions]
Case Title: ST. MARTIN FUNERAL HOME VS. NATIONAL LABOR RELATIONS COMMISSION, ET AL.
[G. R. No. 130866, September 16, 1998] [en banc]
FACTS & RULING OF THE COURT: The Supreme Court [en banc] did not rule on the factual issues of the case but instead re-examined, inter alia, Section 9 of Batas Pambansa Bilang 129, as amended by Republic Act No. 7902 [effective March 18, 1995] on the issue of where to elevate on appeal the decisions of the National Labor Relations Commission [NLRC].
The High Court remanded the case to the Court of Appeals consistent with the new ruling enunciated therein that the "appeals" contemplated under the law from the decisions of the National Labor Relations Commission to the Supreme Court should be interpreted to mean "petitions for certiorari under Rule 65" and consequently, should no longer be brought directly to the Supreme Court but initially to the Court of Appeals.
Before this new en banc ruling, the Supreme Court has consistently held that decisions of the NLRC may be elevated directly to the Supreme Court only by way of a special civil action for certiorari under Rule 65. There was no ruling allowing resort to the Court of Appeals.
In support of this new view, the Supreme Court ratiocinated, insofar as pertinent, as follows: "While we do not wish to intrude into the Congressional sphere on the matter of the wisdom of a law, on this score we add the further observations that there is a growing number of labor cases being elevated to this Court which, not being a trier of fact, has at times been constrained to remand the case to the NLRC for resolution of unclear or ambiguous factual findings; that the Court of Appeals is procedurally equipped for that purpose, aside from the increased number of its competent divisions; and that there is undeniably an imperative need for expeditious action on labor cases as a major aspect of constitutional protection to labor.
"Therefore, all references in the amended Section 9 of B. P. No. 129 to supposed appeals from the NLRC to the Supreme Court are interpreted and hereby declared to mean and refer to petitions for certiorari under Rule 65. Consequently, all such petitions should henceforth be initially filed in the Court of Appeals in strict observance of the doctrine on the hierarchy of courts as the appropriate forum for the relief desired.
xxx"

### Annotating
Notes:
- Ask legal advisor what entity types occur most usually in text pertaining to our legal code:
- probable entities of corpus juris to identify: 

CITATION:
- 'motion for consideration'
- 'motion to extend my time to answer'
- 'people of the philippines vs ...'
- 'palmdale vs ...'

AMOUNT
COMPANY
CONSTRAINT
COPYRIGHT
COURT
DATE
DEFINITION
DISTANCE
DURATION
GEOENTITY
PERCENT, 

REGULATION:
- 'implementing rules and regulations'
- '

TRADEMARK

JUDGEMENT:
- whole document
- 'granted'
- 'denied'
- 'convicted'
- 'acquited'

DECISION:

GAZETTE:
- 'official gazette of the republic of the phil.'
- 'official journal of the republic of the phil.'
- newspaper
- journal

PROCEEDINGS:
- 'legal proceedings'
- 'hearing...'
- 'regional trial court'
- 'metropolitan trial court'
- 'administrative

ARTICLE:
SECTION:

CLAUSE
- 'republic act'
- group fo words
- phrase

PARAGRAPH:

PROSECUTOR:

APPEAL:

DEFENDANT
APPELANT:
- 'petitioner'
- '<name of person>'
- '<name of organization>

PLAINTIFF
- <name of person>
- people of the philippines

INVOLVED ENTITY

ADVOCATE

LEARNED COUNSEL

ROLE
JUDGE
OFFENCE
ACCUSATION
OBJECTION
JURISDICTION
PENALTY
COMPENSATION
EVIDENCE
EVIDENCE DESCRIPTION
ACT
CIRCULAR
SERIES
CASE
GENERAL REGISTRY NUMBER
PETITION
RULE
ORGANIZATION

- ask advisor what entity types usually occur in the legal code
- ask advisor what entity types to retain, or remove, or add

- ask advisor to identify probable entities of each entitiy type using an example document as guide e.g.
1. "ON-LINE No. 61 Series of 1998 TOPIC ~ Circular
2. PETITIONS FOR CERTIORARI UNDER RULE 65 ~ Petition
3. RULES OF COURT FROM DECISIONS OF THE NLRC NOW TO BE INITIALLY FILED WITH THE COURT OF APPEALS AND NO LONGER DIRECTLY WITH THE SUPREME COURT" ~ Rule
4.  The Supreme Court ~ Court
5.  Section 9 ~ Section
6.  Batas Pambansa Bilang 129 ~ Act
7.  Republic Act No. 7902 ~ Act
8.  March 18, 1995 ~ Date

- do this for each entity type and ask advisor to label probable entities of the document under said each entity type
1. Act: Batas Pambansa Bilang 129, Republic Act No. 7902, ...
2. Date: March 18, 1995, December 16, 1975, December 31, 1975, ...
3. disseminate information to group regarding what entities to look for in each document given examples under each entity type

**Side notes:**
* Petitioner: Another word for plaintiff, the person starting the lawsuit. Plaintiff: The person who sues or starts a civil case, also called the petitioner or the complainant.



## Labor Related Jurisprudence
* <s> finish identifying 1st batch of 1901-1920, 1921-1940, 1941-1960, 1961-1980, 1981-1995, 1996 and 1997 jurisprudence
* identify 2nd batch of 1998, 1999, 2000, 2001, 2002, 2003, and 2004 jurisprudence
* identify 3rd batch of 2005, 2006, 2007, 2008, 2009, 2010, and 2011 jurisprudence
* identify 4th batch of 2012, 2013, 2014, 2015, 2016, 2017, and 2018 jurisprudence
* identify last batch of 2019, 2020, and 2021 jurisprudence </s> CUT SHORT BECAUSE OF RATE LIMIT

inner right + inner left is the calculation
* indeces covered in 1901-1920: 0-573 (574), 0-276/574-850 (277) 
* indeces covered in 1921-1940: 0-579 (580), 0-275/580-855 (276)
* indeces covered in 1941-1960: 0-565 (566), 0-272/566-838 (273) 
* indeces covered in 1961-1980: 0-558 (559), 0-266/559-825 (267)
* indeces covered in 1981-1995: 0-685 (686), 0-345/686-1031 (346)
* indeces covered in 1996: 0-541 (542), 0-239/542-781 (240)
* indeces covered in 1997: 0-546 (547), 0-280/547-827 (281)
* indeces covered in 1998: 0-12 (13),
* indeces covered in 1999: 0-12 (13),
* indeces covered in 2000: 0-482 (483),
* indeces covered in 2001: done
* indeces covered in 2002: done
* indeces covered in 2003: done
* indeces covered in 2004: done
* indeces covered in 2005: done
* indeces covered in 2006: done
* indeces covered in 2007: done
* indeces covered in 2008: done 
* indeces covered in 2009: done
* indeces covered in 2010: done
* indeces covered in 2011: done
* indeces covered in 2012: done
* indeces covered in 2013: done
* indeces covered in 2014: done
* indeces covered in 2015: 0-24 (25), 0-963/25-988 (964) done
* indeces covered in 2016: 0-27 (28), 0-1060/28-1088 (1061) done
* indeces covered in 2017: 0-24 (25), 0-975/25-1000 (976) done
* indeces covered in 2018: done
* indeces covered in 2019: done
* indeces covered in 2020: done
* indeces covered in 2021: done

**Articles:**
1. accessing gpt-4 API
https://medium.com/codingthesmartway-com-blog/unlocking-the-power-of-gpt-4-api-a-beginners-guide-for-developers-a4baef2b5a81

2. using langchain to in the future potentially use the gathered labor related jurisprudence documents in entity and relationship extraction:
* https://medium.com/databutton/getting-started-with-langchain-a-powerful-tool-for-working-with-large-language-models-286419ba0842?source=list-11be0107d282--------3-------4f7d69921300---------------------
* https://towardsdatascience.com/ai-driven-insights-for-product-managers-vol-1-leveraging-langchain-and-pinecone-with-gpt-4-7755485019f9
* https://medium.com/@meta_heuristic/how-to-use-private-llm-gpt4all-with-langchain-9f890e6960f3
* https://medium.com/@vikastiwari708409/how-to-use-gpt4all-llms-with-langchain-to-work-with-pdf-files-f0f0becadcb6
* https://blog.futuresmart.ai/building-a-document-based-question-answering-system-with-langchain-pinecone-and-llms-like-gpt-4-and-chatgpt

**Side notes:**
1. all `juris_<year>parser.ipynb` files from 2021 down to 2001 have all completed parsing the jurisprudence documents in their year
2. however `juris_<year>parser.ipynb` parsers from 2021 down to 1901 all access the OPEN_AI_API_KEY via the original local machines system environment OPEN_AI_API_KEY variable, recent changes have moved the local machines system environment OPEN_AI_API_KEY value to the .env file which is ignored by .gitignore to prevent being pushed to remote repository and being exposed publicly



# Transformation Tasks:
## Labor Corpus Juris
- <s>remove all consecutive \n and replace with whitespace, re.sub(r"[\n\s]{2,10}", ' ', text_content)</s>
- <s>remove unnecessary phrases re.sub((<some unnecessary phrase 1>|<some unnecessary phrase 2>), '', text_content)</s>
- <s>match all expressions with values 0 to 9 and with at least 2 but not more than 3 digits re.search("(^C|^P)([0-9]{2,3})", content).group()</s>
- <s>remove leading and trailing whitespaces and newlines text_content.strip(), text_content.strip('\n')</s>
- <s>do this in each labor category: proposed international labor conventions, ratified international labor conventions, rules on contracting arrangement, significant dole department orders, NLRC, mahor philippine labor law resources, other labor law resources, rules of the labor code, and, thirteenth month pay law</s>
- <s>convert all dataframe objects of each labor legal code category to .txt file for annotation</s>
- in each .txt file manually separate the lines that are headers nad the rules

"LABOR CIRCULAR ON-LINE No. 61 Series of 1998 TOPIC At a Glance PETITIONS FOR CERTIORARI UNDER RULE 65 OF THE RULES OF COURT FROM DECISIONS OF THE NLRC NOW TO BE INITIALLY FILED WITH THE COURT OF APPEALS AND NO LONGER DIRECTLY WITH THE SUPREME COURT [en banc] [New Interpretation of ""Appeals"" from NLRC Decisions] Line 1
Case Title: ST. MARTIN FUNERAL HOME VS. NATIONAL LABOR RELATIONS COMMISSION, ET AL. [G. R. No. 130866, September 16, 1998] [en banc] Line 2
FACTS & RULING OF THE COURT: The Supreme Court ... appropriate forum for the relief desired. xxx""" Line 3

indeces covered:
Major philippine labor laws: Done
NLRC:
other labor law resources
proposed international labor conventions
ratified international labor conventions
rules of the labor code
rules on contracting arrangement
significant DOLE dept orders
13th month pay law

- upload or indicate all possible entities in the web app annotator. Expertise and advise of legal practitioner on what possible entities are would be better
- create system architecture for dealing with the raw text content in .txt files, 
- Even if we are to annotate the corpus juris manually and all of it, am option could be to split the data and train a custom NER model with this data in order to identify the entities in the other Labor Law Legal Codes
- once identified all entities using NER or by manually doing so create the knowledge graph automatically if not manually

## Labor Related Jurisprudence
- <s> act as if all answers are collected, by combining all .csv files into a single dataframe for cleaning </s>
- <s> answer__df.csv will be comprised of columsn file_path and answer </s>
- <s> apply capitalization, removal of punctuation, to whole answer column </s>
- <s> check if substring NOT occurs in answer column </s>
- <s> match either the phrases NOT LABOR RELATED or LABOR RELATED and return to the whole answer column </s>
- <s> the answer column will be comprise of inconsistent casing of values "labor related" and "not labor related", e.g. "Labor related.", "labor related", "not labor related.", "Not labor related", "the case is not labor related", "the case is labor related", etc.</s>
- <s> the answer column will also comprise of error messages TIMEOUT_ERROR, RATE_LIMIT_ERROR, TIME_LIMIT_REACHED, INVALID_REQUEST_ERROR, API_CONNECTION_ERROR as values from the api calls that resulted in errors keep these values </s>
- <s> merge the similar incosist4encies into just NOT LABOR RELATED, and LABOR RELATED </s>
- <s> merge answers__df with juris__df.csv where the the file_path column and file_path column in both tables is equal </s>
- <s> merge resulting df with juris.csv where the file_url column and identifier column is equal </s>



- synthesize the interaction of users between items where instead of explicit interaction such us rating of user for item we use the nubmer of clicks
type of interactions:
clicked 1
stayed for more than 1 minute 2
commented 3
liked 4
shared 5
however we may not be able to finish a web architecture that allows users to share posts etc.
- another option for the possible dataset to synthesize is to use instead explicit ratings and each rating will have a scoring system of 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, and 5
1st type of description of ratings
0.5 - unrelated to your case
1.0 - unrelated yet helpful to your case
1.5 - unrelated yet helpful to your case
2.0 - 

2nd type of description of ratings
1 - unrelated to your case
2 - unrelated yet helpful to your case
3 - somewhat helpful to your case
4 - mostly helpful to your case
5 - used as main references to your case



# Loading Tasks:
## Labor Corpus Juris
1. Once annotation is done upload data to database by proxy via .sql script

## Labor Related Jurisprudence
1. upload final__df.csv to database by proxy via .sql script
2. upload synthetically created user-item interaction from final__df.csv by proxy via .sql script
3. to import the juris_meta.csv file note that the sql scripts must be run in this sequential order should it be pulled from github: 
a. \ir ./create_db.sql
b. \ir ./create_tables.sql
c. \ir ./insert_data.sql
4. to delete the entire created database and its tables by the preceding commands above that created the database and tables in the first place sql scripts must be run in this sequential order:
a. \ir ./delete_tables.sql
b. \ir ./delete_db.sql



# Exploratory Data Analysis:
## Labor Related Jurisprudence
**Prerequisites to do:**
1. see how the knowledge graph of Hongwei, Wang is structured, see if items are contained in knowledge graph, if users are also contained in knowledge graph and why
a. run MKR and KGCN repositories code to get `kg_final.txt` and `ratings_final.txt` files. When the code was run to preprocess these aforementioned file output messages were the following:
```
reading item index to entity id file: ../data/movie/item_index2entity_id.txt ...
reading rating file ...
converting rating file ...
number of users: 6036
number of items: 2347
converting kg.txt file ...
number of entities (containing items): 6729
number of relations: 7
done
```

b. understand the `kg.txt` and `ratings.dat` files in order to model labor related jurisprudence user-item dataset and the knowledge graph that will be integrated to it
c. do data exploration and experimentation on these files by finding out each unique values of each column of the `kg.txt` and `ratings.dat` files
d. if kg.txt file in MKR contains 6729 entities containing items that are also in the item column in the user-item rating dataset, question now is are these 6729 items unique, and in my exploratory data analysis of the `kg.txt` and `ratings.dat` file why does some user id's still occur in the knowledge graph?

2. see functions on how knowledge graph and user-item rating data is preprocessed in code Hongwei, Wang's code in their in KGCN or MKR paper
a. understand how `read_item_index_to_entity_id_file()` works
b. understand how `convert_rating()` works
c. understand how `convert_kg()` works

3. because Hongwei, Wang's KGCN and MKR used a non-eager tensorflow implementation of both these models we must refer to the Recommender-System repository which contains eager tensorflow implementation of both these models

**To do:**
1. <s>analyze MKR and DFM-GCN ratings.dat by seeing the unique values of userID, itemID, and rating</s>
2. <s>analyze again if the the itemID's ever occur in either the head and tail columns of the knowledge graph</s>
3. an idea I have is that the data we have about the cases citing case laws could be used as a knowledge graph (requires )
4. match all "g.r. no." expressions or any expression like it such as 
* i.p.i. no.
* g.r. no. 46802-46812
* g.r. no. 42590, 42591
* adm. case no. 879
* g.r. no. 45274 and 45275
* g.r. no. 43522, 43523, 43751-43753
* per. rec. no. 714-a
* g.r. no. l-5984 and l-5985
* g.r. no. l-11319-20; l-13504; l-13507-8
* a.c. no. 9906
* a.m. no. p-14-3233 [formerly oca ipi no. 12-37...
* a.c. no. 8608 [formerly cbd case no. 11-2907]

**Questions:**
a. what exactly are those head entities?
b. what exactly are those tail entities?
c. are the head entities items that also co-occur in the user-item rating matrix
d. are the tail entities items that also co-occur in the user-item rating matrix

**Insights:**
some insights gain on the movie ratings dataset and the knowledge graph used by the MKR model we're the following:
1. In dataset used by MKR, movie ratings dataset had a total of 6040 unique users: 
2. In dataset used by MKR, movie ratings dataset had a total of 3706 unique items: 
3. In dataset used by MKR, movie ratings dataset had a total of 1,000,209 rows
4. In knowledge graph used by MKR, kg had a total of 2445 unique head nodes/vertices/entities
5. In knowledge graph used by MKR, kg had a total of 4563 unique tail nodes/vertices/entities
6. In knowledge graph used by MKR, kg had a total of 7 unique relations/edges

**Conclusions:**
1. since we have now about almost 4000 unique items which is greater than this datasets number of unique items, this may be sufficient enough to generate enough recommendations to users
2. about 6000 to 7000 users will be enough to power our recommender system
3. we will have to synthesize the ratings either by: 1. creating these 7000 legal practitioners google accounts 
4. since recommendation systems are barpartite graphs, having 4000 items and 7000 users will at the maximum amount to 28,000,000 million ratings since 4000 times 7000 is this number, should each user rate all 4000 items, and even then if each user does not decide to rate 4000 items, the total ratings done will be still in the range of 1 million to 10 million, as an educated estimate, roughly speaking

**Articles:**
* wang, h. details that https://github.com/hwwang55/KGCN/issues/5


**Side Notes:**
* The MKR paper uses I hypothesize a simple translational model to encode the knowledge graph
* The KGCN paper uses a graph convolutional network to encode the knowledge graph
* **User**: Hi, in your paper, you mention that you sample a fixed size set of neighbors for each entity. How do you choose neighbors for each entity? Random or in other ways? **Wang**: The entities are randomly sampled.
* **Wang**: you need to find a KG that matches the items in your dataset, and then do the linking between entities and items. **User**: What if I want to create a kg myself? Does your code expect to have each item exist in the kg.txt? **Wang**: Do you have the information to construct a KG for items? KG contains factual knowledge so it cannot be "created" but only "extracted" from available source of information. For example, you have the attributes of items, and these attributes can be connected to each other. Or, you have some natural texts describing these items, so you can use information extraction (IE) tools to extract a KG for these items. **User**: Yes, I do have info like article, specialty, lead-concept etc. **Wang**: You need to extract information from articles, and see if the specialty and lead concept information you mentioned can form a graph
* **User**: The first column is the id of the item, and the second column is the id of the movie in the knowledge graph. **User**: Is it just the movie id? Don’t you have the ID of the director or actor?
* **User**: Hello Professor Wang, I would like to ask why the second column of kg_rehashed.txt has three combinations. For example, what does 2474 film.writer.film 2475 mean? **Wang**: Hello, the first film indicates that the domain of this triple is film, the second writer and the third film indicate that the head and tail are writer and film respectively. Thanks!
* **User**: Hello Professor Wang, may I ask why some relationships in kg_rehashed.txt are bidirectional, such as <img alt="relations"/>. **User**: In the picture, there is no bidirectional relationship between coutry and language? Will it have a big impact if my data is all one-way relationships? **Wang**: Hi, these relationships are not bidirectional, can you describe your problem in detail? **User**: Hello Professor Wang, my use of the word "bidirectional" may not be appropriate. In fact, what I want to say is two "directionally symmetrical" relationships in opposite directions rather than a "bidirectional" relationship. As you mentioned: <img/>. **User**: I found that there are 4 pairs of relationships (relationships 1-8 in the picture above) with "symmetrical" head and tail nodes (such as film.writer.film and film.film.writer). Relationships 9-11 have no corresponding "symmetrical" ones. "opposite direction" relationship.
Question 1. Why set up the relationship like this? Why is there no corresponding "symmetrical" "reverse" relationship in relation 9-11?
Question 2. I used my own data to reproduce the experiment. There are 6 types of relationships in total. The relationships are all like 9-11 without "symmetry" and "opposite direction". The tail node is encoded with 0-len(size). Now I The reproduction result is not ideal. I guess it is because the relational data is not processed well. I don’t know if this is the case?
* **User**: Ask if the entity_id in raw_train.txt and the entity_id and relation_id in kg.txt are in the knowledge graph of Microsoft Satori knowledge graph? How to download this knowledge map? **Wang**: Hello! Yes, but this knowledge map is used internally by Microsoft, so the ID has also been anonymized and cannot be used directly by the outside world.



# Things I Learned:
1. 