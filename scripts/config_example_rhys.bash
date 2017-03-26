#!/bin/bash

FIXR_GRAPH_EXTRACTOR=/home/ubuntu/FixrGraphExtractor
FIXR_GRAPH_INDEXER=/home/ubuntu/FixrGraphIndexer
FIXR_GRAPH_ISO_BIN=/home/ubuntu/FixrGraphIso/graph_build/src/fixrgraphiso/fixrgraphiso
FIXR_COMMUNITY_DETECTION=/home/ubuntu/FixrCommunityDetection
SPARK_SUBMIT_PATH=/home/ubuntu/spark-2.0.0-bin-hadoop2.7/bin/spark-submit

OUT_DIR=/home/ubuntu/example_extraction/rhys_extraction
REPO_LIST=/home/ubuntu/api-program-graphs/expeval/pattern_queries/1_SQLiteDatabase.ingest.deduped-hash.json

# Index options
MIN_METHODS=2
MIN_NODES=2
MIN_EDGES=3
MIN_COMMON_METHODS=2

# ISO OPTIONS
TIMEOUT=5
JOB_SIZE=5000
