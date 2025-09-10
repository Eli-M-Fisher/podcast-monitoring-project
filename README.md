
# **My report for the test project - Listener - podcast-monitoring-project**

## podcast-monitoring-project

A system for extracting data and audio files (in this case podcasts) that transcribes and analyzes what is said in a podcast and categorizes the content according to parameters

### Summary:

In this project test I had to create a system that takes podcast content, processes their content, that is, transcribes the speech into text (ttc).
We then analyze the risk level of the content according to relevant word lists (which come encrypted) and allow researchers, after the process I performed, to query the information using queries. This is actually a system of microservices of Kafka, Elasticsearch, MongoDB, Kibana, and FastAPI.

### Instructions for running and using

##### My system requirements:

It's Docker, Python 3 of course, and that's it.
To install:

```
git clone ...

cd podcast-monitoring-project

docker-compose down -vdocker-compose up -d --build
# or
docker-compose up --build
```

### tests use and operation:

Go to `http://localhost:5601` which is Kibana,
Go to the `Discover` tab, then create an `Index Pattern`, and enter `podcasts_metadata_v2`.

There you can see ***metadata, transcription, and BDS analysis.***

##### Instant tests:

Go to `http://localhost:8000/docs`, where you can execute the queries in the order requested within each query in Description

### Code and system structure

Here I will list the folders of the program I built:

**producer_service:** Yes, I read audio files, and send metadata to Kafka with it.

**consumer_service:** Its role is to store metadata in Elasticsearch and the files. Information (podcasts) in Mongo.

**transcriber_service:** Its role is to perform speech to text with whisper, and then it updates the information again in es.

**analyzer_service:** Calculates all the classifications for testing: bds_percent, is_bds and bds_threat_level.

**query_service:** FastAPI for queries that can be performed to see data..

**common:** A shared logger file that I participate in for all files

### The thought process and different choices:

##### Development process I did:

- I immediately understood in the first stage that this was a ***pipeline*** system that was in the first stage a **Producer** and also a **Consumer**..
- Then I developed the rest in order as separate services accordingly:
  **Transcriber**
  **Analyzer**
  **Query Service** with fastAPI with endpoints for queries

##### Some of Problems I encountered:

- At first I was using Google STT which was slow and dependent on the cloud so I decided to switch to Whisper.

- ES update problem (different versions between body={"doc": ...} and doc=...), I updated to the latest version.

### Personal summary:

The parts that were challenging for me were making sure that the transfer of the indexed data of es would be uniform and updated every time in every service it goes through.

Writing complete and clear documentation including comments was challenging but very helpful.

It was also challenging to learn technologies or libraries along the way like Whisper

In the end, I tried to make a **simple and modular system** with all the order and conventions I learned about.

**Software author:** Eliyahu Fisher *(luchik fisher, l.i)*
